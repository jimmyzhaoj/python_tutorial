''' JavaScript Object Notation '''
import json

with open('C:/Projeccts/Python_Tutorial/OOP/states.json') as f:
  data = json.load(f)
# for stat in data['states']:
#     print(state['name'],state['abbreviation'])
for state in data['states']:
   del state['area_codes']
with open('C:/Projeccts/Python_Tutorial/OOP/states_noareacode.json','w') as f:
    json.dump(data,f, indent=2)