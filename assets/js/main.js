document.addEventListener("DOMContentLoaded", function() {
    var results = document.getElementById("result");
    var entriesArray = [];
    document.getElementById("le button").addEventListener("click", function() {
        entriesArray = document.getElementById("comment").value.split(/\n/);
        console.log(entriesArray);
        results.innerHTML = `
        <h2 style="font-size: 3em; padding-top: .5em" class="text-center"><strong>Result:</strong></h2>
        <h2 style="text-decoration: underline; font-size: 2.5em; padding-top: .5em" class="text-center">You\'re fuckin\' gay</h2>
        `
        window.scrollTo(0,document.body.scrollHeight);
    });
});