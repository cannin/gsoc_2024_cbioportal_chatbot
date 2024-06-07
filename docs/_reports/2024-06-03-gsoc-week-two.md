---
layout: post
title:  "Week Two of GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. OPENAPI Chain for cBioportal API endpoints
  Created a openapi chain using cBioportal API endpoints as spec. 
  It can answer questions about samples and studies by interacting with cBiportal API.
  It can be controled by choosing different parameters for PROJECTION. 
  But the format of response can not be controled by prompt. Need to modify the response to human language.

### 2. Create a Mbox Chatbot
  Converted mbox message to text, and used first 5 messages to test for chatbot.
  Chatbot can answer questions and retrieved mbox messages, and also return the url from the google conversation retrieved.

### 3. PIPENV
  Used pipenv and created pipfile and pipfile.lock to record all the dependencies

### 4. pubmed loader
 Tested pubmed loader from langchain, it can only extract abstract without content of paper. 
 Also, it cannot load paper by pubmed ID, but the title only. 
 Need to modify code to load pubmed by PMID and extract the whole content from pubmed papers.


 ## Next
 1. Modify PubmedLoader to work with PubMedCentral
 2. OpenAPI Spec Loading to Human Language 
  
  
