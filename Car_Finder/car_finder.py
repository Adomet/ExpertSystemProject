import re
from pyke import knowledge_engine
from pyke import krb_traceback
import random
import long_responses as long
engine = knowledge_engine.engine(__file__)

def random_greet():
    greet_list = list()
    greet_list.append("I am Car_Finder, How can i help you?")
    return greet_list[random.randint(0,len(greet_list)-1)]

def messagge_probability(user_message,recongised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_words=True

    for word in user_message:
        if word in recongised_words:
            message_certainty +=1
    
    percentage = float(message_certainty/float(len(recongised_words)))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0




def check_all_messages(message):
    global isCarSuggesting
    highest_prob_list={}
    
    def response (bot_response,list_of_words,singe_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = messagge_probability(message,list_of_words,singe_response,required_words)


    ## REGULAR RESPONSES ##
    response('Hello i am Car_Finder. How can i help you!',['hello','hi','sup','hep','heyo'],singe_response=True)
    response('my name is Car_Finder.',['what','is','your','name'],required_words=['your','name'])
    response('mee too.',['i','love','hate','you'],required_words=['i','you'])
    response('i am Car_Finder.',['who','are','you'],required_words=['who','you'])
    response('I\'m doing fine, and you?', ['how','are','you','doing'],required_words=['how'])
    response('i love you too!',['i','love','you'],required_words=['love','you'])
    response('Nice to meet you!',['my','name','is'],required_words=['my','name'])
    response(long.R_EATING,['what','do','you','eat'],required_words=['you','eat'])
    response(long.R_SUGGEST,['can','you','suggest','me','a','car'],required_words=['suggest','car'])


    best_match = max(highest_prob_list,key=highest_prob_list.get)

    res = long.unknown() if highest_prob_list[best_match] < 1 else best_match

    if(res == long.R_SUGGEST):
        isCarSuggesting =True
    #print(highest_prob_list)
    return res


isCarSuggesting = False
answeredQuestionIndex = 0
def resForACarSuggestion():
    global isCarSuggesting
    global answeredQuestionIndex 
    isCarSuggesting = True
    answeredQuestionIndex = 0
    response = ["Of course! I im just going to ask some quesitons about what type of car you want."]
    return response[0]

def suggest_car(message):
    global answeredQuestionIndex
    global isCarSuggesting

    answerToFact(message,answeredQuestionIndex)

    if(answeredQuestionIndex == (len(long.car_questions))):
        res = get_suggested_car()
        answeredQuestionIndex=0
        isCarSuggesting = False
        engine.reset()
    else:
        res = long.car_questions[answeredQuestionIndex]
        answeredQuestionIndex +=1
    return res

def answerToFact(message,questionIndex):
    index = questionIndex-1
    for word in message:
        if(index==0):
            if word == "electric":
                engine.assert_('facts','electric',[True])
            if word == "gasoline":
                engine.assert_('facts','electric',[False])
        if(index==1):
            if word == "4x4":
                engine.assert_('facts','type4x4',[True])
            if word == "4x2":
                engine.assert_('facts','type4x4',[False])
        if(index==2):
            if int(word) > 10000:
                engine.assert_('facts','cheap',[False])
            else:
                engine.assert_('facts','cheap',[True])

def get_suggested_car():
    response=""
    #engine.reset()      # Allows us to run tests multiple times.
    #engine.assert_('facts','electric',[True])
    engine.activate('rules')
    try:
        with engine.prove_goal('rules.what_to_buy($car)') as gen: 
            for vars, plan in gen:
                response = ("You should buy: %s" % (vars['car']))
                print(response)

    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        # This converts stack frames of generated python functions back to the .krb file.
    
    if(response==""):
        response=long.R_NOSUGGEST

    return response


def chatbot_response(text):
    split_message = re.split(r'\s+|[,;?!.-]\s',text.lower())
    response =''
    if(isCarSuggesting):
        response = suggest_car(split_message)
    else:
        response = check_all_messages(split_message)
    return response


#Creating GUI with tkinter
import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = chatbot_response(msg)
        ChatLog.insert(END, "Car_Finder: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Car_Finder")
base.geometry("600x500")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font=("Verdana",10,'bold'))
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
#Create Button to send message
SendButton = Button(base, font=("Verdana",11,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#ff2800", activebackground="#ff2800",fg='#ffffff',
                    command= send )
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font=("Verdana",10,'bold'))
#EntryBox.bind("<Return>", send)
#Place all components on the screen
scrollbar.place(x=576,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=570)
EntryBox.place(x=6, y=401, height=90, width=440)
SendButton.place(x=450, y=401, height=90)
base.mainloop()