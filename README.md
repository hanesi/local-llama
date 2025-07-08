First run these commands to create a virtual environment:

```
python3.12 -m venv llama-env
source llama-env/bin/activate
pip install --upgrade pip
```

Then install llama C++ backend with python bindings:

```
pip install llama-cpp-python \
  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/metal
```

Next, create a models folder and download from HF:

```
mkdir models && cd models
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
cd ..
```

Run the test_app.py script to confirm installation:

```
python test_app.py
```

To run the real app, use uvicorn:

```
uvicorn app:app --reload
```

if you get a llama-cpp module not found error with the above command, update the path:

```
export PATH="/Users/ianhanes/Documents/GitHub/local-llama/llama-env/bin:$PATH"
```