from bs4 import BeautifulSoup
import csv
import os

rows = []

for file in os.listdir("../data/xml"):
    with open(f"../data/xml/{file}") as f:
        soup = BeautifulSoup(f, "xml")

        links = [ref.text for ref in soup.find_all("ref") if "http" in ref.text]

        for link in links:
            rows.append([file, link])

with open("../results/links_per_paper.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["paper","link"])
    writer.writerows(rows)