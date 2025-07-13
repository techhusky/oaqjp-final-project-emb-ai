import requests

def emotion_detector(text_to_analyze):
    ''' Function to call the Watson emotion detection service and return the response'''
    emotionServiceUrl = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    inputDoc = { "raw_document": { "text": text_to_analyze } }  # dictionary with text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Request headers
    response = requests.post(url=emotionServiceUrl, json=inputDoc, headers=header)  # Send POST request emotion service
    return response.text  # Return the response