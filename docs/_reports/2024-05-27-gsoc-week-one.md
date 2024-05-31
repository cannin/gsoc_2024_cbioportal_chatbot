---
layout: post
title:  "Week One | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Test "Add Used Documents to Demo " on all the markdown files
  test markdown files returning the retrieve data's url in chatbot response, and make a list of it. 
  
### 2. Write Mbox loader and load Mbox data
   write a mbox loader, and load both google group conversation and cBioportal news
   
### 3. Test LangChain and OpenAPI Specs
  build a openapi_chain to ask questions about data from cBioPortal's API
  
  Comment: The api is too long for Openapi_chain, so will use two endpoints, getAllstudiesUsingGET and getSamplesBykeywordsUsingGET 

## Next Step
1. Use pip env 
2. write/contribute pubmed loader in langchain
3. Using first 5 messages from mbox to train chatbot
  
  

   
  
