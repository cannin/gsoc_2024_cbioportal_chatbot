---
layout: post
title:  "Week Zero | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks

 ### 1. Test GPT Endpoints
 Brief: Deleted the elastic search database, and used the Chroma vector database instead.Tried both Azure gpt-3.5-turbo-instruct and Azure gpt-4 for LLM and embeddings. 


 ### 2.  Download All Markdown Documents for cBioPortal
 Brief: Downloaded  and loaded all the markdown documents locally. The quantity of md documents is 81. 
	

 ### 3.  Access cBioPortal Group mBox
 Brief: Downloaded mBox messages. It includes Google group conversations and cBioportal news.
 
 Comment: cBioportal news can also be helpful to build chatbot.


 ### 4.  Pipeline to Load PDFs into Embedding DB
 Brief: PDFs are located in the tutorials  folder in the documentation site.  Wrote a PDF_loader class to load both text and image from pdf. Also added metadata like url for each pdf.
 
 Comment: In cBioportal website, pdfs don’t have individual urls. There is one     url containing all the pdfs: https://docs.cbioportal.org/user-guide/overview/ 
    Alternative way is using urls in github which has individual url for each pdf:     https://github.com/cBioPortal/cbioportal/tree/master/docs/tutorials 


 ### 5.  Add Used Documents to Demo
 Brief: Wrote an advanced markdown_loader class to load, split and add metadata, such as url. Rewrote the prompt to ask the chatbot to return the url of data retrieved in response. Tried this function on a small md folder, and it was working. 



 ## Next step:
1. Try “Add Used Documents to Demo” on all the markdown files and make a list of docs which can generate responses using retrieved text.
2. Test LangChain ability to use cBioPortal API
3. Load Mbox packages 
