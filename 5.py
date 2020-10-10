#if语句
#示例
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if(car=='bmw'):
        print(car.upper ())
    else:
        print(car.title())

#条件测试
car='bmw'
print(car=='bmw')
print(car=='audi')

car='Audi'
print(car=='audi')
print(car.lower()=='audi')
print(car)

requested='mushrooms'
if requested!='anchovies':
    print('Hold the anchovies!')


age=18
print(age==18)

if(age!=10):
    print("this is not the correct age ! ")

print(age<21)
print(age<=21)
print(age>21)
print(age>=21)


age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
age_1=21
print(age_0>=21 and age_1>=21)



age_0=22
age_1=18
print(age_0>=21 or age_1>=21)
age_0=18
print(age_0>=21 or age_1>=21)


requested=['mushrooms','onions','pineapple']
print('mushrooms' in requested)
print('zxy' in requested)

banned=['andrew','carolina','david']
user='marie'
if user not in banned:
    print('User is not in this banner')


#if语句
age=19
if age>=18:
    print('old enough')
    print('test is true')

age=17
if age>=18:
    print('old enough')
    print('test is true')
else:
    print('not enough')
    print('test is false,run else')


age=12
if age<4:
    print(str(age)+'cost $0')
elif age<18:
    print(str(age)+'cost $5')
else:
    print(str(age)+'cost $10')


requested=['mushrooms','extra cheese']
if 'mushrooms' in requested:
    print('adding mushrooms')
if 'pepperoni' in requested:
    print('adding pepperoni')


#if语句处理表
requesteds=['mushrooms','green peppers','extra cheese']
for requested in requesteds:
    if requested=='green peppers':
        print(requested+'is running over')
    else:
        print('adding'+requested+'.')
print('finished')


requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(requested_topping)
    print('finished')
else:
    print('this is null')