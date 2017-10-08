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