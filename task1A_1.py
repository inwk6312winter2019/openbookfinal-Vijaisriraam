import string

def unique_words(book):
	mydict=dict()
	utuple=[]
	for line in book.split():
		word=line.strip(string.punctuation)
		if word not in mydict:
			mydict[word]=1
		else:
			mydict[word]+=1
#	print(mydict)
	for line in book.split():
		words=line.strip()
		if words not in utuple:
			utuple.append(words)
	print(tuple(utuple))

""" This is to check if any word is repeated more than once in the tuple
	count=0
	for char in utuple:
		if(char=='eBooks'):
			count+=1
	print('repeated times:',count)"""

fp1=open('Book1.txt')
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()

print("\n ============Unique words in Book1:================\n")
unique_words(file1)
print("\n ============Unique words in Book2:================\n")
unique_words(file2)
print("\n ============Unique words in Book3:================\n")
unique_words(file3)

