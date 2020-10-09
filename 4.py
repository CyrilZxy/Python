#遍历列表
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician+" is cool !")
    print('魔术师\n')

print('Thanks everybody!')


#数值列表
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

numbers=list(range(1,7))
print(numbers)

numbers=list(range(2,13,2))
print(numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    square = value
    squares.append(value)
print(squares)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares=[value**2 for value in range(1,11)]
print(squares)
#一行代码代替四行代码
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)


#使用列表的一部分
#切片
player=['charles','martina','michael','florence','eli']
print(player[0:3])
print(player[1:4])
print(player[:4])
print(player[2:])
print(player[-3:])

#遍历切片
players=['charles','martina','michael','florence','eli']
for player in players[:3]:
    print(player.title())


my_foods=['pizza','falafel','carrot cake']
print(my_foods)
foods=my_foods[:]
print(foods)

foods=my_foods


#元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250 不能给元组的元素赋值
for dimension in dimensions:
    print(dimension)


dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
for dimension in dimensions:
    print(dimension)






