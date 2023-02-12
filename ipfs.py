import requests
import json


def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    projectID = "2LYvv1bvjzxvILIxXGZzKejuMeQ"
    projectSecret = "1cc5f367c0b20a043728edeb9a8a280f"
    endpoint = "https://ipfs.infura.io:5001"

    response = requests.post(endpoint + '/api/v0/add', files=data, auth=(projectID, projectSecret))
    print(response.text)
    cid = response.text.split(",")[1].split(":")[1].replace('"', '')
    return cid


pin_to_ipfs("hello world")
