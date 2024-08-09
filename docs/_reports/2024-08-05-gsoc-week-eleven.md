---
layout: post
title:  "Week Eleven | Welcome GSoC"
tags: gsoc
author: Xinling Wang
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2024/projects/5PYvMkWW)
- [Work Repository](https://github.com/cannin/gsoc_2024_cbioportal_chatbot)

## Tasks
### 1. Evaluation of chatbot
Used ChatGpt to generate 100 questions for docuemntation and mailing lists.
Wrote a script to ask cbioportal chatbot evaluation questions.

### 2. Add topic
Add chain used in each response

### 3. Update Chat history
Updated chat history in sliding window, removing old messages.

### 4. Add API endpoints
Add /api/studies/{studyId}/samples, /api/studies/{studyId}/tags, /api/studies/{studyId}, and /api/studies/{studyId}/samples/{sampleId}:

## Next Step:
1. analyze evaluation test, improving route logic
2. try conversation summary for chat history
3. continue working on langchain PR
4. try lite llm
5. clean database, especially short chunks
