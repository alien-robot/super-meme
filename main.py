#greetings
print("hello user")
user = input("whats your name? ")
mood = input("how are you? ")
if mood == "good" or "fine":
    print("im thriled to hear that! ")
    print("keep it up! ")
if mood == "bad":
    print ("im sorry to hear that, i hope your day gets better ")
    print ("I believe that everyone has good days and bad days, but you can't let the bad times beat you down ")
name = input("say, what should my name be? ")
game = input("how about we play a game? ")
if game == "okay" or "sure":
 game_chose = input("what game would you like to play? guess my number or hangman?")
 if game_chose == "hangman":
    def get_secret_word():
        file = open("word_list.txt", "r+")
    word_bank = file.read().split("\n")
    index = random.randint(0, len(word_bank) - 1)

 def build_gallow_ascii_art():
    file = open("gallow_art.txt","r+")
    art = file.read().split("***")
    return art
