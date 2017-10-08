document.addEventListener("DOMContentLoaded", function() {
    // Get the ID of the result element
    var results = document.getElementById("result");
    // Make an empty array for the entries
    var entriesJSON = [];
    // When the analyze button is clicked...
    document.getElementById("le button").addEventListener("click", function() {
        // Split the entries newlines and assign them to entriesArray
        entriesJSON = document.getElementById("comment").value.split(/\n/);
        // Log the array in the console so I can see it
        console.log(entriesArray);
        // Put the results in the HTML
        results.innerHTML = `
        <h2 style="font-size: 3em; padding-top: .5em" class="text-center"><strong>Result:</strong></h2>
        <h2 style="text-decoration: underline; font-size: 2.5em; padding-top: .5em" class="text-center">Enter Results</h2>
        `
        // Scroll to the bottom of the page to see the results
        window.scrollTo(0,document.body.scrollHeight);
    
    });
});