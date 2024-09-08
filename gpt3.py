import requests
import json

# Replace with your OpenRouter API key
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

def get_user_input():
    return input("Enter your message (or type 'exit' to quit): ")

def make_api_request(message):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    payload = {
        'model': 'openai/gpt-3.5-turbo',
        'messages': [
            {'role': 'user', 'content': message}
        ],
        'max_tokens': 500  # Increased token limit
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def save_response_to_file(content):
    with open("response.html", "w") as file:
        file.write(content)
    print("Response saved to response.html")

def main():
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'exit':
            print("Exiting the program.")
            break
        
        response = make_api_request(user_message)
        
        # Print the full response for debugging
        print("Full API Response:")
        print(json.dumps(response, indent=4))
        
        # Attempt to extract and print the response content
        try:
            choices = response.get('choices', [])
            if choices:
                content = choices[0].get('message', {}).get('content', 'No content found.')
                # Save content to a file
                save_response_to_file(content)
            else:
                print("No choices found in response.")
        except Exception as e:
            print("Error processing response:", e)
            print("Full response:", response)

if __name__ == "__main__":
    main()
