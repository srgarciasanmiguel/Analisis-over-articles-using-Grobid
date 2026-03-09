# Analisis-over-articles-using-Grobid

## Overview

This project analyzes 10 open-access research papers using Grobid to extract structured information from PDFs.

The pipeline performs:

- Abstract extraction
- Keyword cloud generation
- Figure counting
- Link extraction

## Data

11 open-access papers were downloaded from:

- doaj.org

## Pipeline

1. Convert PDFs → TEI XML using Grobid
2. Extract abstracts
3. Generate keyword cloud
4. Count figures per paper
5. Extract URLs

## Installation

### Environment Setup

conda env create -f environment.yml
conda activate grobid-analysis

### Run Grobid

docker run -t --rm -p 8070:8070 8070:8070 grobid/grobid:0.8.2-crf

### Run Scripts

python scripts/run_grobid.py
python scripts/wordcloud_generator.py
python scripts/count_figures.py
python scripts/extract_links.py

## Docker Installation

docker build -t grobid-analysis .
docker run grobid-analysis