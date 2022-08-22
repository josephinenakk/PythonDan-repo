student_details_dictionary = {
                                "student_name":"Mark",
                                "percentage":62.3,
                                "grade":"B-",
                                "isPassed":True,
                                "teachers":{
                                    "science":"Tr Michone",
                                    "math":"Tr suzan"
                                },
                                "subjects":
                                            {
                                                "science":[True,52.3],
                                                "math":[True,67.89]
                                            },
                                "other_activities":{
                                                        "outdoor":"Cricket",
                                                        "indoor":"Badminton"}
                        }
print(student_details_dictionary["other_activities"].update({"outdoor":"football"}))
print(student_details_dictionary)