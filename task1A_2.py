import string

def count_the_article(book):
	count=0
	book_list=[]
	for line in book.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		book_list.append(myword)
#		print(book_list)
		count=count+1
	print('The total no of words in the word_list is:',count)

fp1=open('Book1.txt')
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()

print("\n=========Book1 word list count============\n") 
count_the_article(file1)
print("\n=========Book2 word list count============\n") 
count_the_article(file2)
print("\n=========Book3 word list count============\n") 
count_the_article(file3)

