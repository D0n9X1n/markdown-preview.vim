$(document).ready(function () {
    setInterval("refresh()", 1000);
});

function refresh() {
    $.get("http://localhost:20016").done(function (data) {
        $("body").html(data);
        $('pre code').each(function (i, block) {
            hljs.highlightBlock(block);
        });
    });
}
