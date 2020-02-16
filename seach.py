from user_class import User
from urllib.parse import urlencode

ourfriends = User()
user1_id = input('Input id user №1 : ')
user2_id = input('Input id user №2 : ')

ourfriends.users(user1_id, user2_id)

url = 'https://vk.com/id'
user = ''.join((url, user1_id))

print(user)