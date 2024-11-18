import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = re.sub(r'@\w+|http\S+|[^a-zA-ZāčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ\s]', '', text).lower().strip()
print(cleaned_text)
