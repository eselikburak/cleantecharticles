
// Delete if there is a message on the page! 
if ($("#message")) {
    setTimeout(() => {
        $("#message").remove();
    }, 4000)
}


// Source: https://codepen.io/JacobLett/pen/jzdYPz 
$(document).ready(function () {
    // executes when HTML-Document is loaded and DOM is ready

    $(".card").hover(
        function () {
            $(this).addClass('shadow-lg border border-dark').css('transform', 'scale(1.03)');
        }, function () {
            $(this).removeClass('shadow-lg border border-dark').css('transform', 'scale(1.0)');
        }
    );

    // document ready  
});

// To delete display: inline-block(this is defaul in ck-editor!) inside add new article or edit article pages !
$(".django-ckeditor-widget").css("display", "");


// To Change Title When a user leave the current tap!
var title = document.title;
var title_message = "Go back to learning! ";
var titleInterval;
document.addEventListener("visibilitychange", (event) => {
    if (document.visibilityState == "visible") {
        document.title = title;
        clearInterval(titleInterval);
    } else {
        titleInterval = setInterval(changeTitle, 2000);
    };

});

function changeTitle() {
    if (document.title == title) {
        document.title = title_message + title;
    } else {
        document.title = title;
    }
};
