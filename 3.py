#列表
#修改、添加、删除
bicycle = ["aaa","bbb","ccc","ddd"]
print(bicycle)
print(bicycle[0])
print(bicycle[0].title())
print(bicycle[-1])

message = ("this is "+bicycle[2].title())
print(message)

print(bicycle)
bicycle[0]="山地车"
print(bicycle)
bicycle.append("eee")
print(bicycle)

gg=[]
gg.append("gg")
gg.append("mm")
print(gg)

gg.insert(0,"first")
print(gg)

del gg[0]
print(gg)

print(bicycle)
pop_bicycle =bicycle.pop()
print(bicycle)
print(pop_bicycle)

pop_bicycle=bicycle.pop(0)
print(bicycle)
print(pop_bicycle)

bicycle.remove("ccc")
print(bicycle)


#组织列表
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars,reverse=True))
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

l=len(cars)
print(l)


#索引错误使用
cars = ['bmw','audi','toyota','subaru']
#print(cars[100])
'''
Traceback (most recent call last):
  File "D:/PyCharm Project/Python学习/3.py", line 67, in <module>
    print(cars[100])
IndexError: list index out of range

Process finished with exit code 1
'''

