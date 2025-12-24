import openai

key = "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"

openai.api.key = key

def chat(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4.1-mini",
        message = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat(user_input)
        print(response)
