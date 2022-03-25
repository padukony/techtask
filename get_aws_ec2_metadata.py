# This is a python code that will query the metadata of an AWS EC2 instance and provide a json formatted output.
# This will give all metadata output in one short by passing "all" argument otherwise specific metadata value 
# can be retrieved by passing correct metadata key while executing this code.
# This python program should be executed using python3 on any AWS EC2 instance

import requests
import json
import sys

metadata_url = 'http://169.254.169.254/latest/'

# This method is to look for all subfolders 
def expand_tree(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = expand_tree(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output

# This method is to get all metadata key-value pairs
def get_metadata():
    initial = ["meta-data/"]
    result = expand_tree(metadata_url, initial)
    return result

# This method is to get all metadata key-values in json format 
def get_metadata_json():
    metadata_not_json = get_metadata()
    metadata_json = json.dumps(metadata_not_json, indent=4, sort_keys=True)
    return metadata_json

# This method is to validate the output is in json format or not
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result

# This method is to extract value for specific key
def find_key(key):
    metadata = get_metadata()
    find_key_not_json = list(gen_dict_extract(key,metadata))
    find_key_json = json.dumps(find_key_not_json, indent=4, sort_keys=True)
    return find_key_json

if __name__ == '__main__':
    
    latest_url = metadata_url + "/meta-data"
    argu = requests.get(latest_url)
    valid_argu= argu.text
    
    try: 
        if sys.argv[1] == "all":
            print(get_metadata_json())
        else:
            print(find_key(sys.argv[1]))

    except IndexError:
        print("Enter a valid argument from below list:\n","all\n",valid_argu)

