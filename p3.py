#!/usr/bin/env python

from googletrans import Translator
import re
from nltk.stem import WordNetLemmatizer




f_name = input("Data file? : ")
f = open(f_name, "r+")
data = f.read()

data = data.replace("\n", " ")

another = data
#data = data[:-1]

#remove puntuation 
#----------------
punc = '''!()[]{};:"\,<>./?@#$%^&*~।'''
for ele in data:
	if ele in punc:
		data = data.replace(ele, "")
uni = []
for i in range(len(data)):
	#print(data[i],"---->",ord(data[i]))
	uni.append(ord(data[i]))


lst = data.split()

temp = []
for i in range(len(lst)):
	temp.append(ord(lst[i][0]))



lang = []
for i in range(len(temp)):
	if (temp[i] <= 127):
		lang.append('English')
	elif (temp[i] >= 2432 and temp[i] <= 2559):
		lang.append('Bengali')
	elif (temp[i] >= 2304 and temp[i] <= 2431):
		lang.append('Hindi')
	elif (temp[i] >= 2560 and temp[i] <= 2687):
		lang.append('Punjabi')
	elif (temp[i] >= 2688 and temp[i] <= 2815):
		lang.append('Gujrati')
	elif (temp[i] >= 2816 and temp[i] <= 2943):
		lang.append('Oriya')
	elif (temp[i] >= 2944 and temp[i] <= 3071):
		lang.append('Tamil')
	elif (temp[i] >= 3072 and temp[i] <= 3199):
		lang.append('Telegu')
	elif (temp[i] >= 3200 and temp[i] <= 3327):
		lang.append('Kannada')
	elif (temp[i] >= 3328 and temp[i] <= 3455):
		lang.append('Malayalam')
	elif (temp[i] >= 69760 and temp[i] <= 69839):
		lang.append('Bhojpuri')
	elif ( (temp[i] >= 1536 and temp[i] <= 1791) or (temp[i] >= 1872 and temp[i] <= 1919) or (temp[i] >= 64336 and temp[i] <= 65023) or (temp[i] >= 65136 and temp[i] <= 65279) ):
		lang.append('Urdu')

for i in range(len(lst)):
	print("\"", lst[i], "\" is a/an ", lang[i], " word.")

data = another

print("\n---------------------------------------------------\n")

print("\nTarget Language List:")
print("\nEnter 'bn' for Bengali")
print("Enter 'en' for English")
print("Enter 'hi' for Hindi")
print("Enter 'pa' for Punjabi")
print("Enter 'gu' for Gujrati")
#print("Enter 'or' for Oriya")
print("Enter 'ta' for Tamil")
print("Enter 'te' for Telegu")
print("Enter 'kn' for Kannada")
print("Enter 'ml' for Malayalam")
print("Enter 'ur' for Urdu\n")
ter = input("Enter the target language: ");


translator = Translator()
result = translator.translate(data)  #By default english
result_ter = translator.translate(result.text, dest = ter)

#print(result.src)
#print(result.dest)
print("\nOriginal Text: ")
print(result.origin)
print("Translated Text: ")
print(result_ter.text)
#print(result.pronunciation)


punc = '''!()[]{};:"\,<>./?@#$%^&*_~।¯'''
res = result.text
for ele in res:
	if ele in punc:
		res = res.replace(ele, "")
res = res.lower()
data = res.split()

lemmatizer = WordNetLemmatizer()
temp = []
for i in data:
	temp.append(lemmatizer.lemmatize(i))


#print(temp)

pos = []
neg = []
c = 0
f1 = open("pos.txt", "r")
l = f1.readlines()
for line in l:
	pos.append(line.strip())
		
f2 = open("neg.txt", "r")
l2 = f2.readlines()
for line in l2:
	neg.append(line.strip())

#print(pos)
p = 0
n = 0

for i in temp:
	if i in pos:
		#print("pos: ",i)
		p += 1
	if i in neg:
		#print("neg: ",i)
		n += 1
#print(n, "  ", p)

print("====================Conclussion====================")
if(p+n > 0):
	if(p/(p+n) > 0.6):
		print("Sentiment type : Positive")
	elif(n/(p+n) > 0.55):
		print("Sentiment type : Negative")
	else:
		print("Sentiment type : Neutral")
else:
	print("Sentiment type : Neutral")
print("===================================================")








