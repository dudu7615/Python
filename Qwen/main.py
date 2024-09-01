from pathlib import Path
import os
import gc
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from transformers.trainer_utils import set_seed
from config import Config

model_dir = Path(__file__).parent / "Qwen-1_8B-Chat"
modelConfig = Config(
    path=model_dir,
    seed=1234,
    cpu_only=False,
)


def loadModel(args: Config):
    tokenizer = AutoTokenizer.from_pretrained(
        args.path,
        trust_remote_code=True,
        resume_download=True,
    )

    device_map = "cpu" if args.cpu_only else "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.path,
        device_map=device_map,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    config = GenerationConfig.from_pretrained(
        args.path,
        trust_remote_code=True,
        resume_download=True,
    )

    return model, tokenizer, config


def clear():
    os.system("cls")


def gcer():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def printHistory(history):
    for query, response in history:
        print(f"User: {query}")
        print(f"Qwen: {response}")
        print("")


def main():
    history, response = [], ""

    model, tokenizer, config = loadModel(modelConfig)

    seed = modelConfig.seed

    set_seed(seed)
    # clear()

    while True:
        query = input("\nUser> ").strip()

        # Run chat.

        try:
            for response in model.chat_stream(
                tokenizer, query, history=history, generation_config=config
            ):
                clear()
                printHistory(history)
                print(f"\nUser: {query}")
                print(f"Qwen: {response}")
        except KeyboardInterrupt:
            print("[WARNING] Generation interrupted")
            continue

        history.append((query, response))


if __name__ == "__main__":
    main()
