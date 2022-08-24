person_details={}
""""
#created empyy dictionary and using update method created dictionary with given data
person_details.update({"Husband_details":{'Frist_name': 'John', 'Middel_name': '', 'Last_name': 'Doe', 'Age': 40, 'Occupation': 'Engineer', 'habbies': ['Tv', 'music', 'gardenig']}})
person_details.update({"wife_details":{'Frist_name': 'Jane', 'Middel_name': '', 'Last_name': 'Doe', 'Age': 35, 'Occupation': 'None', 'habbies': ['Tv', 'Cooking', 'craft', 'singing']}})
person_details.update({"kid1_details":{'Frist_name': 'SHane', 'Middel_name': 'Watson', 'Last_name': 'Doe', 'Age': 12, 'Occupation': '5th grade', 'habbies': ['Dance', 'Tv']}})
person_details.update({"kid2_details":{'Frist_name': 'Lilly', 'Middel_name': '', 'Last_name': 'Doe', 'Age': 5, 'Occupation': 'None', 'habbies': 'Tv'})
#person_details.update({"pets_details":{'number_of-pets': 2, 'details': [{'name': 'Oliver', 'Type': 'Male', 'age': 5}, {'name': 'Gus', 'Type': 'Male', 'age': 4}]}}})
print(person_details)
#1.who has more number of hobbies?
#x=(person_details[0]["habbies"])
y=len(x)
#print(y)

b="habbies"
c=0
if(b in person_details[c]):
    print(person_details[c][b])
    print(type(person_details[c][b]))
    d=(person_details[c][b])
    g=len(d)
    print(y)

    #increase the value of c and compre g with previous value and keep greatest value 
    '''b="Occupation"
    for x in person_details:
    for a in x:
        if(b in a):
         print(a)

    '''

    #2.who doesnot have middle name?
b="Middel_name"
c=2
if(b in person_details[c]):
    print(person_details[c][b])
    print(type(person_details[c][b]))
    d=(person_details[c][b])
    print(d)
    """

'''
    presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
'''

person_details.update({ 
    "Husband_details":{
    "Frist_name":"John",
    "Middel_name":"",
    "Last_name":"Doe",
    "Age":40,
    "Occupation":"Engineer",
    "habbies":["Tv","music","gardenig"]
    }
})
print(person_details)

person_details.update({ 
    "Wife_details":{
    "Frist_name":"Jane",
    "Middel_name":"",
    "Last_name":"Doe",
    "Age":35,
    "Occupation":"None",
    "habbies":["Tv","Cooking","craft","singing"]}})
print(person_details)


person_details.update([
    {
    "FirstKid":{ 
    "Frist_name":"SHane",
    "Middel_name":"Watson",
    "Last_name":"Doe",
    "Age":12,
    "Occupation":"5th grade",
    "habbies":["Dance","Tv"]}

    "SecondKid":{ 
    "Frist_name":"Lilly",
    "Middel_name":"",
    "Last_name":"Doe",
    "Age":5,
    "Occupation":"None",
    "habbies":"Tv"}}])
    
person_details.update({
    "number_of_pets":2,
    "details":[{
        "name":"Oliver",
        "Type":"Male",
        "age":5
    },{"name":"Gus",
        "Type":"Male",
        "age":4}
    ]

} )

print(person_details)


