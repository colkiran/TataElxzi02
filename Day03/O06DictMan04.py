
# Copy with dictionary  =

d1={'name':'nithya','age':20,'desig':{1:'engineer',2:'TL'}}
print(f"d1:{d1}")
from copy import deepcopy

d2=deepcopy(d1)  #  deep copy
print(f"d2:{d2}")
d2['desig'][3]="mgr"
print(f"d1:{d1}")
print(f"d2:{d2}")
