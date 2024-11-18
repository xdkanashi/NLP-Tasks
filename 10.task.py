from googletrans import Translator #pip install googletrans==4.0.0-rc1

translator = Translator()
texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

for text in texts:
    translated = translator.translate(text, src="lv", dest="en")
    print(f"{text} -> {translated.text}")