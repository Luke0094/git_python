preferiti = {"Impara ad usare il browser":"www.impara.com"}

def aggiungi_preferito(nome_preferito, url):
    preferiti.update({nome_preferito:url})

aggiungi_preferito("Youtube","www.youtube.com")
print(preferiti["Youtube"])