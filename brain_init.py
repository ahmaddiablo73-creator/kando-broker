from ctransformers import AutoModelForCausalLM

# بارگذاری یک مدل بسیار سبک برای تست اولیه
# کاندو در حال فراخوانیِ هسته‌یِ هوشمند است
print("KANDO-CORE: INITIALIZING BRAIN...")
llm = AutoModelForCausalLM.from_pretrained("TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF", model_file="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

print(llm("What is the current trend in the market?"))