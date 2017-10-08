import json
from tone_analyzer_v3 import ToneAnalyzerV3

class SadTone():

    tone_analyzer = ToneAnalyzerV3(
    version='{2017-09-21}',
    username='{"765733e9-c353-46ac-a622-35a614caf5fe"}',
    password='{"mYsZDMBl1wBY"}'
    )

    tone = tone_analyzer.tone(json.load(testInput['document_tone']['tone_categories'], tones='emotion')
        content_type='text/plain')


    tone(text, tones=None, sentences=None, content_type='text/plain')

    testInput = json.dumps(
    "document_tone" {
        "tone_categories" [
        {
            "tones": [
            {
                "score": 0.134622,
                "tone_id": "anger",
                "tone_name": "Anger"
            },
            {
                "score": 0.013182,
                "tone_id": "disgust",
                "tone_name": "Disgust"
            },
            {
                "score": 0.092403,
                "tone_id": "fear",
                "tone_name": "Fear"
            },
            {
                "score": 0.013411,
                "tone_id": "joy",
                "tone_name": "Joy"
            },
            {
                "score": 0.635069,
                "tone_id": "sadness",
                "tone_name": "Sadness"
            }
    )

    def sadFreqAnalyzer(jsonOutput)
        #Variable Initialization
        numTones = 0
        totalSad = 0
        avgSad = 0
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
                    if emotion = negEmotions[0]:
                        totalSad += 1
                        totalNegEmotion += 1
                        avgSad += jsonOutput.document_tone['tones'][score]
                    elif emotion = negEmotions[1]:
                        totalFear += 1
                        totalNegEmotion += 1
                    elif emotion = negEmotions[2]:
                        totalAnger += 1
                        totalNegEmotion += 1
        
        avgSad / totalSad = avgSad
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


    sadFreqAnalyzer(testInput)