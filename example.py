"""
AI Cost Optimizer Example

A minimal example demonstrating how a developer might
experiment with LLM usage in a simple application.
"""

from synstar import chat

prompt = "Explain artificial intelligence in simple terms."

response = chat(prompt)

print("Prompt:")
print(prompt)

print("\nResponse:")
print(response)
