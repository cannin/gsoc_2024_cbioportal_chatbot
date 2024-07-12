---
layout: post
title:  "Week Seven | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Solved the issue of mbox embedding DB is too large
Wrote a script to export ChromaBD into csv file
Deleted embedding queue in mbox embeddingDB

### 2. Create a docker file
Created a docker file for cBioPortal Chatbot

### 3. Add example questions
Added example questions in UI, click the question will autofill the input box

### 4. Catch error in OPENAPI chatbot
For openapi chatbot, if no keywords found in user query, it will return all the studies, which is too large.
Catched this error, and send user a message to try other keywords

## Next Step:
1. combine mbox embeddings with others
2. use route logic to combine chatbots
3. create a new docker for it
