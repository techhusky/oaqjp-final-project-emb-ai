import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionAnalyzer(unittest.TestCase):
    def test_joy(self):
        emotion = emotion_detector("I am glad this happened")
        self.assertEqual("joy", emotion["dominant_emotion"])

    def test_anger(self):
        emotion = emotion_detector("I am really mad about this")
        self.assertEqual("anger", emotion["dominant_emotion"])

    def test_disgust(self):
        emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual("disgust", emotion["dominant_emotion"])

    def test_sadness(self):
        emotion4 = emotion_detector("I am so sad about this")
        self.assertEqual("sadness", emotion4["dominant_emotion"])

    def test_fear(self):
        emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual("fear", emotion["dominant_emotion"])

unittest.main()