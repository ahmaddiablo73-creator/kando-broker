from ctransformers import AutoModelForCausalLM
import pandas as pd

llm = AutoModelForCausalLM.from_pretrained("TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF", model_file="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

# ۱. بارگذاری و خلاصه سازی داده‌ها به زبان ساده
data = pd.read_csv('D:\\KANDO-CORE\\ACCOUNTING\\ledger.csv')
summary = data.tail(5).to_string()

# ۲. دستورِ صریح (System Prompt) برای جلوگیری از تولید کد
prompt = f"""
You are a financial analyst for KANDO-CORE. 
Here is the latest data:
{summary}

Act as an expert. Do NOT write code. 
Give a 3-sentence summary of the financial performance and one actionable recommendation.
"""

report = llm(prompt)
print(report)