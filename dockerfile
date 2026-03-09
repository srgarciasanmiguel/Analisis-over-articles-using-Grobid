FROM python:3.12.3

WORKDIR /Analisis-over-articles-using-Grobid

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "scripts/abstract_wordcloud.py"]