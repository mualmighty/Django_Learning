$(function () {

    $("#all_types").click(function (){

        console.log("全部类型");

        var $all_types_container = $("#all_types_container");
        $all_types_container.show();

        var $all_type = $(this);
        var $span = $all_type.find("span").find("span");
        $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    })

    $("#all_types_container").click(function (){

        var $all_type_container = $(this);
        $all_type_container.hide();

        var $all_type = $("#all_types");
        var $span = $all_type.find("span").find("span");
        $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-down");

    })


    $("#sort_rule").click(function (){
        console.log("排序规则");
        var $sort_rule_container = $('#sort_rule_container');
        $sort_rule_container.slideDown();
    })

})