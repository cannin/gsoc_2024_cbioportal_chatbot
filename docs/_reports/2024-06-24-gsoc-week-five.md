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
### Add all metaData for pubmed papers
Created a default dictionary for each paper and append metadatas. Write a function to add metadata in loader.

### Load PDF of pmc papers
loaded 26 pdf papers and add metadatas for each paper.

### self-query retriever
Used and test self-query retriever, the responses were very good. It can support keywords like pmid/pmcid/studyid and so on.

### Created a PR to add pmid
Created a pr to add 5 missing pmid. And the pr is merged

## Next Step
1. create embeddings and merge all datasets
2. create a docker image
3. create a instruction page to deploy chatbot project
