# file mode
# 'r'---read
# 'w'--write
# 'a'---append
# 'r+'---read/write
# 'w+'---read/write


# f=open('demo.txt','r')
# print(f.read())
# print(f.read(10))
# for i in range(5):
#    print(f.readline())      #one line at a time
# print(f.readlines())          #all lines in a list format
# f.close()


# f=open('demo1.txt','r')        #if file not present in directory, it will create new file in WRITE MODE  only not in read mode
# f.close

# f=open('demo1.txt','w')  
# f.write('hello world\n')
# f.write('hello python\n')
# f.close()



# f=open('demo1.txt','w')  #once file created dont use write mode to make any changes it will override the file content and create new file if it doesnt exist
# f.write('python\n')
# f.write('c++\n')
# f.close()


# f=open('demo1.txt','w')
# f.writelines(['hello world\n','hello pyhton\n'])
# f.close()


# f=open('demo1.txt','a+')  #add new data at the end without overriding and if file doesnt exist it will create new file 
# f.write('hello abc\n')
# print(f.tell())
# f.write('hello xyz\n')
# f.seek(0)
# print(f.read())
# f.close()


# f=open('demo2.txt','x')    #X MODE - if file not present will create the file and if it already exists it will throw an error
# f.close()


# f=open('demo3.txt','a')     #X,W,A modes will create a new file
# f.close()


# r mode - FileNotFoundError
# X mode - FileExistsError


#'r+' (read and write): it open the file for both rreading and writing the fiel pointer is palce dat the begining of the file
#'w+' (write and read): it opens the file for both writing and reading. it truncates the file if it already exists or create a new file if it doenst exist

#a+' (append and ready):it opens the file for both appending and reading the file pointer is at the end of the file if it exists and it create a new file if it doesnt exist



# with open('demo.txt','r') as f:
#     print(f.read())
# print(f.closed)


# lines=['hello','python','file handling']

# with open('demo2.txt','w') as file:
#     l=[line+'\n' for line in lines]
#     file.writelines(l)






# import json
# #json file contains data in key:value

# # with open('data.json','r') as j:
# #     d=json.load(j)               #load - to read json obj from json file

# # print(type(d))

# d={'Name':'abc',
#    'School':'AAA',
#    'Address':'chennai',
#    'Age':12,
#    'Phone':123456789,
#    'lang':'हिंदी'}

# j_obj=json.dumps(d)                 #dumps - to convert a python object to json object & dump - to load json object to json file
# p_obj=json.loads(j_obj)             #loads - json object to python object


# print(j_obj,type(j_obj))
# print(p_obj,type(p_obj))

# with open('new.json','w') as w:
#     json.dump(d,w,indent=4,sort_keys=True) #data,file_name
    


# with open('new.json','a') as w:
#     json.dump(d,w,indent=4,sort_keys=False) #data,file_name


#update a json file

# with open('new.json','r') as f:
#     d=json.load(f)
# print(d,type(d))
# d['pincode']=600042

# with open('new.json','w',encoding='utf-8') as w:
#      json.dump(d,w,indent=4,ensure_ascii=False)      #ensure_ascii - write characters other than english




# new_employee={
#     "employee":{
#         "id":102,
#         "name":"Ravi",
#         "department":"HR",
#         "skills":["communication","Recruitment"],
#         "address":{
#             "city":"delhi",
#             "zip":"110111"
#         }
#     }
# }


# with open("new_employee.json",'w') as f:
#     json.dump(new_employee,f,indent=4)


#read the employee skills
#print one by one

# with open('new_employee.json','r') as f:
#     d=json.load(f)
# a=d["employee"]["skills"]
# for i in a:
#     print(i)


# #change the zipcode and add a new skill
# d['employee']['address']['zip']='200010'
# d['employee']['skills'].append("Excel")

# with open('new_employee.json','w') as f:
#     json.dump(d,f,indent=4)

# #add new employee

# with open('new_employee.json','r') as f:
#     d=json.load(f)

# d['employee'][1]={"id":103,
#         "name":"Rahul",
#         "department":"IT",
#         "skills":["Security","pipeline"],
#         "address":{
#             "city":"mumbai",
#             "zip":"302073"
#         }}

# with open('new_employee.json','w') as f:
#     json.dump(d,f,indent=4)




import csv

# data=[['Name','age','city'],
#       ['Alice',10,'New york'],
#       ['Bob',11,'New york'],
#       ['john',12,'london']]


# with open('people.csv','w',newline='') as c:
#     writer=csv.writer(c)
#     writer.writerows(data)

# l=[['dave',11,'new york'],
#    ['max',12,'london']]

# with open('people.csv','a',newline='') as c:
#     writer=csv.writer(c)
#     writer.writerows(l)

# data=[['Name','age','city'],
#       ['a',10,'New delhi'],
#       ['b',11,'mumbai'],
#       ['c',12,'chennai']]

# with open('people1.csv','w',newline='') as c:
#     writer=csv.writer(c)
#     writer.writerows(data)


'''with open('people.csv','r',newline='') as a,open('people1.csv','r',newline='') as b, open('people2.csv','w',newline='') as c:
    reader1=csv.reader(a)
    reader2=csv.reader(b)

    writer=csv.writer(c)
    for i in reader1:
        for j in reader2:
            if i==j:
                writer.writerows(i)
            else:
                writer.writerows(i)
                writer.writerows(j)'''



# with open('people.csv','r') as c:
#     reader=csv.reader(c)
#     # # # for row in reader:
#     # # #     print(row)
#     # # print(next(reader))
#     # # print(next(reader))
#     # print(list(reader))


# with open('people.csv','r') as c:
#     reader=csv.DictReader(c)
#     print(list(reader))
#     for row in reader:
#         print(row['Name'],row['age'],row['city'])


# li=[{'Name':'Alice','Age':'10','City':'New york'},
#     {'Name':'Bob','Age':'11','City':'delhi'},
#     {'Name':'John','Age':'12','City':'mumbai'},
#     {'Name':'Dave','Age':'13','City':'New york'},
#     {'Name':'Max','Age':'14','City':'london'}]

# with open('people3.csv','w',newline='') as w:
#     writer=csv.DictWriter(w,fieldnames=['Name','Age','City'])
#     writer.writeheader()
#     writer.writerows(li)


# with open('people3.csv','r+',newline='') as r:  #add new column
    
#     reader=csv.reader(r)
#     writer=csv.writer(r)
#     l=['hindi','english','german','french','mandarin']
#     header = next(reader)
#     header.append('Lang') 
#     i=0
#     for row in reader:
#         row.append(l[i])
#         writer.writerow(row)
#         i+=1




# #field names
# fields=['Name','Branch','Year','CGPA']
# #data rows of csv files
# rows=[['Nikhil','COE','2','9.0'],
#       ['Sanchit','COE','2','9.1'],
#       ['Aditya','IT','2','9.3'],
#       ['Sagar','SE','1','9.5'],
#       ['Prateek','MCE','3','7.8'],
#       ['Sahil','EP','2','9.1']]

# #name of csv file
# #filename="university_records.csv"
# #writing to csv file
# with open('test.csv','w') as csvfile:
#     #creating a csv writer object
#     csvwriter=csv.writer(csvfile,dialect='excel')
#     #writing the fields
#     csvwriter.writerow(fields)
#     #writing the data rows
#     csvwriter.writerows(rows)
        


# import yaml
#pip install pyyaml

# data={
#     "Name":"Desktop",
#     "Version":1.2,
#     "Users":['John','Max']
# }

# with open('project.yaml','w') as w:
#     yaml.dump(data,w,sort_keys=False)
        
# with open('project.yaml','r') as r:
#     data=yaml.safe_load(r)
#     print(data)
    

# data={
#     'employee':{
#         'name':'Alice',
#         'age':30,
#         'contact': {
#             'email':'alice@example.com',
#             'phone':'123456789'
#         },
#         'skills':['python','django','sql']

#     }
# }

# with open('employee.yaml','w') as file:
#     yaml.dump(data,file,sort_keys=False)
        



#json to yaml
#yaml to json


# import json
# import yaml

# data={
#     'employee':{
#         'name':'Alice',
#         'age':30,
#         'contact': {
#             'email':'alice@example.com',
#             'phone':'123456789'
#         },
#         'skills':['python','django','sql']

#     }
# }

# with open('ytoj.yaml','w') as file:
#     yaml.dump(data,file,sort_keys=False)

# with open('ytoj.yaml','r') as r:
#     l=yaml.safe_load(r)

# with open('ytoj.json','w') as w:
#     json.dump(l,w,indent=4)

# with open('new_employee.json','r') as r:
#     l1=json.load(r)

# with open('new_employee.yaml','w') as w:
#     yaml.dump(l1,w,sort_keys=False)




