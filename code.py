import urllib.request as ul 
from bs4 import BeautifulSoup as soup

url = "https://github.com/nightguarder"
req = ul.Request(url,headers={"User-Agent": "Mozilla/5.0"})
client = ul.urlopen(req)
htmldata = client.read()
client.close()

pagesoup = soup(htmldata, "html.parser")
itemlocator = pagesoup.findAll('div', {"class":"container-xl px-3 px-md-4 px-lg-5"})
filename = "github.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Github, Projects\n"
f.write(headers)

for items in itemlocator:   
    divcontainer = items.findAll("div")
    content = divcontainer[0].text

    plaintext = items.findAll("span")
    text = plaintext[0].text.strip()

    print(content)
    print(text)   

    f.write(content.replace(","," ")  + text.replace(",", " ") + "\n")
    f.write("Total number of div: "  + str(len(itemlocator[0]))) 
f.close()