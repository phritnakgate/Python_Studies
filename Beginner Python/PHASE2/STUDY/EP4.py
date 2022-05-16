#Set Operator => คณิตศาสตร์ ม.4 เลยย
fruita = {"กล้วย", "มะยม", "มะนาว"}
fruitb = {"Strawberry", "Kiwi", "มะม่วง", "มะนาว"}

#Union
allfruit = fruita.union(fruitb)
print(allfruit)

#Difference
allfruit = fruita.difference(fruitb)
print(allfruit)

#intersection
allfruit = fruita.intersection(fruitb)
print(allfruit)

#subset
x = {"Strawberry", "Kiwi"}
print(x.issubset(fruitb))

#superset
print(fruitb.issuperset(x))

#max-min
num = {111,222,333,111,222,222,333}
print(min(num))
print(max(num))