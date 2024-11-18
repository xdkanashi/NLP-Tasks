from transformers import AutoTokenizer, AutoModelForCausalLM
from deep_translator import GoogleTranslator
from langdetect import detect #pip install transformers deep-translator langdetect 

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def complete_text(input_text, max_length=80):
    detected_language = detect(input_text)

    if detected_language != 'en':
        translation = GoogleTranslator(source=detected_language, target='en').translate(input_text)
    else:
        translation = input_text

    input_ids = tokenizer.encode(translation, return_tensors="pt")

    output_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        temperature=0.7,  
        top_p=0.9,       
        no_repeat_ngram_size=2  
    )
    
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    if detected_language != 'en':
        translated_generated_text = GoogleTranslator(source='en', target=detected_language).translate(generated_text)
        return translated_generated_text
    else:
        return generated_text

if __name__ == "__main__":
    text = "Reiz kādā tālā zemē"
    completed_text = complete_text(text)
    print("Ģenerēts teksts:")
    print(completed_text)