"""
ORIGINALLY MADE FOR
COTW-8: Math Quiz Master by AI STUDENT COMMUNITY



## Math Quiz Master
"""

# [imports] Import Important Stuff
import time
import random
from pyfiglet import Figlet
from termcolor import colored , cprint

# [config] Config Figlet Fonts (style)

slant = Figlet(font="slant")
standard=Figlet(font="standard")

# [config] Hints

global answ_keys
answ_keys=3

# [func] Get number of hints available (data) (style)

def get_hints():
    return answ_keys

# [func] Update number of hints available (data) (style)

def update_hints(num):
    global answ_keys
    answ_keys =num

# [func] Termcolor Config for Titles  (style)
def title_p(text):
    colour="cyan"
    return cprint(standard.renderText(text),color=colour)

# [func] Termcolor Config for Printing Problems  (style)

def prob_p(text):
    colour="light_green"
    try:
        return colored(text,color=colour)
    except:
        return text

# [func] Termcolor Config for Positive/Negative Messages  (style)

def solmsg(type:bool,text):
    if type:
        colour="green"
    else:
        colour="light_red"     
    try:
        return colored(text,color=colour)
    except:
        return text
    
# [config] Config Level High Scores (data)

highscores=[{"level":"1","hi":0},{"level":"2","hi":0},{"level":"3","hi":0},{"level":"Overall","hi":0}]

# [func] load high score , level or overall (data) (backend)

def load_high_score(level=None):
   # print(level)
    if level:
        for x in highscores:
            if x["level"]==str(level):
               # print(x)
                #print(x["hi"])
                return x["hi"]
    else:
        return highscores[3]["hi"]
    
# [func] save high score , level or overall (data) (backend)

def save_high_score(high_score,level=None):
    if not level:
        level="Overall"
    for x in highscores:
        if x["level"]==str(level):
            x["hi"]=high_score

# [func] Generate Problems (backend)

def generate_problem(level):
    '''Generates a random arithmetic problem'''

    if level == 1:
        # [!] Difficulty - Low - Only Addition/Subtraction - 3 numbers upto 10,20,30 respectively
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 30)
        operator = random.choice(['+','-'])
        operator_second = random.choice(['+','-'])
        problem = f'{num1} {operator} {num2} {operator_second} {num3}'
    elif level == 2:
        # [!] Difficulty - Med - Only Addition/Subtraction/Multiplication(only till first two numbers) - 2 or 3 numbers upto 20,20,15* respectively
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        probability=random.randint(1,100)
        if probability>30:
             num3=random.randint(1,15)
             operator = random.choice(['+','-','*'])
             operator2=random.choice(['+','-'])
             problem = f'{num1} {operator} {num2} {operator2} {num3} '
        else:
             operator = random.choice(['+','-','*']) 
             problem = f'{num1} {operator} {num2}' 
    elif level == 3:
        # [!] Difficulty - High - Only Addition/Subtraction/Multiplication/Division - 2 digits 
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 40)
        operator = random.choice(['+','-','*', '/'])
        problem = f'{num1} {operator} {num2}'
    answer = round(eval(problem))
    # return the problem and the answer as a tuple
    return problem, answer
# [func] hide passwords in room (style) (backend)
def hide_problems(problems):
    '''Hides arithmetic problems in various places in the room'''
    # Generate random locations for the problems
    #print(len(problems))
    places=["under the Table","under the Bed","behind the photoframe","below the shoes","in the laundry","in the lawns","in the store","along the dusty files"]
    locations = random.sample(places, len(problems))
    # Print the problems in their corresponding locations
    for i, problem in enumerate(problems):
        # print the problem number and its location
        print(f"Problem {i+1} is hidden {prob_p(locations[i])} .")
incorrect_answers=[]
# [func] solve answers  (backend)
def solve_problem(problem, answer, keys):
    '''Prompts the user to solve the arithmetic problem and returns True if the answer is correct'''
    # prompt the user to solve the problem
    user_answer = input(f"Solve the problem (Enter hint to Use your hint ({keys} left)): {prob_p(problem)} = ")
    if user_answer.lower()=="hint":
        if keys==0:
            print("You dont have any key ")
            user_answer = input(f"Solve the problem: {prob_p(problem)} = ")
        else:
            print(f"Using key \nCorrect answer is {answer}")
            user_answer=answer
            keys=keys-1
            update_hints(keys)
            
    # check if the user's answer is correct
    if float(user_answer) == answer:
        cprint(standard.renderText("Correct"),color="green")
        #print(solmsg(True,"[+] Correct Answer"))
        return True
    else:
        print(solmsg(False,"[-] Incorrect Answer"))
        dict={"prob":problem,"answer":answer,"attempt":float(user_answer)}
        incorrect_answers.append(dict)
        return False
# [config] Config Level Weights (data)
level_weights = [1, 2, 3]
# [config] Set the duration for each level
level_durations = [30, 20, 10]
# [config] Config Number of Questions
num_questions=7
# [func] main function to call quiz (main)
def quiz():
    title_p(text="Welcome to Maths Escape")
    print("Directions\n For answers in decimal , round off to nearest tens or ones as applicable. \n\t Eg- 13/29 = 0\nTime Limits\n\n\t Level 1\t 30 seconds\n\tLevel 2\t 20 Seconds\n\tLevel 3\t 10 Seconds")

    high_score=load_high_score()
    print(solmsg(True,f"Current Overall High Score "))

    print(solmsg(False,slant.renderText(str(high_score))))
    # Set the initial score to 0
    total_score = 0
    total_can_be_earned=0
    # Loop over the three levels
    for level in range(1, 4):
        title_p(f"Level {level}")
        hi_score=load_high_score(level=level)
        print(solmsg(text=f"Current High Score {hi_score}",type=False))
        
        # Prompt the user to continue to the next level
        while True:
            choice = input("Do you wish to continue? (Yes to continue) ")
            if choice.lower() == "yes":
                # Start the timer for this level
                start_time = time.time()
                break
        
        # Generate the problems for this level
        problems = [generate_problem(level) for i in range(num_questions)]
        
        # Hide the problems in the room
        hide_problems(problems)
        
        # Initialize the score for this level to 0
        level_score = 0
        correct=0
        can_be_earned=0
        # Loop over the problems and prompt the user to solve them
        for i, problem in enumerate(problems):
            # Check if time is up
            if time.time() - start_time > level_durations[level - 1]:
                print("Time's up! You exceeded the time limit.")
                break
            
            print(f"Problem {i+1} ")
            ans_keys=get_hints()
            # Prompt the user to solve the problem
            is_correct = solve_problem(problem[0], problem[1], ans_keys)
            time_left = level_durations[level - 1] - (time.time() - start_time)
            # Update the level score
            if is_correct:
                correct+=1
                level_score += level_weights[level - 1]
            
            # Print the time left after each problem is solved
            print(f"Time left: {time_left:.2f} seconds")
        
        # Calculate the time taken for this level
        time_taken = time.time() - start_time

        for x in incorrect_answers:
            prob=x["prob"]
            ans=x["answer"]
            attempt=x["attempt"]
            print(f" ({prob}) [Your Answer] : {attempt} [Correct Answer] : {ans}")
        
        if correct == num_questions:
            print(slant.renderText(f"Perfect Score {level}"))
            ans_keys=get_hints()
            ans_keys+=1
            print(solmsg(True,"Awarded One Key..."))
        # Calculate the level score and add it to the total score
        
        total_score += level_score
        
        print(f"You took {time_taken:.2f} seconds to answer the question(s).")
        for x in  range(num_questions):
            can_be_earned+=  level_weights[level - 1]
        total_can_be_earned+=can_be_earned
        print(f"Your score for this level is {level_score} / {can_be_earned}.")
        incorrect_answers=[]
        hi_score=load_high_score(level)
        print(f"Previous High Score {hi_score}")
        if level_score>hi_score:
            print("You set a new high score !")
            save_high_score(high_score=level_score,level=level)
        
    print(f"Your total score is {total_score} / {total_can_be_earned}.")

# [start] Start the quiz
quiz()