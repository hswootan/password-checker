import requests
import hashlib
from colored import fg, attr
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwdned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(response)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwdned_api_check(password)
        if count:
            print(
                f"%s[+] -> [{password}]%s" % (fg(1), attr(1)) + f" was found {count} times ... you should change your password")
        else:
            print(f"%s[+] -> [{password}]%s" %
                  (fg(2), attr(1)) + " was not found. ")
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
