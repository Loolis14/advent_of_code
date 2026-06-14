from hashlib import md5
from itertools import count


def find_encoding(secret_key: str) -> int:
    key = secret_key.encode()
    for i in count():
        data = key + str(i).encode()
        if md5(data).hexdigest().startswith("0" * 5):
            return i


print('Result:', find_encoding('ckczppom'))
