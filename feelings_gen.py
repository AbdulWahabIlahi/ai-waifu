from textblob import TextBlob

def emotion_mapping(text):
    """
    Maps a given text to a single drastic emotion based on its sentiment polarity.
    
    :param text: str, input sentence to analyze
    :return: str, a single drastic emotion corresponding to the sentiment polarity
    """
    emotions_by_polarity = {
        (-0.9, -0.8): "despair",
        (-0.8, -0.7): "panic",
        (-0.7, -0.6): "shame",
        (-0.6, -0.5): "rage",
        (-0.5, -0.4): "disappointment",
        (-0.4, -0.3): "sadness",
        (-0.3, -0.2): "exhaustion",
        (-0.2, -0.1): "confusion",
        (-0.1, 0.0): "neutrality",
        (0.0, 0.1): "curiosity",
        (0.1, 0.2): "hope",
        (0.2, 0.3): "contentment",
        (0.3, 0.4): "pride",
        (0.4, 0.5): "excitement",
        (0.5, 0.6): "joy",
        (0.6, 0.7): "ecstasy",
        (0.7, 0.8): "bliss",
        (0.8, 0.9): "elation",
        (0.9, 1.0): "triumph"
    }
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    for (lower, upper), emotion in emotions_by_polarity.items():
        if lower <= polarity < upper:
            return emotion
    return "neutrality"

if __name__ == "__main__":
    input_text = input("Enter a sentence: ")
    print("Detected Emotion:", emotion_mapping(input_text))
