from typing import *
import os
import json


def create_tokens_folder():
    # If the tokens folder does not exist
    # create one
    if not os.path.exists('tokens'):
        os.mkdir('tokens')


def write_tokens(email: str, access_token: str, refresh_token: str = "") -> None:
    """
    Saves the login tokens for next usage
    :param email: The email of the account used to create the file name
    :param access_token: The access_token retrieved from the server
    :param refresh_token: The refresh_token used when the access_token doesn't work
    :return: None
    """
    email = email.replace('@', '_')
    create_tokens_folder()

    token_object = {
        "email": email,
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    with open(os.path.join('tokens', email + '.token'), 'w') as token_file:
        json.dump(token_object, token_file, indent=4)


def read_tokens(email: str) -> Dict:
    """
    Retrieves login information from previous saved files, excepts AssertionError when not found
    :param email: The email is used to create the token file name, therefore necessary
    :return: A dictionary with the following keys: email, access_token, refresh_token
    """
    email = email.replace('@', '_')
    create_tokens_folder()

    assert os.path.exists(os.path.join('tokens', email + '.token')), "Coloque senha para que um token seja criado"

    with open(os.path.join('tokens', email + '.token'), 'r') as token_file:
        token_object = json.load(token_file)

    return token_object
