# time_tick_quiz.py/home/anr7/Documents/TimeTickQuiz/src

import requests
import html
import random
import threading
import time
import sys

CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"
TIME_LIMIT = 15  # seconds per question

time_up = threading.Event()


# ------------------ api functionss ------------------

def fetch_categories():
    """
    fetches trivia categories from the API.
    """
    categories = requests.get(CATEGORY_URL).json()
    return categories["trivia_categories"]
    pass

def fetch_questions(params, amount=10):
    """
    fetches the questions based on given filters.
    """
    params["amount"]=amount
    questions = requests.get(QUESTION_URL, params).json()
    return questions["results"]
    pass

# ------------------ user input selection ------------------

def select_category():
    """
    prompts user to select a category from the list.
    """
    categories=fetch_categories()

    print("Select Category of questions ")
    print("----------------------------------------------")


    for category in categories:
        print(f'{category["name"]}({category["id"]})')
    print("----------------------------------------------")
    selected = input()

    for category in categories:
        if selected == category["name"]:
            selected = category["id"]

    
    return selected
    pass

def select_difficulty():
    """
    prompst user to select question difficulty.
    """
    print("----------------------------------------------")
    print("Select difficulty from easy, medium and hard")
    print("----------------------------------------------")
    selected = input()

    if (selected.lower()=="easy" or selected.lower()=="e"):
        selected = "easy"
    
    elif (selected.lower()=="medium" or selected.lower()=="m"):
        selected = "medium"
    
    elif (selected.lower()=="hard" or selected.lower()=="h"):
        selected = "hard"
    return selected
    
    pass

def select_question_type():
    """
    prompts the user to select type of questions (multiple/boolean).
    """
    print("----------------------------------------------")
    print("Select difficulty from multiple and boolean")
    print("----------------------------------------------")
    selected = input()


    if (selected.lower()=="multiple" or selected.lower()=="m"):
        selected = "multiple"
    
    elif (selected.lower()=="boolean" or selected.lower()=="b"):
        selected = "boolean"

    return selected
    
    pass

# ------------------ quiz logicc ------------------

def ask_question(questions):
    """
    presents a question to the user with a countdown timer.
    """
    qn = 1
    correct = 0
    for question in questions:

        if question["correct_answer"] in ["True", "False"]:
            options = ["True", "False"]
        else:
            options = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(options)
        clean_question = html.unescape(question["question"])

        print(qn, end = ")")
        print(clean_question)
        print(">>> ", end="")
        print(" , ".join(html.unescape(options)))

        time_up.clear()
        answer = [None]

        # Timer function

        def timer(timel=TIME_LIMIT):
            for i in range(timel, 0, -1):
                if time_up.is_set() : return;
                if i<10:
                    i="0"+f"{i}" # To prevent /r goofiness
                sys.stdout.write(f"\r$~Time left: {i}s ")
                sys.stdout.flush()
                time.sleep(1)
            time_up.set()
        # Input function 

        def getInput():
            while not time_up.is_set():
                try:
                    inp = int(input(""))
                    if 1 <= inp <= len(options):
                        if time_up.is_set():
                            continue
                        answer[0] = inp
                        time_up.set()
                        break  # valid input
                    else:
                        if time_up.is_set():
                            continue
                        print(f"Invalid choice! Enter a number between 1 and {len(options)}.")
                except ValueError:
                    if time_up.is_set():
                        continue
                    print("Invalid input! Please enter a number.")
    
        t_tim = threading.Thread(target=timer)
        t_inp = threading.Thread(target=getInput)

        t_tim.start()
        t_inp.start()

        t_inp.join()  # wait for input
        t_tim.join()  # wait for timer to cleanly exit
        sys.stdout.write("\r" + " " * 20 + "\r")


        
        if answer[0] is None:
            
            print("Timed out!")
        elif options[answer[0]-1] == question["correct_answer"]:
            print("Correct")
            correct+=1
        else:
            print("Wrong")

        print("")
        qn+=1

    return correct

def select_quiz_options():
    """
    gathers all the quiz options and fetch questions accordingly.
    """
    params={}
    params["category"] = select_category()
    params["difficulty"] = select_difficulty()
    params["type"] = select_question_type()
    return params


# ------------------ main fucntion ------------------

def main():
    """
    Entry point for the TimeTickQuiz game.
    """
    print("----------Welcome to the TimeTickQuiz fam---------")

    flag = "yes"

    while(flag.lower() in ["y", "yes"]):
        questions = fetch_questions(select_quiz_options())
        print("------------------------------------------\n")
        if not questions:
            print("Check your choices and try again")
            sys.exit(1)
        
        correct = ask_question(questions)
        print(f"\nYour score is {correct}")
        flag = input("----------Do you want to play again------\n")
        

    sys.exit(0)
if __name__ == "__main__":
    main()
