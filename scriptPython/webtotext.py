from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup

value = [
"au-dela-des-grilles","au-seuil-de-lislam","barrage-contre-le-pacifique","bataille-du-rail","cesar-et-les-gaulois","ceux-du-rail","chefs-de-demain","evasion","gervaise","jeux-interdits","la-baby-sitter","la-belle-et-la-bete","la-bievre","la-boite-aux-reves","la-course-du-lievre-a-travers-les-champs","la-grande-chartreuse","la-grande-pastorale","la-maison-sous-les-arbres","la-symphonie-francaise-du-travail","larabie-interdite","le-chateau-de-verre","le-jour-et-lheure","le-passager-de-la-pluie","le-pere-tranquille","le-triage-de-trappes","les-felins","les-maudits","manoeuvres-de-tanks-en-temps-de-guerre","monsieur-ripois","occitanie","paris-brule-t-il","plein-soleil","quelle-joie-de-vivre","soigne-ton-gauche","toulouse","venus-aveugle",
]
for i in range(len(value)):
    url = "http://fondationreneclement.fr/filmographie/"+ value[i] +"/"

    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style", "nav", "header", "div", "section", "footer", "h1"]):
        if 'class' in script.attrs:
            if "mkdf-page-header" in script.attrs['class']:
                script.extract()    # rip it out
            if "mkdf-mobile-header" in script.attrs['class']:
                script.extract()    # rip it out
            if "section_mission_palmares" in script.attrs['class']:
                script.extract()    # rip it out
            if "mkdf-side-menu" in script.attrs['class']:
                script.extract()    # rip it out
            if "mkdf-page-footer" in script.attrs['class']:
                script.extract()    # rip it out
            if "bouton_or" in script.attrs['class']:
                script.extract()    # rip it out
            if "titre_h1_or" in script.attrs['class']:
                script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)

    with open(value[i]+'.txt', 'x') as f:
        f.write(text)
    # sleep(2)
