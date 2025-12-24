import openai
import sys

key = "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"

openai.api_key = key

def chat(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4.1-mini",
        message = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = " ".join(sys.argv[1:])
        break
        
        response = chat(user_input)
        print(response)
