import json

import requests


def clean_data():
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
    r = r.json()
    temp_dict = {}
    for k, v in list(r.items()):
        if v in ['N/A', '-', '']:
            r.pop(k)
        elif v is None:
            r.pop(k)
        elif type(v) == dict:
            for kk, vv in list(v.items()):
                if vv in ['N/A', '-', '', None]:
                    v.pop(kk)
        elif type(v) == list:
            for i in v:
                if i in ['N/A', '-', '', None]:
                    r.pop(k)
    return json.dumps(r)


print(clean_data())

# {"name": {"first": "Daniel", "last": "Smith"}, "age": 45}
