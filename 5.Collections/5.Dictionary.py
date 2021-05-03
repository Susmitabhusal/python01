dict1 = {}
dict1 = {'id': 1,    'name': 'Susmita'}
#         key :value  key  : value
dict1 = {1: 'Apple', 2: 'Banana'}
dict1 = {1: 'Apple', 2: 'Banana' , 'list1':[1,2,3,4]}
dict2 = dict({1:'Apple' , 2:'Banana'})

print(dict1)
print(type(dict1))
print(isinstance(dict1,dict))
print(id(dict1))
print(len(dict1))
print()

print("------------------------------")
dict1 = {'id': 1,    'name': 'Susmita'}
print(dict1)
print(dict1['id'])
print(dict1['name'])
dict1['id'] =2
print(dict1)
print()
print("-------------------------------")
person ={}
print("------------------------------------------")
person={}
person['id']=1
person['full_name']='Rajan Thapa'
person['contact_address']='KTM, Nepal'
person['email']=['rajan@yahoo.com','rjan@gamil.com']
person['mobile']=['123456789','456789123']

print(person)
print(len(person))
print(min(person))
print(max(person))

print(person['id'])
print(person.get('id'))
print()
print(person.items()) # dict_items([('id', 1), ('full_name', 'Rajan Thapa'), ('contact_address', 'KTM, Nepal'), ('email', ['rajan@yahoo.com', 'rjan@gamil.com']), ('mobile', ['123456789', '456789123'])])
print()

print(person.keys()) # dict_keys(['id', 'full_name', 'contact_address', 'email', 'mobile'])
print(person.values()) # dict_values([1, 'Rajan Thapa', 'KTM, Nepal', ['rajan@yahoo.com', 'rjan@gamil.com'], ['123456789', '456789123']])
 #print(person.clear()) # Remove all

person2 = person #copy by reference
print(id(person))
print(id(person2))
print()
person3 = person2.copy()
print(id(person3))
print(id(person2))

#for loop with dictionary
print("-----------connectiontion with loop-----------")
for key in person.keys():
    #print(key)
    print(person[key])
print()
for value in person.values():
    print(value)
print()
for key, value in person.items():
    print(key,value)
print()

countries = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}
print("------keys------")
for key in countries.keys():
    print(key)
print()
print("------values-----")
for value in   countries.values():
    print(value)
print()
print("------keys and values-----")
for key,value in countries.items():
    print(key,":" ,value)
print()
for key in countries.keys():
    print(key, "-->" ,countries[key])
print()

countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
             'United Kingdom':{'Capital':'London','Language':'English'},
            'United States':{'Capital':'Washington DC','Language':'English'},
            'Italy':{'Capital':'Rome','Language':'Italian'}
            }
print("-------keys--------")
for key in countries.keys():
    print(key)
print()
print("--------values using keys-----")
for key in countries.keys():
    print(countries[key])
print()
print("------value --------")
for value in countries.values():
    print(value)
print()
print("--------whole dictionary-----")
for key, value in countries.items():
    print(key ,":", value)


