---
layout: post
title:  "Week Six | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Create embedding for datasets
Created embedding for pubmed pdf and pubmed papers
Also, updated metedata for pubmed pdf
    
### 2. data management for mbox messages
Converted mbox messages to json, and combines messages from same conversation
    
### 3. Load OPENAPI to human Language
Designed and implemented a retriever for openapi to return all cbioportal api response, 
and created a chatbot on top of it to make a human language response

### 4. Load and split mbox data     
Created a splitter for mbox, and load it to langchain.
Still working on embeddings

## Next Step:
1. Redo a data cleaning for mbox and get latest 3 yr messages, down the size to 30MB since old messages have wrong answer.
2. create embedding for mbox
3. create a docker file
4. add example questioin like GPT
    

    
