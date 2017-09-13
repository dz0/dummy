

function get_inlined_jq( toggler ){
        var id = toggler.id;
        call_id = id.substr(  "toggler_".length );

        // get corresponding closest container?
        return $(toggler).siblings("#inlined_"+call_id).first();
}

function style_inlined( toggler, prop, val ){
    $target = get_inlined_jq(toggler);
    $target.css( prop, val );
}

function smart_toggle( toggler ){

        toggler = (typeof toggler !== 'undefined') ?  toggler : this;   // defaults to "this" -- element calling the function
        
        $target = get_inlined_jq(toggler);
        if ($target.is(":visible")) $target.hide();
        else show_inlined($target);
    
}

MAX_RECURSION_DEPTH = 3;

function show_inlined($container, recurse, depth){
    
    recurse = (typeof recurse !== 'undefined') ?  recurse : true; // default
    depth = (typeof depth !== 'undefined') ?  depth : 0; // default
    
    var id = $container.prop('id');
    var call_id = id.substr(  "inlined_".length );
 
    var $code = $("#codes #code_"+call_id).first();  // take from #codes list
    
    if($container.text().trim()=="") // if empty
    {
        // $container.append(  $code.html() ); // TODO: attr('innerHTML')?? should take initial stuff
        $container.append(  $code.prop('outerHTML') ); // TODO: attr('innerHTML')?? should take initial stuff
    }
        
    $container.show();
    
    if(recurse && (depth < MAX_RECURSION_DEPTH) ){
        $togglers = $container.find(".toggler");
        $togglers.each( function(){
            $target = get_inlined_jq(this);
            show_inlined($target, true, depth+1);
        });
    }
}
