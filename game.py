def main():
    score = []
    max_guess = 6
    while True:
        username = input("Hey! What is your name? ")
        print(f"{username}, I'm thinking of a number between 1 and 100")
        print("Try to guess my number.")
        import random
        answer = random.randint(1,100)
        guess=validInput()      
        count = 1
        while guess != answer:
            if guess > answer:
                print("Your guess is too high, try again")         
            elif guess < answer:   
                print("Your guess is too low, try again") 
            guess=validInput()
            count+=1
            if count == max_guess:
                print("Too many tries!")
                break
        if guess == answer:
            score.append(count)
            print(f"Well done, {username}! You found my number in {count} tries!")        
        again=input("Would you like to play again? Yes or No: ").strip().lower()
        if again =="no":
            if score == []:
                print("You've never guessed! Try again.")
            print(f"Your best score is {min(score)}")
            break


def validInput():
    valid_input=False
    while not valid_input:
        try:
            guess = int(input("Your guess? (Enter an integer between 1 and 100) "))
            if type(guess) == int and 1 <= guess <= 100:
                valid_input = True 
        except ValueError:
            continue
    return guess       
main()