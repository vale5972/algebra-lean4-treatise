import http.server
import socketserver

PORTA = 8080

html_page = """
<!DOCTYPE html>
<html lang="it">
<head>
     <meta charset="UTF-8">
     <title>Monitoraggio Flusso Video Hardware</title>
     <style>
         body { background-color: #050505; color: #1aff1a; font-family: monospace;
     text-align: center; }
          .container { border: 2px solid #1aff1a; padding: 20px; width: 600px; margin:
      40px auto; }
         video { width: 100%; border: 1px solid #1aff1a; background-color: #000;
     height: 250px; }
         .errore { color: #ff3333; margin-top: 15px; font-weight: bold; }
     </style>
</head>
<body>
    <div class="container">
         <h3>[ TERMINALE ] - MONITORAGGIO ATTIVO</h3>
         <p>Stato: Unita Sintonizzata</p>
         <video id="flusso_video" autoplay playsinline></video>
         <div id="messaggio_errore" class="errore"></div>
     </div>
    <script>
        const video = document.getElementById('flusso_video');
        const errore = document.getElementById('messaggio_errore');
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => { video.srcObject = stream; })
            .catch(err => { errore.innerText = "ACCESSO NEGATO / WEBCAM ASSENTE"; })
    ;
    </script>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_page.encode("utf-8"))

with socketserver.TCPServer(("", PORTA), Handler) as httpd:
    httpd.serve_forever()
