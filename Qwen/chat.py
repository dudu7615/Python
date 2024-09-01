from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig
from pathlib import Path
from config import Config
import os
import sys


model_dir = Path(r"Qwen\Qwen-1_8B-Chat")
# model_dir = Path(r"Qwen\Qwen-1_8B-Chat-Int4")
modelConfig = Config(
    path=model_dir,
    seed=1234,
    cpu_only=False,
)


# 可选的模型包括: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained(modelConfig.path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    modelConfig.path, device_map="auto", trust_remote_code=True, fp16=True
).eval()

model.generation_config = GenerationConfig.from_pretrained(
    modelConfig.path, trust_remote_code=True
)
# model.generation_config.temperature = 1.0
# model.generation_config.top_k = 10
# model.generation_config.top_p = 0.9

history = []
resp: str = ""
os.system("cls")
while True:
    question = input("User> ").strip()
    lastResp = ""
    print("Qwen> ", end="")
    for resp in model.chat_stream(tokenizer, question, history=history):
        print(resp.replace(lastResp, ""), end="")
        sys.stdout.flush()
        lastResp = resp
    history.append((question, resp))
    print("\n\n")
