---
layout: post
title:  "Week Twelve | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Improve the accuracy of chatbot
Updated the route logic by add one more all_chain call when study call found nothing

Cleaned databases by deleting all the chunks less than 100 characters

### 2. Updated the evalution test
Added data source in evaluation questions, and asked chatbot to only return one letter of option
Ran the 100 questions test again, gain 82/100
Also, generated 100 new MC questions, and gain 79/100.
Convert the result in CSV file.
    
### 3. Create a Langchain Pull Request
Add a pubmed integration at Langchain. Need some adjusting.

Link: https://github.com/langchain-ai/langchain/pull/25368

### 4. Train chatbot to make plots
Trained chatbot to make scatter, bar, and pie chart. 

Link: https://github.com/cannin/gsoc_2024_cbioportal_chatbot/issues/21
    

## Next step:
1. create a download button for data analysis chatbot
2. deep analyze how wrong the incorrect questions were
3. modify docker instruction and readme(how to add docs, how to extract embeddings)    
4. continue working on Langchain PR
5. read SCLC papers
   
    
