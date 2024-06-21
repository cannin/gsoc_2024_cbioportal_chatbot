---
layout: post
title:  "Week Four | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Load Pubmeb Paper
  Loaded 250 pubmed papers in Langchain. 
  Made a list of paper without pmcid, and a list with pmcid but no xml form

### 2. Text splitter and MetaData for Pubmeb Paper
  Desiged and used RecursiveCharacter splitter by using some common header words in papers as separators, such as abstract, conclusion.
  Added metadata, such as pmcid and title for loaded papers.
    
  Comment: The chatbot can response accurately but need title of paper. 
             Trying self-query retriever now to let chatbot do search in metadata first, then text content
    
### 3. PDF loader for pubmed paper
  Found and tried a PDF loader, call PyMuPDFLoader, which can read multi-column paper.

  Comment: Going to use this loader to load rest 28 papers without xml.
              Also, going to try ignore reference part in paper by mention it in prompt.
              
## Next Step:
  1. add all metadatas from cBioPortal study.json
  2. use self query retriever for pubmed database
  3. load 28 pdf paper and ignore reference part.
  4. Think about how to design category management for different data sources.
     
    
