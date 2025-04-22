#import datetime
import allure

import requests

from urls import Urls

class Response:

    RESPONSE_USER_EXISTS = {
        "success": False,
        "message": "User already exists"
    }

    RESPONSE_INCOMPLETE_DATA = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    RESPONSE_INCORRECT_DATA = {
        "success": False,
        "message": "email or password are incorrect"
    }