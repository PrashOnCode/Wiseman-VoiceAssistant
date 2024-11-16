from openai import OpenAI
  
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="<API Key Here>",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named wiseman skilled in general tasks like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(completion.choices[0].message.content)