from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

abstracts = ""

for file in os.listdir("../data/xml"):
    with open(f"../data/mxl/{file}") as f:
        soup = BeautifulSoup(f, "xml")
        abs_tag = soup.find("abstract")

        if abs_tag:
            abstracts += abs_tag.text + " "

wc = WordCloud(width=800, height=400, background_color="white")
wc.generate(abstracts)

plt.imshow(wc)
plt.axis("off")
plt.savefig("../results/wordcloud.png")