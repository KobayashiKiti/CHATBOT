# Running the Chat Application

This guide will help you run the chat application contained in the `index.html` file.

## Prerequisites

Ensure you have the following:

- A modern web browser (Chrome, Firefox, Safari, etc.)
- A local web server (like Python's SimpleHTTPServer, Node's http-server, etc.). Or you can use Live Server feature from VSCode
- An API key from OpenAI for API access. Or a laptop/PC with >8GB RAM

## Start the app using Local API

1. **Download model**

Create a folder named `models`, then download `mistral-7b-openorca.Q4_0.gguf` from here <https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca> and put into the `models` folder

2. **Install llama_cpp Python**

Follow the guide here to install llama_cpp Python <https://github.com/abetlen/llama-cpp-python>

3. **Run local OpenAI server**

Run the following script to run an OpenAI API server locally. The server should run at port 8000

```bash
python3 -m llama_cpp.server --model "./models/mistral-7b-openorca.Q4_0.gguf" --chat_format chatml --n_gpu_layers 1
```

4. **Update chat application code**

Open the `index.html` file and locate the following line

```html
  // Real GPT
  // const OPEN_AI_ENDPOINT = 'https://api.openai.com/v1' // Comment this line

  // Security, do not deploy this in production
  const chatGPTKey = 'sk-*****'; // Create an API key from here

  // Local GPT
  const OPEN_AI_ENDPOINT = 'http://localhost:8000/v1' // Uncomment this line
```

Run the application again. It should use localhost for local API inteference.
