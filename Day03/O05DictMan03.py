
print("clear".center(40, "-"))

player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}
print(f"player :{player}")

player.clear()

print(f"player :{player}")

print("items".center(40, "-"))
# items is a combination of keys and values functions

emp = {'emp1' : {'name':'Jack', 'age':42, 'desig':"MGR", 'dept': 'finance','salary': '65000'},
       'emp2' : {'name':'Mike', 'age':32, 'desig':"PM", 'dept': 'IT','salary': '165000'},
       'emp3' : {'name':'Jane', 'age':30, 'desig': "Analyst",'dept': 'finance','salary': '85000'}
       }

print(f"emp1 : {emp['emp1']}")
print(f"emp2 : {emp['emp2']}")
print(f"emp3 : {emp['emp3']}")

for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, v)
    print("-" * 40)

print("update".center(40, "-"))
# updating emp2 values with emp1 values

emp1 = {'name':'Jack', 'age':42, 'desig':"MGR",'salary': '65000'}
emp2 = {'name':'Mike', 'age':32, 'desig':"PM", 'dept': 'IT'}
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

