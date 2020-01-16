import bs4	#analyse de page html
import requests	#permet d'utiliser le protocole html
import os	#créer les dossiers
import sys	#récupérer les arguments
import re	
from io import BytesIO	#gère des flux 
from PIL import Image	#transforme en image la page html

def telImages(urlChap, chap):	#fonction telechargement
	while urlChap:		
		page = requests.get(urlChap)	#récupérer la page html
		base = bs4.BeautifulSoup(page.text, 'html.parser')	#parser la page
		try:
			img = base.select_one("img[id='img']").get('src')  #prendre l'image
			print(f"Telechargement...")		#Ecris telechargement
			img_recup = requests.get(img)	#recupérer l'image dans une variable
			image = Image.open(BytesIO(img_recup.content))	
			image.save(os.path.basename(urlChap)+'.jpg')	#enregistrer image
		except Exception as e:
			print("Impossible de telecharger cettte image")

		UrlImg  = base.select_one("div[id='imgholder'] a").get('href')	#recupérer addresse page 
		if int(UrlImg.split("/")[2]) != chap:	#vérifie si le num chap diff chap entré
			break
		urlChap =f"{Url+UrlImg}"	#url chap= url mangapanda+url page


def telManga(nom, numChap):	
	numChap = re.split(r"[ ]",sys.argv[2])	#défini les separateurs
	numChap = list(map(int, numChap))	
	url = f"{Url}/{nom}"	
	chap = numChap[0]	#recuperer num chapitre
	if not os.path.exists(f"{chap}"):	#vérifier si dossier n'existe pas
		try:
			os.mkdir(f"{chap}")	#créer dossier
		except :
			print(f"Impossible de cree le dossier chapitre")
			sys.exit()
						
	os.chdir(f"{chap}")	#changer répertoire
	urlChap = f"{url}/{chap}/1"	#lien page
	telImages(urlChap, chap)	#appele fonction get image
	print("Telechargement complet.")
if __name__ == "__main__":
	nom = sys.argv[1]	#prend le nom du manga en argument
	chapitre = sys.argv[2]	#prend le num chapitre"
	Url = "http://www.mangapanda.com"	#url site
	os.chdir(os.path.abspath("."))	#copie dans repertoire courant

	if not os.path.exists(nom):
		try:
			os.mkdir(nom)	#creer dossier chapitre
		except :
			print(f"Impossible de cree le dossier du manga")
			sys.exit()

	os.chdir(nom)
	telManga(nom, chapitre)