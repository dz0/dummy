import json
import py

def jqueryfy(id):
    """replace tricky characters to underscores"""
    import re
    result = re.sub(r"[.<>\[\] ]", '_', id)
    # print("DBG: jquerify", result)
    return result

def render_html(visited_lines, codes, call_map, watched_values):

    def inlines_tpl( line_id , indent):
        if line_id not in call_map:
            return ""
            
        calls = call_map[ line_id ] # get calls from current line
        togglers = []
        inline_containers = []
        for code_id in calls:  
            code_id_jq = jqueryfy(code_id)
            toggler_html = f"""
                            <span class='toggler button' id='toggler_{code_id_jq}' tiltle='{code_id}'
                                onclick='smart_toggle(this)' 
                                onmouseover='style_inlined(this, "border-width", "3px")' 
                                onmouseout='style_inlined(this, "border-width", "1px")'>&#8597;</span>"""
            inline_container_html = f"""<div class='inlined' id='inlined_{code_id_jq}' style="margin-left: {indent}ch;"></div>"""
            
            togglers.append( toggler_html )
            inline_containers.append( inline_container_html )
        
        return ('\n'.join(togglers) + 
                '\n\n' +
                '\n'.join(inline_containers) 
                )
       
    def watches_tpl( line_id, indent ):
        watches = watched_values.get( line_id )    
        if watches:
            def gen_html_table( mtx ):
                from py.xml import html
                
                result  = html.table(
                    html.thead( html.tr( [html.th( x ) for x in mtx[0] ] ) ),  # header
                    html.tbody( 
                            *[ html.tr( [html.td( x ) for x in row] )   # rows
                                for row in mtx[1:] ] 
                                ),
                    class_="fixed_headers"
                ) 
                # make it fixed height scrollable # https://codepen.io/tjvantoll/pen/JEKIu
                # result = str(result) + """
                # """

                return result 
                
            # watches = json.dumps( watches )
            watches = gen_html_table( watches )
            container = f"""<div class='watches' id='watches_{line_id}' title='watches: {line_id}' style="margin-left: {indent}ch;">{watches}</div>"""
            toggler =   f"""<span class='toggler button watch-toggler' id='toggler_watches_{line_id}' tiltle='toggle watch'
                                onclick='toggle_watch(this)' >&#128269;</span>"""

            return container, toggler
        else:
            return "", ""
        
    def line_tpl(line, module_id, lineno):
        line_id =  join_ids( module_id, lineno)  
        line_id_jq = jqueryfy(line_id)
        visited = "visited" if line_id in visited_lines  else ""
        
        indent = len(line)-len(line.lstrip())
        inlines = inlines_tpl( line_id, indent )
        watches, watches_toggler = watches_tpl( line_id, indent )
        return f"""<div id='{line_id_jq}' class='line {visited}'>
                {watches}
                <span class="line-code" title='{line_id}'>{line}</span>  
                {watches_toggler} 
                {inlines} 
                </div>"""
        
    def code_tpl(id, code):
        """code is inspect.sourcelines"""
        lines, start_lineno = code
        module_id = id.split(SEP_4ID)[0]
        id_jq = jqueryfy( id )
        
        def syntax_highlight(src):
            from pygments import highlight
            from pygments.lexers import Python3Lexer as PythonLexer 
            from pygments.formatters import HtmlFormatter

            formatter = HtmlFormatter(cssclass="code", nowrap=True)
            result = highlight(src, PythonLexer(encoding="utf-8"), formatter)
            
            # remove: <div class="code"><pre> and corresponding endings
            start = '<div class="code"><pre>'
            start = '</div></pre>'
            
            return result

        def dedent_and_highlight(lines):
            orig_code = ''.join(lines) 
            dedented_code = str( py.code.Source( orig_code) )
            # dedented_code = orig_code
            
            # print( "dedented_code\n", dedented_code)
            dedented_code = syntax_highlight( dedented_code )
            
            lines = dedented_code.split("\n") # will loose \n at the ends...
            # print( 'DBG dedent', orig_code, dedented_code, dedented_code, lines )
            return lines
            
        if "<lambda>" not in lines[0]:
            lines[0] = lines[0].rstrip('\n') + "     # "+id +'\n' # inject comment about it's origin
        lines = dedent_and_highlight(lines) 
        
        html_lines = [line_tpl(x, module_id, start_lineno+nr ) for nr, x in enumerate(lines) ]
        html_code = ''.join( html_lines )
        return f"""
    <h4>{id}</h4>
    <div id='code_{id_jq}' class='code'>
    {html_code}
    </div>
        """



    codes_html = '\n\n'.join([ code_tpl(id, code) for id, code in codes.items()] )

            
    html = open('mytracer.tpl.html').read()
    html = html.replace("{{visited_lines}}", str(visited_lines) )
    html = html.replace("{{codes}}", str(codes_html) )

    html = html.replace("{{call_map}}", json.dumps(call_map, indent=4) )
    
    with open('mytracer.html', 'w') as f:
        f.write( html )
        
        from pygments.formatters import HtmlFormatter
        f.write( "\n\n<style>\n%s\n.code  { background: #fff; }\n</style>" % HtmlFormatter().get_style_defs('.code') )
