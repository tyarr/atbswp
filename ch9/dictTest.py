myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],
          'firstName': ['Alan', 'Mary-Ann'], 'lastName': ['Stone', 'Lee']}

def search(myDict, lookup):
    for key, value in myDict.items():
        for v in value:
            if lookup in v:
                return key

search(myDict, 'Mary')