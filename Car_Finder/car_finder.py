import re
from pyke import knowledge_engine
from pyke import krb_traceback
import random
import long_responses as long
engine = knowledge_engine.engine(__file__)

#Message Probabilty for determine choice selection
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

# check all possable messages
def check_all_messages(message):
    global isCarSuggesting
    highest_prob_list={}
    
    def response (bot_response,list_of_words,singe_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = messagge_probability(message,list_of_words,singe_response,required_words)


    ## REGULAR RESPONSES ##
    response('Hello i am Car Finder. How can i help you!',['hello','hi','sup','hep','heyo'],singe_response=True)
    response('my name is Car Finder.',['what','is','your','name'],required_words=['your','name'])
    response('mee too.',['i','love','hate','you'],required_words=['i','you'])
    response('i am Car Finder.',['who','are','you'],required_words=['who','you'])
    response('I\'m doing fine, and you?', ['how','are','you','doing'],required_words=['how'])
    response('i love you too!',['i','love','you'],required_words=['love','you'])
    response('no problem!',['thanks'],singe_response=True)
    response('Nice to meet you!',['my','name','is'],required_words=['my','name'])
    response(long.R_EATING,['what','do','you','eat'],required_words=['you','eat'])
    response(long.R_SUGGEST,['can','you','suggest','find','me','a','car'],required_words=['car'])




    best_match = max(highest_prob_list,key=highest_prob_list.get)

    res = long.unknown() if highest_prob_list[best_match] < 1 else best_match

    if(res == long.R_SUGGEST):
        isCarSuggesting =True
    #print(highest_prob_list)
    return res

# car suggestion flag
isCarSuggesting = False
answeredQuestionIndex = 0

# suggest car based on facts
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

#answer to knowlagebase facts
def answerToFact(message,questionIndex):
    index = questionIndex-1
    for word in message:
        if(index==0):
            if word in ["electric"]:
                engine.assert_('facts','electric',[True])
            if word in ["gasoline"]:
                engine.assert_('facts','electric',[False])
        if(index==1):
            if int(word) > 10000:
                engine.assert_('facts','cheap',[False])
            else:
                engine.assert_('facts','cheap',[True])
        if(index==2):
            if word in ["4x4"]:
                engine.assert_('facts','type4x4',[True])
            if word in ["4x2"]:
                engine.assert_('facts','type4x4',[False])
        if(index==3):
            if word in ["manuel"]:
                engine.assert_('facts','manuel',[True])
            if word in ["automatic"]:
                engine.assert_('facts','manuel',[False])
        if(index==4):
            if int(word) >= 4:
                engine.assert_('facts','seat4',[True])
            if int(word) < 4:
                engine.assert_('facts','seat4',[False])
        if(index==5):
            if word in ["sedan"]:
                engine.assert_('facts','sedan',[True])
            if word in ["suv"]:
                engine.assert_('facts','sedan',[False])
        if(index==6):
            if int(word) >= 200:
                engine.assert_('facts','horsepower',[True])
            if int(word) < 200:
                engine.assert_('facts','horsepower',[False])
        if(index==7):
            if word in ["offroad"]:
                engine.assert_('facts','offroad',[True])
            if word in ["onroad"]:
                engine.assert_('facts','offroad',[False])
        
# get suggested car from knowlagebase
def get_suggested_car():
    response=""
    #engine.reset()      # Allows us to run tests multiple times.
    #engine.assert_('facts','electric',[True])
    engine.activate('rules')
    try:
        with engine.prove_goal('rules.what_to_buy($car)') as gen: 
            for vars, plan in gen:
                response = ("You should buy a %s" % (vars['car']))
                #print(response)

    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        # This converts stack frames of generated python functions back to the .krb file.
    
    if(response==""):
        response=long.R_NOSUGGEST

    return response

# get response of chatbot based on suggestion flag
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

# send button func
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
base.geometry("700x500")
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
scrollbar.place(x=670,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=670)
EntryBox.place(x=6, y=401, height=90, width=550)
SendButton.place(x=560, y=401, height=90)
base.mainloop()