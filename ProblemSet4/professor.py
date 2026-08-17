import random

def create_question_level_(level):
    if level == 1:
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)
    elif level == 2:
        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
    else:
        number1 = random.randint(100,999)
        number2 = random.randint(100,999)
    answer = number1 + number2
    question = f"{number1} + {number2} = "
    return answer, question
def main():
    count = 0
    while True:
        level_chosen = int(input("Level: "))
        if level_chosen not in [1,2,3]:
            print("Invalid level")
        else:
            while count != 10:
                answer, question = create_question_level_(level_chosen)
                while True:
                    user_answer =int(input(question))
                    if user_answer == answer:
                        print("Correct!")
                        count = count + 1
                        break
                    else:
                        print("Try again!")

main()