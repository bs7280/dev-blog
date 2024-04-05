---
id: swesvovvgi6025samudgiq7
title: Creating blog posts from obsidian notes
desc: ""
created: 1705363902269
updated: 1705363902269
date: 2024-01-17
---

I wanted to keep this as simple and cheap as possible. I write blog posts in a specific spot in my obsidian notes, and they get published to a netlify app. 

## Implementation

I found this cool project [devidw/obsidian-to-hugo: Process Obsidian notes to publish them with Hugo](https://github.com/devidw/obsidian-to-hugo) which lets you create a static site from markdown. It worked great but I had to modify it to support a few requirements specific to my note system. 

- grab notes from my obsidian vault that are eligible as posts (`prj.devblog.posts.*`) and pull them into my dev-blog repo
- Remove unused files
- Add linked files like images and move them somewhere they can be rendered

## Build 
`pyscripts/export_obsidian.py`

## Test 

run:
`hugo server`

then view the site at lhttp://localhost:1313/

## Publish

