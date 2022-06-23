import random

R_EATING = "I dont line eating anything because im just a bot duuhh!"
R_SUGGEST = "Of course! can i ask you some questions ?"
R_FIND    = "Of course! can i ask you some questions ?"

R_NOSUGGEST = "Sorry i did not find any car suitable for you."



def unknown():
    response = [
    "Could you please re-phrease that?",
    "...",
    "Sounds about right",
    "what does that mean?"
    ]
    return response[random.randint(0,len(response)-1)]


car_questions = [
    "Do you like electric powered cars or gasoline powered cars ?",
    "How much do you want to spend ?",
    "4x4 or 4x2 ?",
    "Manual or automatic transmission ?",
    "How much seat do you want ?",
    "Suv or Sedan ?",
    "How much horse power do you need ?",
    "Do use your car onroad or offroad ?"
    ]