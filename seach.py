from user_class import User

ourfriends = User()
user1_id = input('Input id user №1 : ')
user2_id = input('Input id user №2 : ')

ourfriends.__str__()

url = 'https://vk.com/id'
user = ''.join((url, user1_id))

print(user)