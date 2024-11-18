from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=-1)

sentences = [
    "Šis produkts ir lielisks, esmu ļoti апmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]
neutral_keywords = ["neitrāls", "nekas īpašs", "parasts", "vidējs", "tikai", "normāls", "bez emocijām"]

def get_sentiment(sentence):
    if any(word in sentence.lower() for word in neutral_keywords):
        return "Neitrāls"
    sentiment = sentiment_analyzer(sentence)[0]["label"]
    return "Pozitīvs" if sentiment == "5 stars" else "Negatīvs" if sentiment == "1 star" else "Neitrāls"

for sentence in sentences:
    print(f"Teikums: {sentence}\nNoskaņojums: {get_sentiment(sentence)}\n")
