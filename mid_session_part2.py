###Question1

# class_file = open("mid_review1.txt", "r").read()
# # print class_file

# letter_count = {}
##setting x equal to ascii of 'a' == 97 'z' == 122
# x = ord('a')
# y = ord('z')
# for letter in class_file:
# 	letter = letter.lower()
# 	if ord(letter)>=x and ord(letter)<=y:
# 		if letter not in letter_count.keys():
# 			letter_count[letter] = 0
# 		letter_count[letter] += 1 

# print letter_count

###Question2

second_file = open("mid_session_part2.txt", "r").read()
import string

word_count = {}
list_of_words = second_file.split(" ")

for word in list_of_words:
	word = word.lower()
	##using import string found this to remove punctuation on Stack
	word = word.translate(string.maketrans("",""), string.punctuation)
	##if word is not in dictionary word_count then add it
	if word not in word_count.keys():
		word_count[word] = 0
	word_count[word] += 1

print word_count



