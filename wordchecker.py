#checking for words from a given file 
file = open("test-subject.txt", "r+")
count = 0 
word = input("enter work to check here: ")
for i in file:
     if any(file for c in word):
        count += 1
print(count)