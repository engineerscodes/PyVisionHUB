 #not duplicate key allowed
 #   duplicate of key is present it will overwrite
customer ={
     "name":"Naveen",
     "Age":19.5,
     "sex":"Male",
    "Age": "19",
     "is noob" :True
 }
#create a new key
customer["color"] ="Black"
#alter
customer["Age"]="19yr"
print(customer)

print(customer["name"])
#print(customer["SEX"]) #because key is not present
"""
Traceback (most recent call last):
  File "C:/Users/HP/PycharmProjects/LearnPython/01.Basic/Dictionaries/dict.py", line 13, in <module>
    print(customer["SEX"])
KeyError: 'SEX'
"""
#to prevent this error use get if the key is not present return none
print(customer.get("SEX"))

#return custome  default value other than none if no key exists

print(customer.get("SEX","key is not present")) #key is not present is displayed

print(customer.get("sex","key is not present")) #male is displayed because key this there
