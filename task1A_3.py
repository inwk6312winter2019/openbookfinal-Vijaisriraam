import string

def sorted_words(book):
	count=0
	mydict=dict()
	book_list=[]
	for line in book.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		book_list.append(myword)
#		print(book_list)
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1
	sort_list=[]

	for char in mydict:   #this returns sorted words in a list
		sort_list.append(char)
	sort_list.sort(reverse=True)
	print(sort_list)

"""To Return the sort list as a tuple"""
"""	for key,value in mydict.items():
		sort_list.append((value,key))
	sort_list.sort(reverse=True)
	print(sort_list)"""

fp1=open('Book1.txt')
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()

print("\n===============Book1 sorted word list====================\n") 
sorted_words(file1)
print("\n===============Book2 sorted word list====================\n") 
sorted_words(file2)
print("\n===============Book3 sorted word list====================\n") 
sorted_words(file3)

