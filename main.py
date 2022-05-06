import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
	_ = display.insert(0, "_")
print(display)
while not end_of_game:
    #Ask use to guess letter and accept input
    user_selection = input("Guess a letter: ").lower()
    
    #Check word length and compare to user_selection by replacing blanks
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_selection:
            display[position] = letter
        #Check chosen_word if user was incorrect remove life
    if user_selection not in chosen_word:
        lives -= 1
        if lives == 0:
      #Exit while loop
            end_of_game = True
            print("You lose.")
  
  	
    print(f"{' '.join(display)}")
  
  	#Check if user has got all letters.
    if "_" not in display:
      end_of_game = True
      print("You win.")

  	
    print(stages[lives])

