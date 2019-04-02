#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import musique
import urllib.parse as urlparse

PORT_NUMBER = 4242

def format_matching_artists(pattern):
    return "QUESTION 12 A FAIRE !\n\nPATTERN RECU:" + pattern


#########################################################
# Cette classe est en charge de traiter les requêtes HTTP
# entrantes sur le port indiqué ci-dessus
#########################################################
class ReleaseHandler(BaseHTTPRequestHandler):
    
    # On ne traite que deux types de requêtes GET possibles :
    # 1. La page d'accueil (index.html, ou URL "/")
    # 2. La page query, qui répond à une requête de demande d'albums
    # Toute autre requête répond avec une erreur 404
    def do_GET(self):
        if self.path.startswith("/query"):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=UTF-8')
            self.end_headers()

            # Ici on récupère la valeur passée dans le champ « artist » du formulaire
            params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            artist = '' if len(params.get('artist', '')) == 0 else params.get('artist', '')[0]
            listArtists = format_matching_artists(artist)
            # Et là on va commencer à envoyer la réponse (i.e. afficher la page)
            self.wfile.write(bytes(listArtists, "utf-8"))

            return

        if self.path == "/" or self.path == "index.html":
            self.path="index.html"
            # On ouvre le fichier HTML statique et on l'affiche
            self.send_response(200)
            self.end_headers()
            self.serveFile(curdir + sep + self.path)
            return
		
        self.send_error(404,'Fichier non trouvé : %s' % self.path)
			
    def serveFile(self, fileName):
        f = open(fileName, 'r', encoding="utf-8") 
        self.wfile.write(f.read().encode("utf-8"))
        f.close()

if __name__ == "__main__":   
    try:
        # Ici on crée un serveur web HTTP, et on affecte le traitement
        # des requêtes à notre releaseHandler ci-dessus.
        server = HTTPServer(('', PORT_NUMBER), ReleaseHandler)
        print('Serveur démarré sur le port ' , PORT_NUMBER)
        print('Ouvrez un navigateur et tapez dans la barre d\'url : http://localhost:%d/' % PORT_NUMBER) 
        
        # Ici, on demande au serveur d'attendre jusqu'à la fin des temps...
        server.serve_forever()

    # ...sauf si l'utilisateur l'interrompt avec ^C par exemple
    except KeyboardInterrupt:
        print('^C reçu, je ferme le serveur. Merci.')
        server.socket.close()
	
