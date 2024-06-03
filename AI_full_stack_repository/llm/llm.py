from langchain.llms import CTransformers
import box
import yaml
from langchain.llms import LlamaCpp
config={'max_new_tokens': 2000,
        'temperature': 0.01,
        "context_length" : 4000}
# Import config vars
with open('config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


def setup_llm():
    # llm = CTransformers(model=cfg.MODEL_BIN_PATH,
    #                     model_type=cfg.MODEL_TYPE,
    #                     max_new_tokens=cfg.MAX_NEW_TOKENS,
    #                     temperature=cfg.TEMPERATURE
    # )
    llm = LlamaCpp(
    streaming = True,
    model_path=cfg.MODEL_BIN_PATH,#"mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    temperature=0.75,
    top_p=1, 
    verbose=True,
    n_ctx=4096
    )
    

    return llm
