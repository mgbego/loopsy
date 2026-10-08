
CodeMirror.defineMode("while", function() {
   return {
      token: function(stream) {
         if(stream.match(/\b(if|else|while|skip|inv)\b/)) {
            return "keyword";
         }
         if (stream.match(/\b(true|false)\b/)){
            return "tf";
         }
         if(stream.match(/\d+/)) {
            return "number";
         }
         if(stream.match(/:=|==|<=|>=|&&|\|\||\+|-|\*|!|>|</)) {
            return "operator";
         }
         if(stream.match(/\(|\)|,|;|{|}/)) {
            return "punctuation";
         }
         if(stream.match(/_?[a-z][a-zA-Z0-9]*/)) {
            return "variable";
         }
         stream.next();
         return null;
      }
   };
});
//checks statement
const statementEditor = CodeMirror(document.getElementById("statement-editor"),{
   lineNumbers: true,
   mode: "while"
});
//checks assume
const assumeEditor = CodeMirror(document.getElementById("assume-editor"),{
   lineNumbers: false,
   mode: "while"
});
//checks assert
const assertEditor = CodeMirror(document.getElementById("assert-editor"),{
   lineNumbers: false,
   mode: "while"
});

window.runCode = async function() {
   const code = statementEditor.getValue();
   const assume = assumeEditor.getValue();
   const assert_ = assertEditor.getValue();
   try{
         const response = await fetch("/run", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ assume: assume, code: code, assert_: assert_ })
         });
        result = await response.json();
   }
    catch(error){
        document.querySelector(".output-box textarea").value = error.message;
        
   }
    document.querySelector(".output-box textarea").value = result.output;
   
}

window.clearOutput = function() {
    document.querySelector(".output-box textarea").value = "";
}

