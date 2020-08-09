import logging

import requests

from model.booking import BookingData
from model.login_auth import UserData
from common.utils import logging as log

logger = logging.getLogger()


class Client:
    s = requests.Session()

    def __init__(self, url):
        self.url = url

    @log('Login')
    def login(self, user_data: UserData):
        data = user_data.__dict__
        return self.s.post(self.url + "/auth", json=data)

    def set_cookies(self, user_data: UserData):
        res = self.login(user_data)
        if res.status_code != 200:
            raise Exception("Error to authorize")
        session_token = res.json().get("token")
        logger.info(f'Get token {session_token}')
        cookie = requests.cookies.create_cookie("token", session_token)
        self.s.cookies.set_cookie(cookie)

    @log('Create new booking')
    def create_booking(self, data: BookingData):
        data = data.object_to_dict()
        return self.s.post(self.url + "/booking", json=data)

    @log('Update booking')
    def update_booking(self, uid: int, data: BookingData):
        return self.s.put(self.url + f"/booking/{uid}", json=data)

    @log('Get booking by id')
    def get_booking(self, uid: int):
        return self.s.get(self.url + f"/booking/{uid}")