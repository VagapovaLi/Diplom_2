#import datetime
import allure

import requests

from urls import Urls

class Response:

    RESPONSE_USER_EXISTS = {
        "success": False,
        "message": "User already exists"
    }
