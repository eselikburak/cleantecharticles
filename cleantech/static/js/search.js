
$(document).ready(function () {
    // Listen searchbox
    $("#searchbox").on("input", function () {
        if (this.value.length == 1 || this.value.length % 3 == 0) {
            $("#search_results").html('')
            $.ajax({
                url: "/blog/search/",
                type: "get",
                data: {
                    searchbox_text: this.value
                },
                success: function (responce) {
                    results = JSON.parse(responce.search_results);
                    $("#searchcard").css("display", "block");
                    if (results == false) {
                        // 
                        let x = document.getElementById("searchbox").value;
                        if (x.length < 1) {
                            $("#searchcard").css("display", "none");

                        } else {
                            $("#search_results").html('')
                            let msg = "No Result!"
                            $("#search_results").html($("#search_results").html() + "<p class='list-group-item text-warning'> - " + msg + "</p>");
                        };
                    } else {
                        for (let i = 0; i < results.length; i++) {
                            $("#search_results").html($("#search_results").html() + "<a class='list-group-item'> - " + results[i].fields.title + "</a>");
                            $("#search_results > a:last").attr("href", '/blog/post/' + results[i].fields.slug);
                        };
                    };
                }
            });
        };
    });

});
