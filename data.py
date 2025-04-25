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


    RESPONSE_NOT_AUTHORIZED = {
        "success": False,
        "message": "You should be authorised"
    }

    RESPONSE_NOT_INGREDIENT = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }



class RequestOrderData:
    payload = {
        "ingredients": ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa74',
                            '61c0c5a71d1f82001bdaaa6c']
    }

