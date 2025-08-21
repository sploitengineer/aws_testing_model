from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def model_fn(model_dir):
    # Load tokenizer and model from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it")
    model = AutoModelForCausalLM.from_pretrained("google/gemma-2-2b-it")
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

def predict_fn(data, model_pipeline):
    prompt = data.get("prompt", "")
    result = model_pipeline(prompt, max_length=256, do_sample=True)
    return {"output": result[0]["generated_text"]}
