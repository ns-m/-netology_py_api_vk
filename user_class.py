import requests
from pprint import pprint

class User:

    def users(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id
        vk = "https://api.vk.com/method"
        access_token = '2a0545aa68a19df8fb37eb969049ac8c06e0f80191a7608cb539ea6bb017b01296311ece43998aee0a577'

        query_params = {
            'site': vk,
            'access_token': access_token,
            'source_uid': self.user1_id,
            'target_uid': self.user2_id
            }

        query = "{site}/friends.getMutual?access_token={access_token}&source_uid={source_uid}&target_uid={target_uid}&v=5.103".format(**query_params)
        response = requests.get(query).json()
        self.response = response
        pprint(f'ID Our friends : {self.response["response"]}')
