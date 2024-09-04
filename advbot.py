import os
from groq import Groq

# Set your API key directly for simplicity
api_key = "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"  # Replace with your actual key

# Initialize the Groq client
client = Groq(api_key=api_key)

# Initialize conversation history
conversation_history = []

while True:
    # Ask the user for their input
    user_query = input("Enter your query (or type 'exit' to quit): ")

    # Exit the loop if the user types 'exit'
    if user_query.lower() == 'exit':
        break

    # Add user message to the conversation history
    conversation_history.append({
        "role": "user",
        "content": user_query,
    })

    # Create a chat completion request with conversation history
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama3-8b-8192",  # Specify the model
    )

    # Extract and print the response
    response_content = chat_completion.choices[0].message.content
    print("Response:", response_content)

    # Add the model's response to the conversation history
    conversation_history.append({
        "role": "assistant",
        "content": response_content,
    })
