import sys
from textblob import TextBlob

print("Press 1 for English to French")
print("Press 2 for English to Spanish")
print("Press 3 for Englsih to Italian")
print("Press 4 for English to Russian")
print("Press 5 for English to Hindi")

try:
	n = input("Enter Number: ")
	n = int(n)
	if n not in range(1, 6):
		raise error
except:
	print("Wrong Input")
	sys.exit()

codes = {1: "fr", 2: "es", 3: "it", 4: "ru", 5: "hi"}

eng_code = "en"
tr_code = codes[n]

word = input("Enter Sentence: ")
word = TextBlob(word)

try:
	trans = word.translate(from_lang=eng_code, to=tr_code)
	print("Translated Sentence: ", end="")
	print(trans)
except:
	print("Wrong Sentence")
	sys.exit()
