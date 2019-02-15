import string

def starts_with_vow(book):
	count=0
	book_list=[]
	vow=('a','e','i','o','u')
	for line in book.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
#		if(myword[0]=='a' or myword[0]=='e' or myword[0]=='i' or myword[0]=='o' or myword[0]=='u'):
#                        count+=1
		book_list.append(myword)
	for elem in book_list:
		if (book_list[elem][0]=='a' or book_list[elem][0]=='e'or book_list[elem][0]=='i'or book_list[elem][0]=='o' or book_list[elem][0]=='u'):
			count+=1
#		print(book_list)
	print('The total no of words in the book, starting with vowels is:',count)

fp1=open('Book1.txt')
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()

print("\n=========Book1 word list count============\n") 
starts_with_vow(file1)
print("\n=========Book2 word list count============\n") 
starts_with_vow(file2)
print("\n=========Book3 word list count============\n") 
starts_with_vow(file3)

