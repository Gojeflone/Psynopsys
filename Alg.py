from watson_developer_cloud import ToneAnalyzerV3
import simplejson
import json
import os
import string


# testInput = json.dumps(
#     {
#         "document_tone":{
#             "tone_categories": [
#                 {
#                     "tones": [
#                         { 
#                         "score": 0.134622,
#                         "tone_id": "anger",
#                         "tone_name": "Anger"
#                         },
#                         {
#                         "score": 0.013182,
#                         "tone_id": "disgust",
#                         "tone_name": "Disgust"
#                         },
#                         {
#                         "score": 0.092403,
#                         "tone_id": "fear",
#                         "tone_name": "Fear"
#                         },
#                         {
#                         "score": 0.013411,
#                         "tone_id": "joy",
#                         "tone_name": "Joy"
#                         },
#                         {
#                         "score": 0.635069,
#                         "tone_id": "sadness",
#                         "tone_name": "Sadness"
#                         }
#                     ]
#                 }
#             ]
#         }
#     }
# )

def runThingy():
    tone_analyzer = ToneAnalyzerV3(
    version='2016-05-19',
    username='03b0c6d9-036e-426c-a631-1a1487b760df',
    password='ljbXEZzJHdnX'
    )

    #tone = tone_analyzer.tone(json.load(testInput('document_tone')['text'], tones ='emotion'),
    #content_type ='application/json')

    #with open(os.path.dirname(__file__) + 'tone.json') as tone_json:
    #  tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
    #    content_type='application/json')

    print("Making JSON")
    with open(str.join(os.path.dirname(__file__), 'tone.json')) as tone_json:
        tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
            content_type='application/json')

    #tone(text, tones=None, sentences=None, content_type='text/plain')


def sadFreqAnalyzer(jsonOutput) :
    print("Running FreqAnalyzer")
    #Variable Initialization
    numTones = 0
    totalSad = 0
    avgSad = 1
    totalFear = 0
    avgFear= 0
    totalAnger = 0
    avgAnger = 0
    totalNegEmotion = 0
    negEmotions = ["Sadness", "Fear", "Anger"]

    #Counting number of tones, negative tones, 
    for jsonObj in jsonOutput.document_tone['tones']:
        numTones += 1
        for emotion in negEmotions:
            if jsonOutput.document_tone['tones']['tone_name'] == emotion:
                if emotion == negEmotions[0]:
                    totalSad += 1
                    totalNegEmotion += 1
                    avgSad += jsonOutput.document_tone['tones'][score]
                elif emotion == negEmotions[1]:
                    totalFear += 1
                    totalNegEmotion += 1
                elif emotion == negEmotions[2]:
                    totalAnger += 1
                    totalNegEmotion += 1
    
    avgSad = totalSad / avgSad
    highRisk = (totalSad) * 0.9
    medRisk = (totalSad) * 0.6
    lowRisk = (totalSad) * 0.3

    #return level of risk
    if avgSad >= highRisk:
        retJson = "{retObj: This person may be showing many signs of depression, or excessive amounts of sadness.}"
        print("High")
        return json.dumps(retJson)

    elif avgSad >= medRisk:
        retJson = "{retObj: person may be showing signs of depression, or moderate amounts of sadness.}"
        print("Med")
        return json.dumps(retJson)
        
    else:
        retJson = "{retObj: This person may be showing little to no signs of depression, and little to no amounts of sadness.}"
        print("Low")
        return json.dumps(retJson)



var jsonFile = runThingy()
sadFreqAnalyzer(jsonFile)