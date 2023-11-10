# -*- coding: utf-8 -*-
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name_or_path = "OPPOResearchInstitute/AndesGPT"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto", trust_remote_code=True)

# instruction mode
inputs = tokenizer('找到下列数组的中位数[3.1,6.2,1.3,8.4,10.5,11.6,2.1]，请用python代码完成以上功能', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))

# chat mode
inputs = tokenizer('Human: 找到下列数组的中位数[3.1,6.2,1.3,8.4,10.5,11.6,2.1]，请用python代码完成以上功能\n\n Assistant:', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))