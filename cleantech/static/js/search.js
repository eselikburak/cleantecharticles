
$(document).ready(function () {
    // Listen searchbox
    $("#searchbox").on("input", function () {
        $.ajax({
            url: "/blog/search/",
            type: "get",
            data: {
                searchbox_text: this.value
            },
            success: function (responce) {
                results = JSON.parse(responce.search_results);
                $("#search_results").html(''); // Clean inside search result-s box if 200. If you put this top of ajax the box is flashing because of it is waiting the responce! 
                $("#searchcard").css("display", "block"); // Show search result-s box 
                $("#categories").fadeOut(500); // Delete Categories Section
                if (results == false) {
                    let x = document.getElementById("searchbox").value;
                    if (x.length < 1) {
                        $("#searchcard").css("display", "none");
                        $("#categories").fadeIn(250);
                    } else {
                        $("#search_results").html('')
                        let msg = "No results for '" + x + "'";
                        $("#search_results").html($("#search_results").html() + "<p class='list-group-item text-danger'> - " + msg + "</p>");
                    };
                } else {
                    for (let i = 0; i < results.length; i++) {
                        $("#search_results").html($("#search_results").html() + "<a class='list-group-item'> - " + results[i].fields.title + "</a>");
                        $("#search_results > a:last").attr("href", '/blog/post/' + results[i].fields.slug);
                    };
                };
            }
        });
    });

});
