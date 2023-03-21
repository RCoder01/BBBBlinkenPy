import requests

_header = {'Content-type': 'application/json'}

jsfunction = str
token = str
data = str

def create_data(code: jsfunction, url: str, title: str, author: str) -> data:
    return f'{{"code":"{code}","url":"{url}","title":"{title}","author":"{author}"}}'

def set(data: data) -> token:
    return requests.post(url="https://blinken.org/api/0/publish", data=data, headers=_header).text

def get(token: token) -> requests.Response:
    return requests.get(f'https://blinken.org/api/0/status/{token}', headers=_header)

def cancel(token: token) -> requests.Response:
    return requests.post(f'https://blinken.org/api/0/cancel/{token}', data='{}', headers=_header)

if __name__ == '__main__':
    default = create_data(
        r'function () {\n    // My self-contained program goes here.    \n    var x = 0;\n'
        r'    var d = 1;\n    var n = 10;\n\n    // Update lights one frame\n    return function'
        r' (lights) {\n        for (i = 0; i < lights.length; i++) {\n            '
        r'if (i > x - n && i < x + n) {\n                lights[i].rgb(1, 0, 0);\n            } '
        r'else {\n                lights[i].rgb(0, 0, 0);\n            }\n        }\n        x += d;'
        r'\n        if (x == lights.length+n || x == -n) {\n            d *= -1;\n        }\n        '
        r'return 50; // ms until called again\n    };\n}',
        'https://fiddle.jshell.net/aLgm721f/show/light/',
        'Red Snake',
        'Anonymous')

    token = set(default)
