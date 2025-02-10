
import json

people_string = '''

{
    "people" : [   
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails":["johnsmith@bogus email.com", "john.smith@work-place.com"], 
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]                
}

'''

data = json.loads(people_string)

print(type(data))
print(type(data['people']))

for person in data['people']:
    del person['phone']

newStr = json.dumps(data,indent=2,sort_keys=True)

print(newStr)


# print(data)

