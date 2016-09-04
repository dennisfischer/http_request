from main import Request

if __name__ == '__main__':
    request = Request()
    request.method = 'GET'
    request.path = '/'
    request.version = 'HTTP/1.1'
    request.headers['Host'] = 'www.example.com'
    request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    print(request.build())
