from itertools import groupby
from pprint import pprint
from collections import defaultdict

data = [{
    'field': {
        'data': 'F1'
    },
    'value': 2.2,
    'date': "dd/mm/yyyy"
}, {
    'field': {
        'data': 'F2'
    },
    'value': 1.2,
    'date': "dd/mm/yyyy"
}, {
    'field': {
        'data': 'F2'
    },
    'value': 3.3,
    'date': "dd/mm/yyyy"
}]

expected_output = [
    {
        'F1': [
            {
                'value': 2.2,
                'date': "dd/mm/yyyy"
            }
        ]
    },
    {
        'F2': [
            {
                'value': 1.2,
                'date': "dd/mm/yyyy"
            },
            {
                'value': 3.3,
                'date': "dd/mm/yyyy"
            },
        ]
    }
]


#solution 1

"""
Group by field.data then loop through gropu items to create new DS
"""

actual_output = [{key: [{k: v for k, v in element.items() if k != 'field'}
                        for element in group]}
                 for key, group in groupby(data, lambda element: element['field']['data'])]
pprint(actual_output)



#solution 2
"""
create a defaultdict and with default values to empty list then append item to it
"""
actual_output = defaultdict(list)

for items in data:
    actual_output[items['field']['data']].append({
        'value': items['value'],
        'date': items['date']
    })

