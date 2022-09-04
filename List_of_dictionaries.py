from multiprocessing.dummy.connection import families


list_dic=[{},{},{}]
print(list_dic)

list_dic[0]= {
                 "first_name":"Alene",
                 "age":46,
                 "height":134,
                 "weight":67,
                 "marital_status":True,
                 "pets":"two",
                 "no_of_childern":2,
                 "family_record":{
                    "wife_details":{
                    "wife_name":"Guonth",
                    "age":45 },
                 
                    "childern":[
                        {
                            "kid1_name":"Ankel",
                            "age":9
                            },
                        {
                            "kid2_name":"Paroties",
                        "age":6
                        } ]
                 }

                        
}           
                    
                                
list_dic[1]= {
                 "first_name":"fine",
                 "age":40,
                 "height":122,
                 "weight":60,
                 "marital_status":True,
                 "pets":"none",
                 "no_of_childern":1
                 }
list_dic[2]= {
                 "first_name":"joe",
                 "age":46,
                 "height":134,
                 "weight":67,
                 "marital_status":True,
                 "pets":"two",
                 "no_of_childern":2
                 }

print("Printing Total List=",list_dic)
print("printing Alene 1st kid1 name =", list_dic[0]["family_record"]["childern"][0]["kid1_name"])
print("printing Alene r in 1st kid2 name  =", list_dic[0]["family_record"]["childern"][1]["kid2_name"][2])

list_dic.append({})
list_dic[3]= {
                 "first_name":"Sarah",
                 "age":60,
                 "height":150,
                 "weight":80,
                 "marital_status":True,
                 "pets":"five",
                 "no_of_childern":7
                 }
print(list_dic,'\n')
list_dic[3].update({"family_record":{'husband_details': {'husband_name': 'Abraham', 'age': 65}, 'childern': [{'kid1_name': 'Isac', 'age': 9}, {'kid2_name': 'many1', 'age': 6}]}})
list_dic[3]["family_record"]["childern"].insert(2,{"kid3_name":'many2',"age":5})
print(list_dic,'\n')
list_dic[3]["family_record"]["childern"].insert(3,{"kid3_name":'many3',"age":4})
list_dic[3]["family_record"]["childern"].insert(4,{"kid3_name":'many4',"age":3})
list_dic[3]["family_record"]["childern"].insert(5,{"kid3_name":'many5',"age":2})
list_dic[3]["family_record"]["childern"].insert(6,{"kid3_name":'many6',"age":1})
list_dic[3]["family_record"]["childern"].insert(7,{"kid3_name":'many7',"age":0})
print("After adding all seven kids = ",'\n',list_dic,'\n')
print("printing only Sarah details = ",'\n',list_dic[3])


