'''JavaScript Object Notation'''
import json

people_string = """
{
    "people": [
        {
            "name": "John SMith",
             "Phone": "615-555-7164",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                 }
            ],
            "emails": ["johnsmith@bigusemail.com]","john.smith@work-place.com"],
            "has_License": false
        },
         {
            "name": "Jane Doe",
             "Phones": "560-555-5153",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                 }
            ],
            "emails": null,
            "has_License": true
        }
    ]    
}
"""
data = json.loads(people_string)
print(data)
