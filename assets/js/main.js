document.addEventListener("DOMContentLoaded", function() {
  
    // Get the ID of the result element
    
    var results = document.getElementById("result");
    
    // Make an empty array for the entries
    
    var entriesJSON = {};
    
    // When the analyze button is clicked...
    
    document.getElementById("le button").addEventListener("click", function() {
      
      var lmao = ["This person may be showing many signs of depression, or excessive amounts of sadness.", "This person may be showing signs of depression, or moderate amounts of sadness.", "This person may be showing little to no signs of depression, and little to no amounts of sadness."][Math.floor((Math.random()*2) +1)];
      
        // Split the entries at newlines and assign them to the JSON
        
        for (var i = 0; i < document.getElementById("comment").value.split(/\n/).length; i++) {
          
          entriesJSON[i] = document.getElementById("comment").value.split(/\n/)[i];
          
          if (document.getElementById("comment").value === "") {
            results.innerHTML = `
              <h2 style="font-size: 2.5em; color: red; padding-top: .5em" class="text-center">Nothing entered.</h2>
              `;
          } else {
          results.innerHTML = `
        <h2 style="font-size: 2.5em; padding-top: .5em" class="text-center">${lmao}</h2>
        `;
        }
      }
        
        // Log the JSON in the console so I can see it
        
        console.log(entriesJSON);
        
        // Scroll to the bottom of the page to see the results
        
        window.scrollTo(0,document.body.scrollHeight);
    
    });
    //jQuery.get();
});