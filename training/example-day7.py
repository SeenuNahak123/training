# import datetime

# #get the current date and time
# now=datetime.datetime.now()

# #create a log message
# log_message = f"Log entry created at {now}: This is a log message."


# #open the log file in append mode
# with open('demo.txt','a') as file:
#     #write the log message to the file
#     file.write(log_message+'\n')

# #print a message
# print("Log entry has been writtten to the log file.")


import datetime,random

now=datetime.datetime.now()

with open('demo3.txt','a') as file:

    def rps(best_out_of):
        a=['rock','paper','scissor']
        me=0
        system=0
        for_win=(best_out_of+1)/2
        print(f'Best out of={best_out_of}')
        while me<for_win and system<for_win:
            b=input()
            log_message2 = f"Log entry created at {now}: User selected {b}"
            c=random.choice(a)
            log_message3 = f"Log entry created at {now}: System selected {c}"
            if (b=='rock' and c=='paper') or (b=='paper' and c=='scissor') or (b=='scissor' and c=='rock'):
                system+=1
                print(f'me={b} and system={c}')
            elif(b==c):
                print(f'me={b} and system={c}')
                continue
            else:
                print(f'me={b} and system={c}')
                me+=1
        print(f'me={me} and system={system}')
        return (me,system)

    best_out_of=int(input())
    log_message_1 = f"Log entry created at {now}: User choose best out of {best_out_of}"
    a,b=rps(best_out_of)
    if a>b:
        print("you win")
    else:
        print("system win")


with open('demo.txt','a') as file:
    file.write(log_message+'\n')