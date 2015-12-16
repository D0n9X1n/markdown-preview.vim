$(document).ready(function () {
    setTimeout("refresh()", 200);
});

function refresh() {
    $.get("http://localhost:20016").done(function (data) {
        if (data) {
            $("body").html(data);
            $('pre code').each(function (i, block) {hljs.highlightBlock(block);});
            // $('html, body').animate({scrollTop:$('#anchor').offset().top}, 800);
            $("html, body").animate({
                scrollTop: (($('#anchor').offset().top - 50) + "px")
            }, {
                duration: 10,
                easing: "swing"
            });
        }
        setTimeout("refresh()", 200);
    });
}
