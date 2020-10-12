#字典

alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#使用字典
alien_0={'color':'green','points':5}
new_points=alien_0['points']
print('get '+str(new_points)+' points!')

alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0={}
alien_0['color']='yellow'
alien_0['points']=6
print(alien_0)

alien_0={'color':'green'}
print(alien_0)
alien_0['color']='yellow'
print(alien_0)

#删除键值对
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print('Sarah like '+
      favorite_languages['sarah'].title())
print('Phil like '+
      favorite_languages['phil'].title())


#遍历字典
user_0={
    'username':'efermi',
    'first':'emrico',
    'last':'fermi'
}
for key,value in user_0.items():
    print('\nKEY:'+key)
    print('VALUE:'+value)


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name,language in favorite_languages.items():
    print(name.title()+
          " favorite language is "+
          language.title()+
          '.')

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())


for name in sorted(favorite_languages.keys()):
    print(name.upper())


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for language in favorite_languages.values():
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.upper())


#嵌套
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#使用range()生成30个外星人
aliens=[]
for alien_number in range(30):
    print(alien_number)
    new_alien={
        'color':'green',
        'points':5,
        'speed':'slow'
    }
    aliens.append(new_alien)
#切片列表
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens:'+
      str(len(aliens)))

for alien in aliens[:3]:
    alien['color']='yellow'
    alien['speed']='medium'
    alien['points']=3
for alien in aliens[:5]:
    print(alien)
print('...')


pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print('crust is :'+pizza['crust'])
for topping in pizza['toppings']:
    print('\t'+topping)


#字典存储字典
user={
    'zxy':{
        'first':'zhang',
        'last':'xinyue',
        'location':'xian'
    },
    'wqq':{
        'first':'wang',
        'last':'qianqian',
        'location':'baoji'
    }
}
for username,user_message in user.items():
    print('username:')
    print(username)
    print('user_message:')
    print(user_message)
