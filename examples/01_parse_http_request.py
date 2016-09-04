from main import Request

if __name__ == '__main__':
    request = Request()
    request.parse(
        '''POST /admin.php HTTP/1.1\r\nHost: team305.webhacky1\r\nContent-Length: 36\r\nCache-Control: max-age=0\r\nOrigin: http://team305.webhacky1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nReferer: http://team305.webhacky1/notes.php\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4\r\nConnection: close\r\n\r\nusername=account0&password=''')
    print(request.build())
