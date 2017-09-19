function make_wathces_scroll_fixed_header(){

        //  https://stackoverflow.com/a/25902860/4217317
        var tables = document.getElementsByClassName("watches")
        for (var i = 0; i < tables.length; i++) {
            tables[i].addEventListener("scroll",function(){
               var translate = "translate(0,"+this.scrollTop+"px)";
               this.querySelector("thead").style.transform = translate;
            });
        }

}

function init(){
    
   // jQuery methods go here...
   // $(".inlined").hide();
   
   $first_code =  $("#codes .code").first();
    
   $("#trace").prepend( $first_code.html() );
   make_wathces_scroll_fixed_header();

   // $(".line.visited .line-code").each(
        // function(){  
            // var title = $(this).parent().prop('id');
            // this.title = title;
    // });

   // $(".toggler").each(
        // function(){  
            // call_id = this.id.substr(  "toggler_".length );
            // this.title = call_id;
    // });
   
}

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

function toggle_watch( toggler ){ 
    
    var call_id = toggler.id.substr(  "toggler_".length );
    $(toggler).siblings(".watches").toggle();
        
}
    
function smart_toggle( toggler ){

        toggler = (typeof toggler !== 'undefined') ?  toggler : this;   // defaults to "this" -- element calling the function
        
        $target = get_inlined_jq(toggler);
        if ($target.is(":visible")) {
            $target.hide();
            $(toggler).addClass("closed").removeClass("opened");
            
        }
        else show_inlined($target);
}

function expand_all_recursively( expander ){

    // get corresponding inlined containers
    $(expander).siblings(".inlined").each( function(){
        show_inlined( $(this), true );
    });
}

MAX_RECURSION_DEPTH = 7;

function show_inlined($container, recurse, depth){
    
    recurse = (typeof recurse !== 'undefined') ?  recurse : false; // default
    depth = (typeof depth !== 'undefined') ?  depth : 0; // default
    
    var id = $container.prop('id');
    
    // if (typeof id !== 'undefined'){ // if we don't find valid container
        // console.log( "show all found container with no id", $container);
        // return;
    // }
        
        
    var call_id = id.substr(  "inlined_".length );
    var $toggler = $container.siblings("#toggler_"+call_id).first().removeClass('closed').addClass('opened');
 
    var $code = $("#codes #code_"+call_id).first();  // take from #codes list
    
    if($container.text().trim()=="") // if empty
    {
        // $container.append(  $code.html() ); // TODO: attr('innerHTML')?? should take initial stuff
        $container.append(  $code.prop('outerHTML') ); // TODO: attr('innerHTML')?? should take initial stuff
    }
        
    $container.show();
    make_wathces_scroll_fixed_header();
    
    if(recurse && (depth < MAX_RECURSION_DEPTH) ){
        
        $container.find(".inlined").each( function(){
            show_inlined($(this), true, depth+1);
        });
        
        // $togglers = $container.find(".toggler");
        // $togglers.each( function(){
            // $target = get_inlined_jq(this);
            // show_inlined($target, true, depth+1);
        // });
    }
}
