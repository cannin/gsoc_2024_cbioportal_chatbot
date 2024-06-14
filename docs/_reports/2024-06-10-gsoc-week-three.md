---
layout: post
title:  "Week Three | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Create a loader for extracted text from xml
Brief: Load extracted xml text and build a pubmed chatbot demo

Comment: It could answer questions like, "what platform was used to collect RNAseq data?", at first time, but not every time.
     The response accuracy needed to improve. It can be improved by designing efficient text splitter. 

Status: **Done**
     
### 2. Write a pipeline to load pubmed papers
Brief: Download all the studies in cBioPortal dataset. 
       Make a list of study with pmid and another list of study without pmid. 
       Convert all the pmids to pmcids, and download xml papers using aws S3. 
       Extract text from xml files and load text to langchain. 
       Add metadata for each paper, such as pmid, pmcid and paper title.
       
Comment: tested this pipeline with one paper. Going to test more papers.

Status: **Done**

### 3. Find pmid for studies have articles
Brief: There are 5 studies have pmid but missed pmid and reference link in cBioportal datahub.
       Find 5 studies's pmid in pmc.

Status: **Done**

## Next Step
  1. Load all the pubmed papers using the pipeline created this week.
  2. Design text splitter for pubmed text.
  3. Create a PR for 5 missing pmids in cBioPortal datahub.
       
     
     
