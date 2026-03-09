from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt

papers = []
figures = []

for file in os.listdir("../data/xml"):
    with open(f"../data/xml/{file}") as f:
        soup = BeautifulSoup(f, "xml")
        count = len(soup.find_all("figure"))

        papers.append(file)
        figures.append(count)

plt.bar(papers, figures)
plt.xticks(rotation=90)
plt.ylabel("Number of figures")
plt.tight_layout()
plt.savefig("../results/figures_per_article.png")