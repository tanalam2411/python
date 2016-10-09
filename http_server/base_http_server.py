import json
import uuid
import BaseHTTPServer


HOST_NAME = ''
PORT_NUMBER = 8080


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    https://wiki.python.org/moin/BaseHttpServer
    """

    def do_GET(self):
        pass

    def do_POST(self):
        print self.path
        if self.path == '/Netra/oauth/token':
            self.send_response(200, 'OK POST')
            self.send_header('Content-Type', 'appplication/json')
            self.end_headers()
            self.wfile.write(json.dumps({"access_token": str(uuid.uuid4())}))
        elif self.path == '/Netra/api/dc/register':
            self.send_response(200, 'ok NCE1')
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({'data':
                                             {'siteId': str(uuid.uuid4()),
                                              'orgId': str(uuid.uuid4())}
                                         }))
            print self.client_address
        else:
            self.send_response(404)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer


    # httpd = server_class((HOST_NAME, PORT_NUMBER), Handler)
    #
    # print "Serving http on port 8080"
    # httpd.serve_forever()

    def worker(host_name, port, handler, server_class):
        print "\nServing http on port: ", port
        httpd = server_class((host_name, port), handler)
        httpd.serve_forever()


    import threading

    threads_list = []
    t1 = threading.Thread(target=worker, args=('0.0.0.0', 8081, Handler, server_class))
    t2 = threading.Thread(target=worker, args=('127.0.0.2', 8080, Handler, server_class))
    threads_list.append(t1)
    threads_list.append(t2)
    t1.start()
    t2.start()