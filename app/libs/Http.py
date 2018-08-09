# coding:utf-8

import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        try:
            r = requests.get(url)
            if r.status_code!=200:
                return {} if return_json else ''
            return r.json() if return_json else r.text
        except:
            return {} if return_json else ''

if __name__ == '__main__':
    str = 'hello{}world'
    print(str.format(123))
    str2 = 'hello{}world{}'
    print(str2.format(123,456))