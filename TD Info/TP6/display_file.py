def display_file(name):
    f = open(name, 'rb')  # Ouvre le fichier en lecture (r = read)
                          # caractère par caractère (b = byte = octet)
    print("Voici les dix premiers caractères du fichier " +
          name + " :")
    for i in range(10):
        c = f.read(1)
        if len(c) == 0:  # vrai si on est arrivé à la fin du fichier
            break
        print("Position " + str(i) + " : '" + c.decode('latin1') +
              "' (code ASCII = " + str(ord(c)) + ")")
    f.close()

display_file('traitement-de-texte.odt')
display_file('cpp.png')
display_file('display_file.py')
display_file('donnees-2-colonnes.csv')
