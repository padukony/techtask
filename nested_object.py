# Function to get the value for specific key in nested json object
import json

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
def find_key(key,object1):
    find_key_not_json = list(gen_dict_extract(key,object1))
    return find_key_not_json

if __name__ == '__main__':
    object1 = {"a":{"b":{"c":"d"}}}
    key = "a"
    print("Key:",key," Value:",find_key(key,object1))
