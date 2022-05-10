def main():
    score = []
    max_guess = 6
    while True:
        username = input("Hey! What is your name? ")
        print(f"{username}, I'm thinking of a number. Try to guess my number.")
        import random
        range = input("Would you like to customize the range?(Yes/No) ").strip().lower()
        if range == 'yes':
            user_range=valid_range()
            start=user_range[0]
            end=user_range[1]            
        else:
            start=1
            end=100
        answer = random.randint(start, end)
        guess = validInput()
        count = 1
        while guess != answer:
            if count == max_guess:
                print("Too many tries!")
                break
            if guess > answer:
                print("Your guess is too high, try again")
            elif guess < answer:
                print("Your guess is too low, try again")
            guess = validInput(start,end)
            count += 1
            
        if guess == answer:
            score.append(count)
            print(f"Well done, {username}! You found my number in {count} tries!")
        again = input(
            "Would you like to play again? Yes or No: ").strip().lower()
        if again == "no":
            if score == []:
                print("You've never guessed! Try again.")
            else: 
                print(f"Your best score is {min(score)}")
            break

def validInput(start=1, end=100):
    valid_input = False
    while not valid_input:
        try:
            guess = int(
                input(f"Your guess? (Enter an integer between {start} and {end}) "))
            if type(guess) == int and start <= guess <= end:
                valid_input = True
        except ValueError:
            continue
    return guess

def valid_range():
    while True:
        try:
            start = int(input("What is your starting point? (Integers only) "))
        except ValueError:
            continue
        if type(start)==int:
            break
    while True:
        try:
            end = int(input("What is your ending point? (Integers only) "))
        except ValueError:
            continue
        if type(end)==int:
            break        
    return [start,end]

main()
