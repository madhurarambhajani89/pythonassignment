#question1
def find_max(a,b,c):

    if a > b and a>c :
      largest=a
    elif b > c and b>a:
        largest=b
    else :
        largest=c
    return largest
c=find_max(10,20,30)
print(c)

#question2
def authencticate(username,password):
    if username=="Franny123" and password=="Blueberry10":
     d= 'true'
    else :
     d="false"
    return d
#question3
from datetime import datetime

time = datetime.now()

user_input = str(input("Enter any of these choices: US, India"))


def format_time(user_input):
    if user_input == "US":
        print( time.strftime("%d,%m,%y"))
    elif user_input == "India":
        print( time.strftime("%m,%d,%y"))
    else:
        print("Wrong Input Specified.")


format_time(user_input)
#question4

from datetime import *

now = datetime.now()
print("1 week ago was it: ", str(now - timedelta(weeks=1)))
print("1 week from now is it: ", str(now + timedelta(weeks=1)))
