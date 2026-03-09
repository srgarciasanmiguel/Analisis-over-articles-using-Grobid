# Analisis-over-articles-using-Grobid

## Overview

This project analyzes 10 open-access research papers using Grobid to extract structured information from PDFs.

The pipeline performs:

- Abstract extraction
- Keyword cloud generation
- Figure counting
- Link extraction

## Data

10 open-access papers were downloaded from:

- arXiv
- PubMed Central
- ACL Anthology

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

docker run -t --rm -p 8070:8070 lfoppiano/grobid

### Run Scripts

python scripts/run_grobid.py
python scripts/wordcloud_generator.py
python scripts/count_figures.py
python scripts/extract_links.py

## Docker Installation

docker build -t grobid-analysis .
docker run grobid-analysis