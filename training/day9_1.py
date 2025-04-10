# #command line arg
# import sys
# from functools import reduce
# # print('hello')
# #print(sys.argv)
# # py day9.py 1 2 3 4

# # print(sys.argv[0])
# # print(sys.argv[1:])
# # print(f'file name {sys.argv[0]}')


# print(reduce(lambda a,b:int(a)+int(b),sys.argv[1:5]))





# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('name',help="enter your name") #without '--' positional arg
# parser.add_argument('phone',type=int,nargs='?',default=123456789,help="enter phone number")
# parser.add_argument('-a','--age',required=True,help="enter your age")   #with '--' Optional arg
# parser.add_argument('-t','--true',action='store_true') 


# args=parser.parse_args()

# print(args.name)
# print(args.phone)
# print(type(args.phone))
# print(args.age)
# print(args.true)





# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('name',nargs='?',default='ABC',help="enter your name") #accept default value for positional argument
# # parser.add_argument('colors',nargs='*',help='enter color') #variable length - stores it in list
# parser.add_argument('colors',nargs='+',help='enter color') #one or more
# args=parser.parse_args()
# #name='abc','xyz','ijk' (packing day1 stores in tuple)
# print(args.name)
# print(args.colors)
# print(type(args.colors))




# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('--fruits',choices=['apple','banana'],default='apple',help="choose fruit")

# args=parser.parse_args()

# print(args.fruits)


# import argparse

# parser=argparse.ArgumentParser(
#     description='enter the name in commad line.'
# )

# parser.add_argument('-n','--name',metavar='Name',required=True)

# args=parser.parse_args()

# print(f"hello {args.name}")





# import argparse

# parser=argparse.ArgumentParser()
# parser.add_argument('--limit',metavar='1-10',type=int,help="maximum value to process")
# args=parser.parse_args()
# print(args.limit)






# import argparse
# def greeting(name,lang):
#     greet={'English': 'Hello',
#            'Spanish':"Hola",
#            'German':"Hallo"}
    
#     print(f"{greet[lang]} {name}!")

# parser=argparse.ArgumentParser('Get language from the user by using cmd')
# parser.add_argument('-n','--name',metavar='Name',required=True)
# parser.add_argument('-l','--lang',metavar='Language',choices=['English','Spanish','German'],required=True)
# args=parser.parse_args()
# greeting(args.name,args.lang)


# import argparse

# parser=argparse.ArgumentParser()

# login_group=parser.add_argument_group('Login Data')
# login_group.add_argument('-u','--user',help='enter user name')
# login_group.add_argument('-p','--password',help='enter user password')

# personal_data=parser.add_argument_group('Personal Data')
# personal_data.add_argument('-n','--name',help='enter name')
# personal_data.add_argument('-a','--age',help='enter age')

# args=parser.parse_args()




# import argparse

# parser=argparse.ArgumentParser()

# group=parser.add_mutually_exclusive_group(required=True)
# group.add_argument('--upload',action='store_true',help='Upload a file')
# group.add_argument('--download',action='store_true',help='Download a file')

# args=parser.parse_args()

# if args.upload:
#     print("Uploading...")
# elif args.download:
#     print("Downloading...")

'''------------------------------------------------------------------------------------------------------------------------------'''

#tasks

#take a list of numbers as arguments and print their average
# import sys

# def avg(l):
#     sum=0
#     for i in l:
#         sum+=int(i)
#     print(sum/len(l))

# avg(sys.argv[1:])

'''------------------------------------------------------------------------------------------------------------------------------'''
#accept a filename and count how many lines it has
# import sys
# def countline(file):
#     with open(f'{file}','r') as r:
#         d=r.readlines()
#     print(len(d))
# countline(sys.argv[1])

'''------------------------------------------------------------------------------------------------------------------------------'''

#pass 2 words and print the longer one
# import sys

# def avg(a,b):
#     print(a if len(a)>len(b) else b)

# avg(sys.argv[1],sys.argv[2])


'''------------------------------------------------------------------------------------------------------------------------------'''
#check if a number passed is prime
# import sys

# def prime(a):
#     flag=0
#     for i in range(2,int(a)):
#         if int(a)%i==0:
#             flag=1
#             break
#     print('prime' if flag==0 else 'not prime')
    
# prime(sys.argv[1])

'''------------------------------------------------------------------------------------------------------------------------------'''
#accept multiple filename and print which ones exist

# import sys
# import os
# def exist1(a):
#     for file in a:
#         if os.path.isfile(file):
#             print(file)
# exist1(sys.argv[1:])


'''------------------------------------------------------------------------------------------------------------------------------'''

#Argparse

'''------------------------------------------------------------------------------------------------------------------------------'''
#add two numbers using argparse
# import argparse

# parser=argparse.ArgumentParser('provide 2 numbers for addition')

# parser.add_argument('a',type=int,help="first number")
# parser.add_argument('b',type=int,help="second number")

# args=parser.parse_args()
# print(args.a+args.b)

'''------------------------------------------------------------------------------------------------------------------------------'''
#repeat a word
#accept a word and a count as argumants, print the word that many times
# import argparse
# parser=argparse.ArgumentParser('Provide a word and number n to print the word n times')

# parser.add_argument('word',help='Provide a word to be repeated')
# parser.add_argument('n',type=int,help='provide n for repetition')

# args=parser.parse_args()
# print(f'{args.word} '*args.n)


'''------------------------------------------------------------------------------------------------------------------------------'''
# choose aperation(add,subtract)
# accept two numbers and an operation(--op add or --op sub)
# import argparse

# parser=argparse.ArgumentParser("Provide 2 number and select an operation")

# parser.add_argument('a',type=int,help='first number')
# parser.add_argument('b',type=int,help='second number')
# parser.add_argument('--op',choices=['add','sub'],required=True,help='select aan operation')

# args=parser.parse_args()
# if args.op=='add':
#     print(args.a+args.b)
# elif args.op=='sub':
#     print(args.a-args.b)

'''------------------------------------------------------------------------------------------------------------------------------'''
# Multiple File Inputs
# Goal: Use nargs='+' to accept a list of file names

# import argparse
# parser=argparse.ArgumentParser('Multiple files inputs')
# parser.add_argument('list',nargs='+',help='Provide one or more file names')
# args=parser.parse_args()
# print(args.list)

'''------------------------------------------------------------------------------------------------------------------------------'''
# Word Counter
# Description:Accept a sentence and count number of words.

# import argparse
# parser=argparse.ArgumentParser("accept a sentence and count number of words")

# parser.add_argument('sentence',nargs='*',help="provide a sentence")
# args=parser.parse_args()
# print(len(args.sentence))

'''------------------------------------------------------------------------------------------------------------------------------'''
# Create a User Profile
# Description:
# Collect user's name, age, and gender from command line and print profile.

# import argparse
# parser=argparse.ArgumentParser("Data for user profile")
# parser.add_argument('-n','--name',required=True,help="User Name")
# parser.add_argument('-a','--age',required=True,help="User Age")
# parser.add_argument('-g','--gender',choices=['male','female'],required=True,help="User gender")

# args=parser.parse_args()
# print(f"Name: {args.name}")
# print(f"Age: {args.age}")
# print(f"Gender: {args.gender}")

'''------------------------------------------------------------------------------------------------------------------------------'''

# File Analyzer
# Description:
# Take a file name as input, and return:

# Number of lines
# Number of words
# Number of characters
# Based on flags passed.

# Arguments:

# filename (positional)
# --lines (store_true)
# --words (store_true)
# --chars (store_true)

# import argparse

# parser=argparse.ArgumentParser("take a file and print number of lines,words,characters")

# parser.add_argument('filename',help='Provide filename for counting')
# parser.add_argument('--lines',action='store_true',help='Prints number of lines')
# parser.add_argument('--words',action='store_true',help='Prints number of words')
# parser.add_argument('--chars',action='store_true',help='Prints number of characters')

# args=parser.parse_args()

# if args.lines:
#     with open(args.filename,'r') as r:
#         d=r.readlines()
#     print(len(d))

# if args.words:
#     with open(args.filename,'r') as r:
#         d=r.read().split()
#     print(len(d))
# if args.chars:
#     with open(args.filename,'r') as r:
#         d=r.read()
#     print(len(d))
'''------------------------------------------------------------------------------------------------------------------------------'''

# Temperature Converter
# Description:
# Convert temperature from Celsius to Fahrenheit or vice versa.

# Arguments:

# --value (required, float)

# --to (choices=['C', 'F'], required)

# import argparse
# parser=argparse.ArgumentParser("Temperature converter")
# parser.add_argument('-v','--value',required=True,type=float,help='provide a number for conversion')
# parser.add_argument('--to',choices=['C','F'],required=True,help='provide conversion type')

# args=parser.parse_args()
# if args.to=='C':
#     print(((args.value-32)*5)/9)
# elif args.to=='F':
#     print(((args.value*9)/5)+32)


'''------------------------------------------------------------------------------------------------------------------------------'''

# Search for Word in File
# Description:
# Search for a word in a text file and print line numbers containing that word.

# Arguments:

# filename (positional)

# --word (required)

# import argparse

# parser=argparse.ArgumentParser("print line number containing the word")
# parser.add_argument('filename',help="provide a file to search")
# parser.add_argument('-w','--word',required=True,help='provide a word to search')

# args=parser.parse_args()

# with open(args.filename,'r') as r:
#     d=r.readlines()
# count=0
# for i in d:
#     if args.word in i:
#         print(f"{count+1}")
#     count+=1

'''------------------------------------------------------------------------------------------------------------------------------'''




