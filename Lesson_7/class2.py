import random

import requests

RCODES = [200, 300, 403, 404, 500]
URL = '*httpbin.org/status/{status}'

def create_retry(try_count):
    def create_retry(func):
        def wrapper(*args):
           func(*args)
        return wrapper
    return create_retry


@retry(5)
def get_request():
    code = random.choice(RCODES)
    resp = requests.get(URL.format(st=code))
    return resp.status_code

print(get_request())

exit()