import random


def function_integer_choice(min, max):
    """
    Random integer.
    Parameters:
    min (int): The minimum value (inclusive) of the range.
    max (int): The maximum value (inclusive) of the range.
    Returns:
    int: A random integer within the range [min, max].
    """
    return random.randint(min, max)


def function_operation_choice():
    """
    Random operation choice
    Parameters:
    None
    Return : 
    str: A random operator choice from ['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def function_calculation(n1, n2, o):
    """
    Calculation base on two number and operator
    Parameters:
    n1(int): The first number 
    n2(int): The second number
    o(str): The operator
    Returns:
    str:A string of the operation
    int:result of the operation
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    A math game provide question for user answer  
    Parameters:
    None
    Returns:
    None
    """
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_integer_choice(1, 10); n2 = function_integer_choice(1, 5.5); o = function_operation_choice()

        PROBLEM, ANSWER = function_calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except:
            print("Please makesure your answer only number")
            continue
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
