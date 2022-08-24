
family_details = {

}
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
            "gender":"Male"
        }
    ]
})
print(family_details)
# who has more number of hobbies?
f="hobbies"
#if(f in family_details.keys() ):
a = len(family_details["husband"][f])
b= len(family_details["wife"][f])
c = len(family_details["children"][0][f])
d= len(family_details["children"][1][f])


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

people_who_doesnt_has_middle_name = []
if (family_details["husband"]["middle_name"] == None ) or (family_details["husband"]["middle_name"] == "" ):
    people_who_doesnt_has_middle_name.append(family_details["husband"]["first_name"])
if (family_details["wife"]["middle_name"] == None ) or (family_details["wife"]["middle_name"] == "" ):
    people_who_doesnt_has_middle_name.append(family_details["wife"]["first_name"])
if (family_details["children"][0]["middle_name"] == None ) or (family_details["children"][0]["middle_name"] == "" ):
    people_who_doesnt_has_middle_name.append(family_details["children"][0]["first_name"])
if (family_details["children"][1]["middle_name"] == None ) or (family_details["children"][1]["middle_name"] == "" ):
    people_who_doesnt_has_middle_name.append(family_details["children"][1]["first_name"])

print (people_who_doesnt_has_middle_name)

# who is younger oliver or Gus ?

if (family_details["pets"][0]["age"] < family_details["pets"][1]["age"]):
    print (family_details["pets"][1]["name"])
else:
    print(family_details["pets"][0]["name"])


# Are both the pets Male or Female ? 

if (family_details["pets"][0]["gender"] == "Male" and family_details["pets"][1]["gender"] == "Male"):
    print ("Both are Male")
else:
    print ("Both are FeMale")
