import requests

TOKEN = ''# Input token


class User:
    def __init__(self, uid):
        self.uid = uid

    def __str__(self):
        return f'https://vk.com/id{self.uid}'

    def __and__(self, other):
        if isinstance(self, User) and isinstance(other, User):
            return self._get_mutual(self.uid, other.uid)
        else:
            return NotImplemented

    def _get_mutual(self, source_uid, target_uid):
        URL = 'https://api.vk.com/method/friends.getMutual'
        params = {
            'v': '5.52',
            'access_token': TOKEN,
            'source_uid': source_uid,
            'target_uid': target_uid
        }
        response = requests.get(URL, params=params)
        try:
            response.raise_for_status()
            if 'response' in response.json().keys():
                return [User(uid) for uid in response.json()['response']]
            else:
                raise requests.exceptions.HTTPError(response.status_code, response.json()['error']['error_msg'])
        except requests.exceptions.HTTPError as error:
            print(error)
            return []


if __name__ == '__main__':
    users = User(input('Input id user №1 : ')) & User(input('Input id user №2 : '))
    for user in users:
        print(user)