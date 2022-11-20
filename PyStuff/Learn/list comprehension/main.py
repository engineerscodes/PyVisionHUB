x = "iron is good"
n = [x for x in x if x != ' ']
print(n)
print(x)

# Cartesian product using a list comprehension
color=['red','green']
size=['L','M','S']

shirts=[(c,s) for c in color for s in size]
print(shirts)

