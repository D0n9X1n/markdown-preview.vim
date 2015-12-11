$.get("http://localhost:20013").done(function (data) {
    $("body").html(data);
    $('pre code').each(function (i, block) {
        hljs.highlightBlock(block);
    });
});
