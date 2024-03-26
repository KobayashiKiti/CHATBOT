from llama_cpp import Llama

llm = Llama(model_path="./models/mistral-7b-openorca.Q4_0.gguf",
            n_gpu_layers=1, n_ctx=4096)

output = llm.create_completion("""<|im_start|>system
You are a helpful chatbot.
<|im_end|>
<|im_start|>user
how the weather today <|im_end|>
<|im_start|>assistant""", max_tokens=500,  stop=["<|im_end|>"], stream=True)

for token in output:
    print(token["choices"][0]["text"], end='', flush=True)


pip install  uvicorn
pip install  starlette
pip install  fastapi
pip install sse_starlette
pip install starlette_context 
pip install pydantic_settings