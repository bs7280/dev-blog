---
id: x8y1lrveef8qxz1zsdt0pbd
title: Alfred ChatGPT Workflow with Local Models
desc: ""
created: 1712957645368
updated: 1712957645368
---
Recently Alfred version 5.5 was released which includes new UI elements and a cool chatgpt interface.  By default this requires a paid chatgpt account to work, and you may want to use an alternative model for a variety of reasons such as:
- Cost
- Privacy
- Running models without gaurdrails
- Enhanced Customization

## Setup Ollama

[Ollama](https://ollama.com/) is an open source tool to download and run LLMs on your own machine. 

1. Download the installer from [Ollama](https://ollama.com/)
2. Run the installer
3. in a terminal run: `ollama run llama2`
	- This will download the model file, which is about 4.2 GB, the first time you run it. 
	- An interactive prompt should open, ask it any question.


From here, you can run many different models, see [Ollama Model Library](https://ollama.com/library) for more. Ex - to install [mistral](https://ollama.com/library/mistral) do  `ollama pull mistral`

### Make sure API is working

**This step is optional, but if you run into trouble its an helpful debugging step.**

*Note* you can also just paste `http://localhost:11434/` into the browser, you should get "Ollama is running"

Before we configure Alfred, we need to make sure that our local LLM is working correctly by making an API call to the locally running server. For more information check out [OpenAI compatibility · Ollama Blog](https://ollama.com/blog/openai-compatibility)

In a terminal paste this command:

```
❯ curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "llama2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```

you should see something like this:

```json
{
	"id": "chatcmpl-491",
	"object": "chat.completion",
	"created": 1712957914,
	"model": "llama2",
	"system_fingerprint": "fp_ollama",
	"choices": [
		{
			"index": 0,
			"message": {
				"role": "assistant",
				"content": "Hi there! *smiling* It's nice to meet you. How can I assist you today? Do you have any questions or tasks you need help with?"
			},
			"finish_reason": "stop"
		}
	],
	"usage": {
		"prompt_tokens": 0,
		"completion_tokens": 35,
		"total_tokens": 35
	}
}
```

## Configure the ChatGPT Alfred Workflow

If you haven't already, install the [Alfred ChatGPT / DALL-E Workflow](https://alfred.app/workflows/alfredapp/openai/), if you are only interested in running it with local models, you can skip the API key step. 

Now find the environmont variable customization pane by clicking the button that looks like `{ X } `

Open workflow configuration
![Pasted image 20240412165809.png]({{< ref "Pasted image 20240412165809.png" >}})

Go to the Environment Variables tab and change the values for:
- `chatgpt_api_endpoint` to `http://localhost:11434`
- `chatgpt_model_override` to `llama2`
	- This is the model we downloaded above, you can change this to other models you download locally.

Example:
![Pasted image 20240412165952.png]({{< ref "Pasted image 20240412165952.png" >}})

Now try to run the workflow...
## Result

If you trigger the workflow and ask **"Who are you"** you should get a response like this:

##### Who are you
> I'm LLaMA, an AI assistant developed by Meta AI that can understand and respond to human input in a conversational manner. I'm here to help you with any questions or topics you'd like to discuss! Is there something specific you'd like to talk about or ask?

Success!
## Customizing

You can now either continue to use the workflow as is or swap in another model. If you wanted to use an llm for coding you could:
- open the terminal and run `ollama pull codellama`

Then update the `chatgot_model_override` above to `codellama` and ask the workflow a python question
