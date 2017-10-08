from tone_analyzer_v3 import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
  version='{2017-09-21}',
  username='{"765733e9-c353-46ac-a622-35a614caf5fe"}',
  password='{"mYsZDMBl1wBY"}'
)

with open(join(dirname(__file__), 'tone.json')) as tone_json:
  tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
    content_type='text/plain')


tone(text, tones=None, sentences=None, content_type='text/plain')
