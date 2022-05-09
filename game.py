def main():
    username = input("Hey! What is your name? ")
    print(f"{username}, I'm thinking of a number between 1 and 100")
    print("Try to guess my number.")
    import random
    answer = random.randint(1,100)
    guess=verifyInput()
        
    count = 1
    while guess != answer:
        if guess > answer:
            print("Your guess is too high, try again") 
            guess=verifyInput()
            count+=1
        elif guess < answer:   
            print("Your guess is too low, try again") 
            guess=verifyInput()
            count+=1
    print(f"Well done, {username}! You found my number in {count} tries!")        
    print("See you next time!")

def verifyInput():
    try:
        guess = int(input("Your guess? "))
        while guess > 100 or guess < 1:
            guess = int(input("Your guess has to be between 1 and 100.\nYour guess: "))

    except ValueError:
        guess =int (input("Your guess has to be an integer.\n Your guess? "))
        while guess > 100 or guess < 1:
            guess = int(input("Your guess has to be between 1 and 100.\nYour guess: "))

    return guess
main()