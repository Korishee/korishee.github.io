import os
from groq import Groq

# Run the pip install command
os.system("pip install groq requests")

# Set your API key directly for simplicity
api_key = "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"  # Replace with your actual key

# Initialize the Groq client
client = Groq(api_key=api_key)

while True:
    # Ask the user for their input
    user_query = input("Enter your query (or type 'exit' to quit): ")

    if user_query.lower() == 'exit':
        print("Exiting...")
        break

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

    # Get the response from the API
    response_content = chat_completion.choices[0].message.content

    # Print the response to the console
    print("Response:", response_content)

    # Save the response to a file
    with open("response.txt", "a") as file:
        file.write(f"Query: {user_query}\n")
        file.write(f"Response: {response_content}\n\n")
