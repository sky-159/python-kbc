# KON BANEGA CROREPATI

# ---WRITTEN BY ME---
'''Problems rn
1. switch the question. 2 value return karni hai. jo ki flag or boolean sa honi hai uska koi ata pata nhi
2. 50:50 to abhi use he ni kari
3. koi bhi life line bss ek baar use honi chiye. list.remove() ya list.pop() use karna hai
4. agar koi life line use hoo chuki hai to fir list alag sa banni hai. fir 1. switch the question 2. ask the expert hona chiye.
matlab wo option remove + list rearangement hona chiye.
5. Har question ka baad quit karna ka option hona chiye.
'''


def ent():
    ente = input("....")


k = 0
ret_swi_qu = 0
print("----WELCOME TO KON BANEGA CROREPATI----")
ent()
intro = '''Welcome to the hot seat of Kon Banega Crorepati!

Here, your knowledge is your wealth. You'll face a series of multiple-choice questions, each one taking you closer to the ultimate prize. 
Answer correctly, and you advance. A wrong answer, however, could end your journey. So, sharpen your mind, trust your instincts, 
and let's begin the game of knowledge and destiny!
'''
print(intro)
ent()
name = input("Enter your name: ")

life_line = '''
Hello {name}, there will 3 life lines. You can use only one life line in a question and you can use a particular life line only once. 

1. 50:50: This lifeline eliminates two incorrect options from the four given choices, leaving the contestant with only one correct and one 
incorrect option. This increases the chances of choosing the right answer to 50%.

2. Switch the Question (or Flip The Question): The current question is replaced with a new one. Any lifelines already used on the original 
question remain expended.

3. Ask the Expert (or Expert Advice): An expert (often a general knowledge specialist or a celebrity) in the studio provides their opinion
on the correct answer.

So {name}, let's start the game.'''

print(life_line.format(name=name))
ent()


def answer():
    global k
    while True:
        try:
            life()
            if (ret_swi_qu == 2) or (ret_swi_qu == 3):
                break
            a = input("Enter your answer: ")
            if a in ans:
                print("CORRECT ANSWER\nNext Question")
                k = 0
                break
            elif a not in "abcdABCD":
                print(
                    "Invalid value. \nPlease enter the answer which is 'A' or 'B' or 'C' or 'D'")
            else:
                print("WRONG ANSWER \nSorry the game is over")
                k = 1
                break
        except ValueError:
            print(
                "Invalid value. \nPlease enter the answer which is 'A' or 'B' or 'C' or 'D'")
        except Exception as e:
            print(f"Unexpected error occured {e}")


def life():
    life_list = ["50:50", "Switch the Question", "Ask the Expert"]
    while True:
        try:
            life_choice = input(
                "Want to use a life line?\nPress \"Y\" if Yes and \"N\" if No.: ")
            if (life_choice == 'Y' or life_choice == 'y' or life_choice == 'N' or life_choice == 'n'):
                break
        except ValueError:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    if life_choice in "Yy":
        print("Available life lines are: ")
        for i in life_list:
            print(life_list.index(i) + 1, i)
        while True:
            try:
                choice = input("Choose a life line (1-3): ")
                choice = int(choice)
                if choice in [1, 2, 3]:
                    break
                else:
                    print("Please choose a valid option (1-3): ")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
        if choice == 1:
            f50_50()
            # life_list.remove("50:50")
        elif choice == 2:
            switch_question()
            # life_list.remove("Switch the Question")
            return ret_swi_qu
        elif choice == 3:
            ask_expert()
            # life_list.remove("Ask the Expert")
    else:
        print("Okay, let's continue the game.")


def f50_50():
    pass


def switch_question():
    extra_ques = '''New Question:
    What is the capital city of France?
    a) Rome
    b) Berlin
    c) Paris
    d) Madrid'''
    ans = "cC"
    print(extra_ques)
    global ret_swi_qu
    while True:
        try:
            a = input("Enter your answer: ")
            if a in ans:
                print("CORRECT ANSWER")
                ret_swi_qu = 2
                break
            elif a not in "abcdABCD":
                print(
                    "Invalid value. \nPlease enter the answer which is 'A' or 'B' or 'C' or 'D'")
            else:
                print("WRONG ANSWER \nSorry the game is over")
                ret_swi_qu = 3
                break
        except ValueError:
            print(
                "Invalid value. \nPlease enter the answer which is 'A' or 'B' or 'C' or 'D'")
        except Exception as e:
            print(f"Unexpected error occured {e}")


def ask_expert():
    print("Expert's answer is...", ans[0])


while True:
    q1 = '''Question 1:
    Which planet is known as the "Red Planet"?
    a) Earth
    b) Mars
    c) Jupiter
    d) Venus'''
    ans = "Bb"
    print(q1)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 1,000")
    ent()

    q2 = '''Question 2:
    Who wrote the Indian National Anthem, "Jana Gana Mana"?
    a) Bankim Chandra Chatterjee
    b) Rabindranath Tagore
    c) Mahatma Gandhi
    d) Subhas Chandra Bose'''
    ans = "Bb"
    print(q2)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 2,000")
    ent()

    q3 = '''Question 3:
    Which of these rivers flows through the city of Varanasi?
    a) Ganga
    b) Godavari
    c) Yamuna
    d) Brahmaputra'''
    ans = "Aa"
    print(q3)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 3,000")
    ent()

    q4 = '''Question 4:
    What is the largest land animal in the world?
    a) Giraffe
    b) African Elephant
    c) Blue Whale
    d) Rhinoceros'''
    ans = "Bb"
    print(q4)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 5,000")
    ent()

    q5 = '''Question 5:
    In which year did India gain independence from British rule?
    a) 1950
    b) 1942
    c) 1947
    d) 1962'''
    ans = "Cc"
    print(q5)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 10,000")
    ent()

    q6 = '''Question 6:
    Which chemical element has the symbol 'Fe'?
    a) Fluorine
    b) Gold
    c) Iron
    d) Silver'''
    ans = "Cc"
    print(q6)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 20,000")
    ent()

    q7 = '''Question 7:
    Which social media platform is known for its short-form video content?
    a) Facebook
    b) Twitter
    c) Instagram
    d) TikTok'''
    ans = "Dd"
    print(q7)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 40,000")
    ent()

    q8 = '''Question 8:
    Which is the smallest continent in the world?
    a) Australia
    b) Europe
    c) Asia
    d) Antarctica'''
    ans = "Aa"
    print(q8)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 80,000")
    ent()

    q9 = '''Question 9:
    What is the name of the highest mountain peak in the world?
    a) K2
    b) Kangchenjunga
    c) Mount Everest
    d) Lhotse'''
    ans = "Cc"
    print(q9)
    answer()
    if k == 1:
        break
    else:
        print("Hurray! You have won Rs. 1,60,000")
    ent()

    q10 = '''Question 10:
    Which of the following is NOT an input device for a computer?
    a) Keyboard
    b) Printer
    c) Mouse
    d) Microphone'''
    ans = "Bb"
    print(q10)
    answer()
    print("Hurray! You have won Rs. 3,20,000")
    break
