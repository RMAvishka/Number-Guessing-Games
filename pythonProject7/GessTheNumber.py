import random
def guess(x1,x2):
    random_Number = random.randint(x1,x2)
    guess = 0
    while guess != random_Number:
        guess = int(input(f"Enter number between {x1} - {x2} = "))
        if guess > x2:
            print("Please Enter A Number In The Range! ")
        elif guess < x1:
            print("Please Enter A Number In The Range! ")
        elif guess > random_Number :
            print(" Try a Another Number , Your Number is too High!" )
        elif guess < random_Number:
            print("Try a Another Number, Your Number is too Low!")
    print("Wooow!!! Amazing You guessed it correctly!!!")
guess(1,100)



