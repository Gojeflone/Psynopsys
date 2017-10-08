document.addEventListener("DOMContentLoaded", function() {
  
    // Get the ID of the result element
    
    var results = document.getElementById("result");
    
    // Make an empty array for the entries
    
    var entriesJSON = {};
    
    // When the analyze button is clicked...
    
    document.getElementById("le button").addEventListener("click", function() {
      
        // Split the entries at newlines and assign them to the JSON
        
        for (var i = 0; i < document.getElementById("comment").value.split(/\n/).length; i++) {
          
          entriesJSON[i] = document.getElementById("comment").value.split(/\n/)[i];
          results.innerHTML += `
        <h2 style="font-size: 2.5em; padding-top: .5em" class="text-center">${entriesJSON[i]}</h2>
        `;
        }
        
        // Log the JSON in the console so I can see it
        
        console.log(entriesJSON);
        
        // Scroll to the bottom of the page to see the results
        
        window.scrollTo(0,document.body.scrollHeight);
    
    });
});