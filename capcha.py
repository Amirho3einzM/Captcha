import random
import time

max_value=9
min_value=1
total_ask=5
oppertion=["+","-","*"]
def qusetion():
    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    oppertions=random.choice(oppertion)
    exam=str(left)+" "+oppertions+" "+str(right)
    answer=eval(exam)
    return exam,answer
input("press enter to start!\n")
start_time=time.time()
print("---------------------------------")

for i in range(total_ask):
    exam,answer=qusetion()
    while True:
        answer_user=input("qusetion # {1}: {0}  :".format(exam,i+1))
        if answer_user==str(answer):
            break
        
end_time=time.time()
total_time=round(end_time-start_time,2)
print("---------------------------------")
print(total_time)