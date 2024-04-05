---
id: hu23xt22xmbpk4lj8vr1frv
title: llama-cpp-json-formatting
desc: ""
created: 1712353924207
updated: 1712353924207
date: 2024-04-05
---
One cool feature in llama.cpp is the ability to provide a grammer from the LLM output, which has some powerful implications. This post is meant to show some examples of my work [messing with python and llama.cpp grammars](https://github.com/bs7280/py-llama-cpp-examples)

## Format LLM response with a given JSON schema

Lets say I want to generate API calls for a given prompt. I can define a JSON schema like this:

```python
schema = '''
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Name and Age API",
    "description": "An API that accepts a name and age as input parameters.",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the person."
        },
        "age": {
            "type": "integer",
            "description": "The age of the person."
        }
    },
    "required": ["name", "age"]
}'''
```

Which requires a string and integer fields "Name" and "Age".

Using a few lines of code and the llama_cpp python library we can make a call to the mistral-7b model

```python
from llama_cpp.llama import Llama, LlamaGrammar
import json

grammar = LlamaGrammar.from_json_schema(schema)
llm = Llama("mistral-7b-instruct-v0.1.Q4_K_M.gguf")

prompt = "Give me an API spec for a 28 year old named Ben"

response = llm(
    prompt,
    grammar=grammar, max_tokens=-1
)

print(response)
```

which outputs

```json
{
    "name": "Ben",
    "age": 28
}
```

## Implications
This is a very simple example but it has a lot of power and potential as both a development and scripting tool. 

Some ideas:
- Generate API requests based on a rough description or email
- Append to a SQL table
- make the model choose from a set of possible answers