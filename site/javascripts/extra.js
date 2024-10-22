(function() {
    var naryaLexer = new RegExp("language-narya");
    var codeBlocks = document.querySelectorAll('pre code'); 
    for (var i = 0; i < codeBlocks.length; i++) {
        if (naryaLexer.test(codeBlocks[i].className)) {
            console.log("Narya code block found");
            hljs.highlightElement(codeBlocks[i]);
        }
    }
})();