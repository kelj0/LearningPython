#! /usr/bin/python3

from codecs import latin_1_encode
from wsgiref.simple_server import make_server

def my_handler(environ,start_response):
    path_info = environ.get("PATH_INFO",None)
    query_string = environ.get("QUERY_STRING", None)
    response_body = "You asked for {0} with query {1}".format(path_info,query_string)

    response_headers = [("Content-Type","text/plain"),("Content-Length",str(len(response_body)))]

    start_response("200 OK",response_headers)
    response = latin_1_encode(response_body)[0]
    return [response]


httpd = make_server("127.0.0.1", 8000, my_handler)
httpd.serve_forever()

