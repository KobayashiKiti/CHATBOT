# Running the Chat Application

This guide will help you run the chat application contained in the `index.html` file.

## Prerequisites

Ensure you have the following:

- A modern web browser (Chrome, Firefox, Safari, etc.)
- A local web server (like Python's SimpleHTTPServer, Node's http-server, etc.). Or you can use Live Server feature from VSCode
- Laptop/PC with >8GB RAM

## Start the app using Local API

1. **Download model**

Create a folder named `models`, then download `mistral-7b-openorca.Q4_0.gguf` from here <https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca> and put into the `models` folder

2. **Install llama_cpp Python**

Follow the guide here to install llama_cpp Python <https://github.com/abetlen/llama-cpp-python>

3. **Run**

*Run Python files*
Open terminal
Runfile: py index_cpp.py

*Run local server ( HTMl files)*
Run the following script to run an server locally. The server should run at port 8000

```bash
python3 -m llama_cpp.server --model "./models/mistral-7b-openorca.Q4_0.gguf" --chat_format chatml --n_gpu_layers 1
```

Run the application again. It should use localhost for local API inteference.
