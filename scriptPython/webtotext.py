from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup

value = [
"9004/bio","9008/saisons","9010/2015","9061/figaro-2", "11664/class-40","11687/figaro-3" , "9007/les-partenaires", "9012/medias", "9016/photo", "9017/videos", "9999/presse", "9025/contact",
]
for i in range(len(value)):
    url = "http://julienpulve.com/s/"+ value[i]
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style", "nav", "header", "div", "section", "footer", "h1", "h2", "h3", "h4", "h5", "h6"]):
        if 'class' in script.attrs:
            if "navbar" in script.attrs['class']:
                script.extract()    # rip it out
        # if 'id' in script.attrs:
        #     if "line-4" in script.attrs['id']:
        #         script.extract()    # rip it out
        #     if "line-5" in script.attrs['id']:
        #         script.extract()    # rip it out
        #     if "line-6" in script.attrs['id']:
        #         script.extract()    # rip it out
        #     if "line-7" in script.attrs['id']:
        #         script.extract()    # rip it out
        #     if "cookiesAccept" in script.attrs['id']:
        #         script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)

    

    with open(value[i].replace("/","_")+'.txt', 'x') as f:
        f.write(text)
    # sleep(2)
