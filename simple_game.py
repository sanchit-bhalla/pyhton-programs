import random

def Computer_code():
    """
    it generates a list of 3 digits
    """
    digits=[str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def generate_clues(comp_code,userguess):
    '''
     Close: You've guessed a correct digit but in the wrong position
     Match: You've guessed a correct digit in the correct position
     Nope: You haven't guess any of the digits correctly
     '''
    if comp_code == userguess:
         return "CODE CRACKED"

    clues = []

    for index,num in enumerate(userguess):
        if num == comp_code[index]:
            clues.append("Match")
        elif num in comp_code:
            clues.append("Close")
    if clues == []:
        clues.append("Nope")
    return clues


secret_code=Computer_code()
print("Welcome to code breaker!")
clue_report=[]

while clue_report != "CODE CRACKED":
    guess = list(input("Enter your guess : "))
    clue_report = generate_clues(secret_code,guess)
    for clue in clue_report:
        print(clue)
        
