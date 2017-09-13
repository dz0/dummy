import py
def render_html(visited_lines, codes, call_map, traced_values):

    def inlines_tpl( line_id , indent):
        if line_id not in call_map:
            return ""
            
        calls = call_map[ line_id ] # get calls from current line
        togglers = []
        inline_containers = []
        for code_id in calls:  
            toggler_html = f"""
                            <span class='toggler button' id='toggler_{code_id}'
                                onclick='smart_toggle(this)' 
                                onmouseover='style_inlined(this, "border-width", "3px")' 
                                onmouseout='style_inlined(this, "border-width", "1px")'>&#8597;</span>"""
            inline_container_html = f"""<div class='inlined' id='inlined_{code_id}' style="margin-left: {indent}ch;"></div>"""
            
            togglers.append( toggler_html )
            inline_containers.append( inline_container_html )
        
        return ('\n'.join(togglers) + 
                '\n\n' +
                '\n'.join(inline_containers) 
                )
        
    def line_tpl(line, module_id, lineno):
        id = join_ids( module_id, lineno) 
        visited = "visited" if id in visited_lines  else ""
        
        indent = len(line)-len(line.lstrip())
        inlines = inlines_tpl( id, indent )
        return f"""<div id='{id}' class='line {visited}'><span class="line-code">{line}</span>   \n{inlines}</div>"""
        
    def code_tpl(id, code):
        """code is inspect.sourcelines"""
        lines, start_lineno = code
        module_id = id.split(SEP_4ID)[0]
        
        def dedent(lines):
            orig_code = ''.join(lines) 
            dedented_code = str( py.code.Source( orig_code) )
            lines = dedented_code.split("\n") # will loose \n at the ends...
            # print( 'DBG dedent', orig_code, dedented_code, dedented_code, lines )
            return lines
            
        lines = dedent(lines) 
        
        html_lines = [line_tpl(x, module_id, start_lineno+nr ) for nr, x in enumerate(lines) ]
        html_code = ''.join( html_lines )
        return f"""
    <h4>{id}</h4>
    <div id='code_{id}' class='code'>
    {html_code}
    </div>
        """



    codes_html = '\n\n'.join([ code_tpl(id, code) for id, code in codes.items()] )

            
    html = open('mytracer.tpl.html').read()
    html = html.replace("{{visited_lines}}", str(visited_lines) )
    html = html.replace("{{codes}}", str(codes_html) )

    import json
    html = html.replace("{{call_map}}", json.dumps(call_map, indent=4) )
    
    with open('mytracer.html', 'w') as f:
        f.write( html )
