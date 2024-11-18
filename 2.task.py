from langid import classify # pip install langid

texts = ["Šodien ir saulaina diena.", "Today is a sunny day.", "Сегодня солнечный день."]
languages = [classify(text)[0] for text in texts]
print(languages)
