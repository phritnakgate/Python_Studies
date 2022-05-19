#โครงสร้างข้อมูลของ Pandas จะมี 3 รูปแบบ : Series Dataframe Panel
import pandas as pd
data_int64 = 98,100,78,80,70
data_object = 3.83,4.00,2.98,3.00,2.80,10,'eiei',True

#1. Series => จัดเก็บข้อมูลในรูปแบบ Array 1 มิติ

s1 = pd.Series(data_int64)
s2 = pd.Series(data_object)

#2. Dataframe => จัดเก็บข้อมูลในรูปแบบ Array 2 มิติ

d1 = pd.DataFrame(data_int64)
d2 = pd.DataFrame(data_object)

print(s1)
print(s2)
print(d1)
print(d2)