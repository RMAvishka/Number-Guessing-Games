import random

def guessToComputer(x1,x2):
    low = x1
    high = x2
    feedback = " "
    while feedback != "c":

        guess = random.randint(low,high)
        feedback = input(f"is Your Number is  {guess}  Am I Correct(C)? OR it's Higher(H)than {guess} OR it's lower(L) than {guess}? = ")
        if feedback == "h":
            low = guess + 1
        elif feedback == "l":
            high = guess - 1

    print("Woooow! U guess it correctly!!!")

guessToComputer(1,10)

