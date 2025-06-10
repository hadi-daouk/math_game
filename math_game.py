import random
import sys
import time

print('Welcome to Math Game, the rules of this game are simple.')
print('You will do as many basic math operations as you can with 5 seconds for each equation.')
print('As you solve more problems the level will increase, making the equations harder')

def levels(typeOfEquation: str, numOfEquations: int) -> None:
    correct_answers = 0
    wrong_answers = 0


    for i in range(numOfEquations):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = 0
        match typeOfEquation:
            case '+':
                num3 = num1 + num2
            case '-':
                num3 = num1 - num2
            case '*':
                num3 = num1 * num2
            case '/':
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
                num3 = round(num1 / num2,2)
            case '%':
                num3 = num1 % num2
        # Check for input error
        while True:
            try:
                user_answer = float(input(f'Answer of: {num1} {typeOfEquation} {num2}'))
                break
            except ValueError:
                print('Please enter a number.')

        if user_answer != num3:
            print('Wrong answer.❌')
            wrong_answers += 1
        else:
            print('Correct!✅')
            correct_answers += 1


    print(f'You got {correct_answers} answers correct and {wrong_answers} answers wrong')


def main() -> None:
    correct_answers = 0
    wrong_answers = 0

    print('-----------------------')
    print('Level 1: Addition')
    levels('+',5)

    print('-----------------------')
    print('Level 2: Subtraction')
    levels('-',5)

    print('-----------------------')
    print('Level 3: Multiplication')
    levels('*',5)

    print('-----------------------')
    print('Level 4: Division')
    levels('/',5)

    print('-----------------------')
    print('Level 5: Modulo')
    levels('%',5)

    time.sleep(1)

    print('Thank you for playing! I hope you enjoyed this little math game!')
    sys.exit(0)

if __name__ == '__main__':
    main()


# Potential updates that can be made:
# Add a limited time for user to answer question
# Add division questions + modulus ✅
# Add a history of all the questions asked and show which are correct and which are wrong

# BIG UPDATES
# Make a simple website for the game
# Make users sign in/log in
# Track users logs, how many games played, how many won, lost, average time took for questions to be answered
