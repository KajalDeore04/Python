#Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play


questions = [
    "What is the capital of India?",
    "What is the currency of Japan?",
    "Who is the current President of the United States?",
    "What is the highest mountain in the world?",
    "Which of the following is a prime number? a) 4 b) 9 c) 11 d) 15"
]

answers = [
    "New Delhi",
    "Yen",
    "Joe Biden",
    "Mount Everest",
    "c"
]



def play_game():
    count = 0
    for i in range(len(questions)):
        print("Question no.{} : {}".format(i+1,questions[i]))
        answer = input("Enter Your Answer\n")
        if answer.lower() == answers[i].lower():
            print("Correct!")
            count = count + 1
            print("You won Rs.",count * 1000)
            print("----------------------------------------------------------------------------------")
        else:
            print("Incorrect!")
            exit()


if input("Do you want to play? ").lower() == "yes":
    play_game()

else:
    print("Loser..............")