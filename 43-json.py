#dic
import json


person={"name":"Ali","languages":["Python","Java"]}

result=person["name"]
result=person["languages"][1]

person_string= '{"name":"Ali","languages":["Python","Java"]}'



# JSON string to Dict
dict_result=json.loads(person_string)

print(dict_result["name"])
print(dict_result["languages"][1])

with open("43-person.json") as f:
    data=json.load(f)
    print(data)



#dict to json string
person_dict={
    "name":"Ali",
    "languages":["Python","Java"]
}   
result_jsonString=json.dumps(person_dict)
print(result_jsonString)


with open("43-person.json","w") as f:
    json.dump(person_dict,f)


result_readable=json.dumps(person_dict,indent=4,sort_keys=False)    
print(result_readable)