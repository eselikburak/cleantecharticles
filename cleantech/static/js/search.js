
$(document).ready( function() {
    $("#searchbox").on("input", function () {
        $("#search_results").html('')
        $.ajax({
            url: "/blog/search/",
            type: "get",
            data: {
                searchbox_text: this.value
            },
            success: function (responce) {
                results = JSON.parse(responce.search_results);
                $("#searchcard").removeClass("d-none");
                if (results == false) {
                    // Do nothing or add 
                    $("#searchcard").addClass("d-none");
                } else {
                    for (let i = 0; i < results.length; i++) {
                        $("#search_results").html($("#search_results").html() + "<a class='list-group-item'>"+ results[i].fields.title + "</a>");
                        $("#search_results > a:last").attr("href", '/blog/post/' + results[i].fields.slug);
                    };
                };
            }
        });

    });

});