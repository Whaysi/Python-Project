import random

q1 = {"question":"What color are Zebras?","trueanswer": "White with black stripes","false1":"Black with white stripes","false2":"Black with red stripes"}
q2 = {"question":"Where was the old campus of Sehir University ?","trueanswer":"Altunizade","false1":"Levent","false2":"Maltepe"}
q3 = {"question":"What is the capital of Turkey","trueanswer":"Ankara","false1":"Istanbul","false2":"Izmir"}
questions = [q1,q2,q3]

userinfo = {"5577": ["Abbas",5.4] , "5466": ["Betul",3.2] , "5551":["Omer",6.4] }

def_prize = 1000

def questionsasker():
    while True:
        if questions.__len__()>0:
            currentquestion = random.choice(questions)
            for i in currentquestion:
                print "Q" + " " + (currentquestion["question"]) + "\n"
                print "ans 1." + (currentquestion["trueanswer"])
                print "ans 2." + (currentquestion["false1"])
                print "ans 3." + (currentquestion["false2"]) + "\n"
                correntans = raw_input("Please select your answer")

                if correntans == currentquestion["trueanswer"]:
                    print "Your answers is " + str(correntans)
                    print "Correct"
                    questions.remove(currentquestion)
                    print "length of list: " , questions.__len__()
                questionsasker()

def adminInterface():
    print "Welcome to Sehir HADI admin section, please choose one of following options:"
    print "1 - Set prize for next competition"
    print "2 - Display questions for the next competition"
    print "3 - Add new question to the next competition"
    print "4 - Delete a question from the next competition"
    print "5 - See User's data"
    print "6 - Log out"
    while True:
        UserSelect = raw_input()
        if UserSelect == "1":
            new_prize = raw_input("Please type the total prize of the next competition:")
            print "Setting new prize..."
            def_prize = new_prize
            print "Going back to the admin menu..."
            adminInterface()
        if UserSelect == "2":
            num = 1
            for question in questions:
                print "Q" + str(num) + " " + (question["question"]) + "\n"
                print (question["trueanswer"]) + " :True"
                print (question["false1"]) + " :False"
                print (question["false2"]) + " :False" + "\n"
                num += 1
            adminInterface()
        if UserSelect == "3":
            new_question = raw_input("Please type the question:")
            new_question_correctAns = raw_input("Please type a Correct answer")
            new_question_incorrectAns1 = raw_input("Please type an incorrect answer")
            new_question_incorrectAns2 =raw_input("Please type an incorrect answer")

            q4 = {"question":new_question, "trueanswer":new_question_correctAns,"false1":new_question_incorrectAns1,"false2":new_question_incorrectAns2}
            questions.append(q4)
            print "Adding to the question database..."
            print "Done..."
            adminInterface()
        if UserSelect == "4":
            num2 = 1
            for question in questions:
                print "Q" + str(num2) + " " + (question["question"]) + "\n"
                num2 += 1
            while True:
                delete_question = input("Please type the number of the question to be deleted")
                del questions[delete_question-1]
                print "Q" + str(delete_question) + " succesfully deleted!"
                print "Going back to the admin menu..."
                adminInterface()
        if UserSelect == "5":
            for a in userinfo:
                print str(userinfo[a][0])+ "," + " Balance:" + str(userinfo[a][1]) + ", Phone number: " + str(a)
            print "\n" "Going back to the admin menu..." + "\n"
            adminInterface()
        if UserSelect == "6":
            Hadililili()

def Hadililili():
    print "--- Welcome to Sehir HADI :) ---"
    while True:
        print "Please type your phone number for sign in"
        UserPhoneNumber = raw_input()
        if  UserPhoneNumber == "**":
            adminInterface()
        if  len(UserPhoneNumber)>4 or len(UserPhoneNumber)<4:
            print "Your Phone Number Should be 4 digit"
        if UserPhoneNumber in userinfo:
            username = userinfo[UserPhoneNumber]
            print "Checkking " + str(UserPhoneNumber) + "..."
            print "Welcome" + str(username)
            print "Competition will start soon.. be ready :)"
            print "******************* Total Players:" + str(len(userinfo))
            break
    questionsasker()


Hadililili()