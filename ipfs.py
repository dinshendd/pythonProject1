import requests
import json


def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    projectID = "2LYvv1bvjzxvILIxXGZzKejuMeQ"
    projectSecret = "1cc5f367c0b20a043728edeb9a8a280f"
    endpoint = "https://ipfs.infura.io:5001"

    datastr = str(data)

    files = {
        'file': datastr
    }

    response = requests.post(endpoint + '/api/v0/add', files=files, auth=(projectID, projectSecret))

    cid = response.text.split(",")[1].split(":")[1].replace('"', '')
    return cid


def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
    # YOUR CODE HERE
    projectID = "2LYvv1bvjzxvILIxXGZzKejuMeQ"
    projectSecret = "1cc5f367c0b20a043728edeb9a8a280f"
    endpoint = "https://ipfs.infura.io:5001"

    params = {
        'arg': cid
    }

    response2 = requests.post(endpoint + '/api/v0/cat', params=params, auth=(projectID, projectSecret))

    data = json.loads(response2.text)

    assert isinstance(data,dict), f"get_from_ipfs should return a dict"

    return data