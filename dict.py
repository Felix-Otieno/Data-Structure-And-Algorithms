dict = {
    'Species': 'Homo Sapien',
    'FirstName': 'Tonny',
    'SecondName': 'Otieno',
    'age': 19,
    'Language': 'Luo',
    'Country': 'Kenya',
    'Nationality': 'Kenyan'
}

dict["FirstName"] = "Robinson"
dict['color'] = 'black'
print(dict)
print(type(dict))


for key, value in dict.items():
    print(key,":", value)