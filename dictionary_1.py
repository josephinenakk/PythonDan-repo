family_details = {}

family_details.update({
            "husband":{
                        "first_name":"John",
                        "middle_name":None,
                        "last_name":"Doe",
                        "age":40,
                        "occupation":"Engineer",
                        "hobbies":["Tv","Music","Gardening"]
                        }
                    })
family_details.update({
                        "wife":{
                        "first_name":"Jane",
                        "middle_name":None,
                        "last_name":"Doe",
                        "age":35,
                        "occupation":None,
                        "hobbies":["Tv","Cooking","Craft","Dance"]
                         }
                     })
family_details.update({
                    "children":[
                            {"first_name":"Shane",
                            "middle_name":"Watson",
                            "last_name":"Doe",
                            "age":12,
                            "occupation":None,
                            "hobbies":["Dance","Tv"]},
                            {"first_name":"Lilly",
                            "middle_name":"",
                            "last_name":"Doe",
                            "age":5,
                            "occupation":None,
                            "hobbies":["Tv"]}
                        ]
                           })

family_details.update({
                        "pets":[
                            {
                                "name":"Oliver",
                                "age":7,
                                "gender":"Male"
                            },
                            {
                                "name":"Gus",
                                "age":5,
                                "gender":"female"
                            }
                        ]
                    })
print("\nline 54- family_details dictionary: \n",family_details)
print("\nline 55- who has more number of hobbies?")
# who has more number of hobbies?
f="hobbies"
#if(f in family_details.keys() ):
a = len(family_details["husband"][f])
b= len(family_details["wife"][f])
c = len(family_details["children"][0][f])
d= len(family_details["children"][1][f])

print("line 64- using if and else :")
# using if and else
larger = 0
person_with_more_hobbies = None
if (larger>b):
    pass
else:
    person_with_more_hobbies = "wife"
    larger = b
# -------

if (larger>c):  # larger 4 
    pass
else:
    person_with_more_hobbies = "child_1"
    larger = c # larger 4
# ------
if (larger>d):  # larger 4
    pass
else:
    person_with_more_hobbies ="child_2"
    larger = d
# -------
if (larger>a):
    pass    
else:
    larger = a  # larger 4
    person_with_more_hobbies = "husband"

print ("person_with_more_hobbies , No_of hobbies",[person_with_more_hobbies,larger] )

print("\nline 95- using elif :")
#using elif
if (a > b and a > c and a > d):
    person_with_more_hobbies = ["husband",a]
elif(b > a and b > c and b > d):
    person_with_more_hobbies = ["wife",b]
elif(c > a and c > b and c > d):
    person_with_more_hobbies = ["child 1",c]
elif(d > a and d > b and d > c):
    person_with_more_hobbies = ["child 2",d]
else:
    print ("None")
print("person_with_more_hobbies , No_of hobbies",person_with_more_hobbies)

# who doesnt has the middle name? 
print("\nline 108- who doesnt has the middle name?")
a1=family_details["husband"]["middle_name"] 
b1=family_details["children"][0]["middle_name"] 
c1=family_details["children"][1]["middle_name"] 

people_who_doesnt_has_middle_name = []
if (a1 == None ) or (a1 == "" ):
    people_who_doesnt_has_middle_name.append(family_details["husband"]["first_name"])
if (a1 == None ) or (a1 == "" ):
    people_who_doesnt_has_middle_name.append(family_details["wife"]["first_name"])
if (b1 == None ) or (b1 == "" ):
    people_who_doesnt_has_middle_name.append(family_details["children"][0]["first_name"])
if (c1== None ) or (c1 == "" ):
    people_who_doesnt_has_middle_name.append(family_details["children"][1]["first_name"])

print ("people who doesnt has middle name are",people_who_doesnt_has_middle_name)

print("\nline 127- who is younger oliver or Gus ?")
# who is younger oliver or Gus ?
if (type(family_details["pets"][0]["age"] ) is int and (family_details["pets"][1]["age"]) is int ):
    if (family_details["pets"][0]["age"] == family_details["pets"][1]["age"]):
        print("age is same")
    elif (family_details["pets"][0]["age"] < family_details["pets"][1]["age"]):
      print (" younger pet is ",family_details["pets"][1]["name"])
#elif ((family_details["pets"][0]["age"])== None or (family_details["pets"][0]["age"]) == 0):
   # print(family_details["pets"][0]["name"],"age is None")
#elif ((family_details["pets"][1]["age"]) == None or (family_details["pets"][1]["age"]) == 0):
    #print(family_details["pets"][1]["name"],"age is None")
else:
    print("younger pet is ",family_details["pets"][0]["name"])

print("\nline 141- Are both the pets Male or Female ?")
# Are both the pets Male or Female ? 

#if (family_details["pets"][0]["gender"] == "Male" and family_details["pets"][1]["gender"] == "Male"):
    #print ("Both are Male")
#else:
    #print ("Both are FeMale")
if ((family_details["pets"][0]["gender"]) == (family_details["pets"][1]["gender"])):
    print("both are ",(family_details["pets"][0]["gender"]))
elif((family_details["pets"][0]["gender"]) != (family_details["pets"][1]["gender"])):
    print((family_details["pets"][0]["name"])," is ", (family_details["pets"][0]["gender"]))
    print((family_details["pets"][1]["name"])," is ",(family_details["pets"][1]["gender"]))
print("\n")

"""
Answer:
line 54- family_details dictionary:{
                'husband': {   'first_name': 'John', 
                                'middle_name': None, 
                                'last_name': 'Doe', 
                                'age': 40, 
                                'occupation': 'Engineer', 
                                'hobbies': ['Tv', 'Music', 'Gardening']}, 
                    'wife': {  'first_name': 'Jane', 
                                'middle_name': None, 
                                'last_name': 'Doe', 
                                'age': 35, 
                                'occupation': None, 
                                'hobbies': ['Tv', 'Cooking', 'Craft', 'Dance']}, 
                 'children': [
                    {  'first_name': 'Shane', 
                        'middle_name': 'Watson', 
                        'last_name': 'Doe', 
                        'age': 12,
                        'occupation': None, 
                        'hobbies': ['Dance', 'Tv']}, 
                       {'first_name': 'Lilly', 
                        'middle_name': '',
                        'last_name': 'Doe', 
                        'age': 5,
                         'occupation': None, 
                        'hobbies': ['Tv']}], 
                'pets': [
                    {'name': 'Oliver', 
                     'age': 7, 
                      'gender': 'Male'}, 
                    {'name': 'Gus', 
                     'age': 5, 
                     'gender': 'female'}]}

line 55- who has more number of hobbies?
line 64- using if and else :
person_with_more_hobbies , No_of hobbies ['wife', 4]

line 95- using elif :
person_with_more_hobbies , No_of hobbies ['wife', 4]

line 108- who doesnt has the middle name?
people who doesnt has middle name are ['John', 'Jane', 'Lilly']

line 127- who is younger oliver or Gus ?
younger pet is  Oliver

line 141- Are both the pets Male or Female ?
Oliver  is  Male
Gus  is  female
"""