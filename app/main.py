import api.client
import json


def load_token_from_json(username): #TODO loading tokens
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    return tokens.get(username)


def save_token_to_json(username, token): #TODO saving tokens
    try:
        # Load existing tokens from the JSON file
        with open('tokens.json', 'r') as f:
            tokens = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty dictionary
        tokens = {}

    # This will overwrite the old token if the username exists
    tokens[username] = token

    # Save the updated tokens back to the JSON file
    with open('tokens.json', 'w') as f:
        json.dump(tokens, f, indent=4)