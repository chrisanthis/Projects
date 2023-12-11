import random, sys

print(sys.version)


words = ['crier', 'accelerates', 'kingsport', 'yunnan', 'chitika', 'tetanus', 'antibiotic', 'weed', 'anticipating', 'shirtless', 'snell', 'likewise', 'zooplankton', 
         'cheap', 'respiratory', 'quickcam', 'sauk', 'augmentation', 'intensify', 'concord', 'rails', 'absorb', 'important', 'tapas', 'chandeliers', 'role', 'coldest']

def selectWord(words):
    return random.choice(words)

print(selectWord(words))
remaining_attemps = 6
selected_letters = ''

def print_secretWord():
    print(' _ '*len(secretWord))

secretWord = selectWord(words)
print_secretWord()   

# def guess_letter():
#     user_guess = input('Choose a letter:')
#     if user_guess.isalpha() and len(user_guess)== 1:
#         selected_letters = selected_letters+user_guess
#     else:
#         print('Only single letters allowed')
#         return user_guess.lower()   
