function get_days() {
    $.ajax({
        url: "/ajax_days",
        type: "POST",
        dataType: "json",
        success: function (data) {
            $("#days_td_id").empty();
            var obj = JSON.parse(data);
            $.each(obj, function (i, val) {
                var img = $('<img id="nums_json">');
                img.attr('src', "../static/entity/crow_cat_console/" + val + ".png");
                img.appendTo('#days_td_id');
            })
        }
    });
}