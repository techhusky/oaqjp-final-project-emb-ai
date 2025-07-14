'''Emotion Detector Flask Server Application'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    '''Provided the textToAnalyze parameter, call the emotion_detector to analyze a 
    statement and return a formatted analysis'''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion detector to analyze
    emotion = emotion_detector(text_to_analyze)

    # Extract the emotion values from the r
    anger = emotion["anger"]
    disgust = emotion["disgust"]
    fear = emotion["fear"]
    joy = emotion["joy"]
    sadness = emotion["sadness"]
    dominant = emotion["dominant_emotion"]

    response = "Invalid text! Please try again!"

    if dominant is not None:
        response = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant}."
        )

    return response

@app.route("/")
def render_index_page():
    '''Render index.html as the default page'''
    return render_template("index.html")

# Start the flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
