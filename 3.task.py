import re

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(re.findall(r'\b\w+\b', text1.lower()))
words2 = set(re.findall(r'\b\w+\b', text2.lower()))
common_words = words1.intersection(words2)
similarity = len(common_words) / ((len(words1) + len(words2)) / 2) * 100

print(f"Sakritības līmenis: {similarity:.2f}%")
