import requests
import json

def add_dominant_emotion(emotionScores):
    '''Examines a dictionary of emotion scores and adds the dominant_emotion of the item
    with the highest score'''

    highScore = 0
    dominantEmotion = None
    for (emotion, score) in emotionScores.items():
        if score > highScore:
            highScore = score
            dominantEmotion = emotion
    
    emotionScores.update({"dominant_emotion": dominantEmotion})
    return emotionScores

def emotion_detector(text_to_analyze):
    ''' Function to call the Watson emotion detection service and return the response'''
    emotionServiceUrl = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    inputDoc = { "raw_document": { "text": text_to_analyze } }  # dictionary with text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Request headers
    response = requests.post(url=emotionServiceUrl, json=inputDoc, headers=header)  # Send POST request emotion service

    print(response.status_code)

    if response.status_code == 400:
        scores = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    else:
        responseDoc = json.loads(response.text)

        # Build the base scores dictionary from the response
        scores = {
            "anger": responseDoc["emotionPredictions"][0]["emotion"]["anger"],
            "disgust": responseDoc["emotionPredictions"][0]["emotion"]["disgust"],
            "fear": responseDoc["emotionPredictions"][0]["emotion"]["fear"],
            "joy": responseDoc["emotionPredictions"][0]["emotion"]["joy"],
            "sadness": responseDoc["emotionPredictions"][0]["emotion"]["sadness"]
        }
        
        # Find and add the dominant emotion
        add_dominant_emotion(scores)

    return scores  # return the scores
    