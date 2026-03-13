# example.py
from synstar import chat

# Auto-select the cheapest model that can handle your task
prompt = "Explain artificial intelligence in simple terms."
response = chat(prompt, optimize_for="cost")  # or "performance"

print(f"Model used: {response.model}")
print(f"Estimated cost: ${response.estimated_cost:.4f}")
print(response.content)
