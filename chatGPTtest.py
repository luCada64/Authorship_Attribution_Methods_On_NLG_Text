from openai import OpenAI

# To run this code you must create a .py file with a global varabile named "OPENAI_API_KEY"
# This variable must contain you're OpenAI API ley
# documentation: https://platform.openai.com/docs/introduction
from chatgptApiKey import OPENAI_API_KEY


# Create a client for openAI chatGPT
client = OpenAI(api_key=OPENAI_API_KEY)


# Let's access the clients
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)