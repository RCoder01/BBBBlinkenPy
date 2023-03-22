import requests

_header = {'Content-type': 'application/json'}

jsfunction = str
token = str
data = str

class Blinken:
    @staticmethod
    def from_components(code: jsfunction, url: str, title: str, author: str) -> data:
        return Blinken(f'{{"code":{code},"url":"{url}","title":"{title}","author":"{author}"}}')

    def __init__(self, data: data) -> None:
        res = requests.post(url="https://blinken.org/api/0/publish", data=data, headers=_header)
        if 200 <= res.status_code < 400:
            self.token = res.text
        else:
            raise ValueError("Unexpected status code", res)

    def get_status(self) -> requests.Response:
        return requests.get(f'https://blinken.org/api/0/status/{self.token}', headers=_header)

    def cancel(self) -> requests.Response:
        return requests.post(f'https://blinken.org/api/0/cancel/{self.token}', data='{}', headers=_header)

if __name__ == '__main__':
    import json

    default = Blinken.from_components(
        # javascript
        json.dumps('''
        function () {
            // My self-contained program goes here.
            var x = 0;
            var d = 1;
            var n = 10;
            // Update lights one frame
            return function (lights) {
                for (i = 0; i < lights.length; i++) {
                    if (i > x - n && i < x + n) {
                        lights[i].rgb(1, 0, 0);
                    } else {
                        lights[i].rgb(0, 0, 0);
                    }
                }
                x += d;
                if (x == lights.length+n || x == -n) {
                    d *= -1;
                }
                return 50; // ms until called again
            };
        }'''),
        'https://fiddle.jshell.net/aLgm721f/show/light/',
        'Red Snake',
        'Anonymous')
