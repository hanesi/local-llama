from llama_cpp import Llama

llm = Llama(
    model_path="./models/llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=20
)

response = llm("Q: What is the capital of France?\nA:", max_tokens=100)
print(response["choices"][0]["text"])
