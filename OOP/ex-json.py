'''JavaScript Object Notation'''
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7168",
            "emails": ["johnsmith@bigseemail,com","john.smith@work_place.com"],
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
# print(type(data))
# # print(data)

for person in data['people']:
    del person['phone']
    # print (person['name'])
 

new_string =json.dumps(data, indent=2, sort_keys=True)
print (new_string)
