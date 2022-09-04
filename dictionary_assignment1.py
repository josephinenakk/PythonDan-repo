person_details=[{},{},{},{},{}]

person_details[0].update(
    {'Frist_name': 'John', 
    'Middel_name': '', 
    'Last_name': 'Doe', 
    'Age': 40, 
    'Occupation': 'Engineer', 
    'habbies': ['Tv', 'music', 'gardenig']
    })
person_details[1].update(
    {'Frist_name': 'Jane', 
    'Middel_name': '',
     'Last_name': 'Doe',
      'Age': 35, 
      'Occupation': 'None', 
      'habbies': ['Tv', 'Cooking', 'craft', 'singing']
      })

person_details[2].update(
    {'Frist_name': 'Shane', 
    'Middel_name': 'Watson', 
    'Last_name': 'Doe', 
    'Age': 12, 
    'Occupation': '5th grade', 
    'habbies': ['Dance', 'Tv']
    })

"""
person_details[2].update(
    {
    'Frist_name': 'SHane', 
    'Middel_name': 'Watson', 
    'Last_name': 'Doe',
     'Age': 12, 
     'Occupation': '5th grade', 
     'habbies': ['Dance', 'Tv']
     })
"""
person_details[3].update(
    {'Frist_name': 'Lilly',
     'Middel_name': '',
      'Last_name': 'Doe', 
      'Age': 5, 
      'Occupation': 'None', 
      'habbies': ['Tv']})
person_details[4].update(
    {'number_of-pets': 2, 
    'details': [{'name': 'Oliver', 'Type': 'female', 'age': 5}, {'name': 'Gus', 'Type': 'Female', 'age': 4}]
    })

#print(person_details,'\n')

###############################################################################################################

#1. who has more number of hobbies?
print("\nline 57 ********************************\n\n1. who has more number of hobbies? ")
#dict.has_key(key)
f="habbies"
a=len(person_details[0][f])
b=len(person_details[1][f])
c=len(person_details[2][f])
d=len(person_details[3][f])
#print(a,b,c,d)
g="Frist_name"
v="has more habbies than all. \n"
a3=person_details[0].keys()
#print("\nline 68- ",a3)
if( a>b and a>c and a>d):
    print(person_details[0][g],v)
elif(b>a and b>c and b>d):
    print(person_details[1][g],v)
elif(c>a and c>b and c>d):
    print(person_details[2][g],v)
elif(d>a and d>b and d>c):
    print(person_details[3][g],v)
else:
    print ("None")

###############################################################################################################
print ("line 81 ********************************\n ")
#2. who doesnt has the middle name? 
a1=person_details[0]['Middel_name']
b1=person_details[1]['Middel_name']
c1=person_details[2]['Middel_name']
d1=person_details[3]['Middel_name']
y1=(person_details[0]["Frist_name"])
#print(c1)
x1 = []
f1="Frist_name"
#print(a1,b1,c1,d1)
if((a1 == None) or (a1 == '')):
    x1.append(y1)
if((b1 == None) or( b1 == '')):
    x1.append((person_details[1]["Frist_name"])) 
if((c1 == None) or (c1 == '')):
    x1.append(person_details[2]["Frist_name"])
if((d1 == None) or (d1 == '')):
    x1.append(person_details[3]["Frist_name"])
print ("2.people who doesnt has middle name are: \n",x1,"\n","\n")

print("line 102 *******************************\n\n3.who is younger oliver or Gus ?")
# who is younger oliver or Gus ?
if((person_details[4]['details'][0]['age']) > (person_details[4]['details'][1]['age'])):
        print ("younger pet is ",(person_details[4]['details'][0]['name']),"\n")
else:
    print("younger pet is ",(person_details[4]['details'][1]['name']),"\n")

print("\nline 109 *******************************\n\n4.Are both the pets Male or Female ?")
# Are both the pets Male or Female ? 
if((person_details[4]['details'][0]['Type']) == "Male" and (person_details[4]['details'][1]['Type'])=="Male"):
    print("Both are Male","\n********************************\n ")
elif((person_details[4]['details'][0]['Type']) == "Male" and (person_details[4]['details'][1]['Type'])=="Female"):
    print(" Male:",(person_details[4]['details'][0]['name']),"female:",(person_details[4]['details'][1]['name']))
    print("\n********************************\n ")
elif((person_details[4]['details'][0]['Type']) == "Female" and (person_details[4]['details'][1]['Type'])=="Male"):
    print(" Female:",(person_details[4]['details'][0]['name']),"Male:",(person_details[4]['details'][1]['name']))
    print("\n********************************\n ")
else:
    print("Both are Female","\n")

"""
Answer:

line 57 ********************************

1. who has more number of hobbies?
Jane has more habbies than all.

line 81 ********************************

2.people who doesnt has middle name are:
 ['John', 'Jane', 'Lilly']


line 102 *******************************

3.who is younger oliver or Gus ?
younger pet is  Oliver


line 109 *******************************

4.Are both the pets Male or Female ?
Both are Female

"""