#preset rules of the game code
word = "lopsy"
right = []
wrong = []
counter = 0 
def build_gallow_ascii_art():
    file = open("gallow_art.txt","r+")
    art = file.read().split("***")
    return art

gallow = build_gallow_ascii_art
#actaul game code
while counter < 5:
    print(gallow[0])
    print("this word has a length of " )
    print(len(word))

    userinput = input("guess: ")
    if userinput == "lopsy":
        print("yes")
        print("you win")
    elif word.count(userinput) == True:
        right.append(userinput)
        print(userinput + " partly")
        print(right)
    else:
        print("no")
        wrong.append(userinput)
        print(wrong)
        counter += 1 

if counter < 6:
    print("you lose")

# storing 
    #if __name__ == "__main__":
    #main()