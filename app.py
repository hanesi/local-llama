from fastapi import FastAPI, Request
from llama_cpp import Llama
import os

model_path = os.getenv("MODEL_PATH", "models/llama-2-7b-chat.Q4_K_M.gguf")

# You can tune these based on the instance
llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=0  # Set >0 if you use a GPU
)

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    result = llm(prompt, max_tokens=128, temperature=0.7)
    return {"response": result["choices"][0]["text"]}
