class Config():
    tokenizer:str = "r50k_base"
    vocab_size:int = 50257
    d_model: int = 384
    hidden_unit: int = 2048
    context_length: int = 512
    num_heads: int = 10
    block_count: int = 6

    model_path: str = "/content/drive/MyDrive/model/llm-large.weights.h5"
    drop_out_rate = 0.1
