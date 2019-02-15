import string

def character_word_count(book):
	mydict=dict()
	for line in book.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		mydict[myword]=mydict.get(myword,0)+1
	print(mydict)

fp1=open('Book1.txt')
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()

print("\n======================================Book1 Dictionery================================\n") 
character_word_count(file1)
print("\n======================================Book2 Dictionery================================\n") 
character_word_count(file2)
print("\n======================================Book3 Dictionery================================\n") 
character_word_count(file3)

