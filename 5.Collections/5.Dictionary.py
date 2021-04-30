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
print(person.clear()) # Remove all

