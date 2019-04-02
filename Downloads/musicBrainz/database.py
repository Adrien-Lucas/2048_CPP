import sqlite3
import os, sys

connection = None

def set_connection(fn):
    def wrapped(dbfile, *args, **kwargs):
        global connection
        if not connection:
            init_connection(dbfile)
        return fn(connection, *args, **kwargs)
    return wrapped

OOM_HINT = ("Vérifiez que vous n'avez pas oublié une condition dans une jointure.\n"
            "Si le problème persite, essayez de relancer l'exécuteur de requêtes.\n")
   
#########################################################
# Cette fonction exécute sur la base
# la requête passée en paramètre
#########################################################
@set_connection
def execute_query(connection, query):
    try:
        # On récupère un objet curseur qui permet de parcourir l'ensemble résultat à la manière d'un itérateur.
        cursor = connection.cursor()
        
        # On exécute la requête ici.
        cursor.execute(query)

        # Après exécution de la requête, on récupère la réponse du SGBD et on renvoie le tout.
        return cursor.fetchall()

    except MemoryError:
        # Tester avec par exemple SELECT a1.* FROM Artistes AS a1, Artistes AS a2;
        print("Pas assez de mémoire pour exécuter la requête SQL.\n" + OOM_HINT)
        raise
    except sqlite3.Error as e:
        if len(e.args) > 0:
            msg = e.args[0]
        else:
            # Il arrive qu'on obtienne sqlite3.OperationalError sur un
            # "out of memory", et quand c'est le cas, e.args est un
            # tableau vide donc le e.args[0] lancerait une exception
            # dans le traitant d'exception :-(. On devine le diagnostique.
            msg = ("Erreur pendant l'exécution de la requête.\n" + 
                   "Cette erreur peut se produire s'il n'y a pas assez de mémoire.\n" + OOM_HINT)
        print(msg)
        raise


#########################################################
# Cette fonction exécute sur la base
# la requête de mise-à-jour passée en paramètre
#########################################################
@set_connection
def execute_update(connection, query):
    try:
        # On récupère un objet curseur qui permet de parcourir l'ensemble résultat à la manière d'un itérateur.
        cursor = connection.cursor()
        
        # On exécute la requête ici.
        cursor.execute(query)

    except sqlite3.Error as e:
        print("Erreur d'exécution de la requête - %s:" % e.args[0])
    

def commit():
    global connection
    
    if not connection:
        sqlite3.initConnection()

    try:
        connection.commit()

    except sqlite3.Error as e:
        print("Erreur d'exécution de la requête - %s:" % e.args[0])
    

#########################################################
# Cette fonction initialise la connexion à la base
#########################################################
def init_connection(dbfile):
    global connection
    
    if not os.path.isfile(dbfile):
        print("Impossible d'ouvrir la base de données %s:\n"
              "le fichier n'existe pas." %
              dbfile)
        sys.exit(1)

    try:
        connection = sqlite3.connect(dbfile)
    
    except sqlite3.Error as e:
        print("Database connexion error - %s:" % e.args[0])
        close_connection()


#########################################################
# Cette fonction ferme la connexion à la base
#########################################################
def close_connection():
    global connection
    
    if connection:
        connection.close()
        connection = None
