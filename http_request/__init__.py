from __future__ import print_function

import re

from future.utils import raise_

CRLF = "\r\n"
REQUEST_LINE_PATTERN = re.compile(' ')
RAW_VALUE_PATTERN = re.compile('\\r\\n\\r\\n')
HEADERS_BODY_PATTERN = re.compile('\\r\\n')
HEADER_VALUE_PATTERN = re.compile(':')
COOKIE_SEPARATOR_PATTERN = re.compile(';')

VALID_METHODS = ['GET', 'POST', 'OPTIONS', 'HEAD', 'PUT', 'DELETE', 'TRACE', 'CONNECT']


class Request:
    def __init__(self):
        self.method = None
        self.path = None
        self.version = 'HTTP/1.1'
        self.raw_headers = None
        self.headers = dict()
        self.body = ''

    def parse(self, raw_request):
        try:
            raw_headers, self.body = RAW_VALUE_PATTERN.split(raw_request)
            splitted_headers = HEADERS_BODY_PATTERN.split(raw_headers)
            self.method, self.path, self.version = REQUEST_LINE_PATTERN.split(splitted_headers[0])

            if self.method not in VALID_METHODS:
                return False

            self.raw_headers = splitted_headers[1:]

            self.headers = {header: value.strip() for header, value in
                            (HEADER_VALUE_PATTERN.split(raw_h, 1) for raw_h in self.raw_headers)}
            return True
        except ValueError:
            return False

    def build(self):
        if self.method is None or self.path is None:
            raise_(ValueError, value="Not all parameters (method, path, version, body) have been set.")

        request_line = self.method + ' ' + self.path + ' ' + self.version + CRLF

        headers = ''
        for header, value in self.headers.items():
            headers += header + ": " + value + CRLF

        return request_line + headers + "\r\n" + self.body