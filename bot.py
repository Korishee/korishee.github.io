import os

# Run the pip install command
os.system("pip install groq requests")

import os
from groq import Groq

# Set your API key directly for simplicity
api_key = "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"  # Replace with your actual key

# Initialize the Groq client
client = Groq(api_key=api_key)

while True:

# Ask the user for their input
  user_query = input("Enter your query: ")

# Create a chat completion request
  chat_completion = client.chat.completions.create(
      messages=[
        {
            "role": "user",
            "content": user_query,
        }
    ],
      model="llama3-8b-8192",  # Specify the model
)

# Print the response from the API
  print("Response:", chat_completion.choices[0].message.content)
