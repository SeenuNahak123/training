i=input('Enter a string:     ')
out='Hello   '+i

with open('hello.txt','w') as f:
    f.write(out)