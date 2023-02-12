import requests
import json


def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    projectID = "2LYvv1bvjzxvILIxXGZzKejuMeQ"
    projectSecret = "1cc5f367c0b20a043728edeb9a8a280f"
    endpoint = "https://ipfs.infura.io:5001"

    files = {
        'file': data
    }

    response = requests.post(endpoint + '/api/v0/add', files=files, auth=(projectID, projectSecret))
    print(response.text)
    cid = response.text.split(",")[1].split(":")[1].replace('"', '')
    return cid


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data