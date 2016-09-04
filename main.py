from __future__ import print_function

import re

from future.utils import raise_

CRLF = "\r\n"
REQUEST_LINE_PATTERN = re.compile(' ')
RAW_VALUE_PATTERN = re.compile('\\r\\n\\r\\n')
HEADERS_BODY_PATTERN = re.compile('\\r\\n')
HEADER_VALUE_PATTERN = re.compile(':')
COOKIE_SEPARATOR_PATTERN = re.compile(';')


class Request:
    def __init__(self):
        self.method = None
        self.path = None
        self.version = None
        self.raw_headers = None
        self.headers = None
        self.body = None

    def parse(self, raw_request):
        try:
            raw_headers, self.body = RAW_VALUE_PATTERN.split(raw_request)
            splitted_headers = HEADERS_BODY_PATTERN.split(raw_headers)
            self.method, self.path, self.version = REQUEST_LINE_PATTERN.split(splitted_headers[0])
            self.raw_headers = splitted_headers[1:]

            self.headers = {header: value.strip() for header, value in
                            (HEADER_VALUE_PATTERN.split(raw_h, 1) for raw_h in self.raw_headers)}
            return True
        except ValueError:
            return False

    def build(self):
        if self.method is None or self.path is None or self.version is None or self.headers is None or self.body is None:
            raise_(ValueError, value="Not all parameters (method, path, version, header, body) have been set.")

        request_line = self.method + ' ' + self.path + ' ' + self.version + CRLF

        headers = ''
        for header, value in self.headers.items():
            headers += header + ": " + value + CRLF

        return request_line + headers + "\r\n" + self.body


if __name__ == '__main__':
    request = Request()
    request.parse(
        '''POST /admin.php HTTP/1.1\r\nHost: team305.webhacky1\r\nContent-Length: 36\r\nCache-Control: max-age=0\r\nOrigin: http://team305.webhacky1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nReferer: http://team305.webhacky1/notes.php\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4\r\nConnection: close\r\n\r\nusername=account0&password=''')
    request.headers['X-Session-Id'] = 'verycreative'
    request.method = 'GET'
    print(request.build())
