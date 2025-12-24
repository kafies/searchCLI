from google import genai
import sys

key = "YOUR-GOOGLE-API-KEY-HERE"

client = genai.Client(api_key = key)

def chat(prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = user_input
    )

    return response.text

if __name__ == "__main__":
    while True:
        user_input = " ".join(sys.argv[1:])
        response = chat(user_input)
        print(response)
        break