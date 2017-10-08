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
        //
        var ToneAnalyzerV3 = require('watson-developer-cloud/tone-analyzer/v3');
        
        var tone_analyzer = new ToneAnalyzerV3({
          username: '{765733e9-c353-46ac-a622-35a614caf5fe}',
          password: '{mYsZDMBl1wBY}',
          version_date: '{2017-09-28}',
          headers: {
            'X-Watson-Learning-Opt-Out': 'true'
          }
        });
        
        var params = {
          // Get the text from the JSON file.
          text: require('test.json').text,
          tones: 'emotion'
        };
        
        tone_analyzer.tone(params, function(error, response) {
          if (error)
            console.log('error:', error);
          else
            console.log(JSON.stringify(response, null, 2));
          }
        );
        //
    });
});