import openai

openai.api_key = "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"
command = input('Enter your query: ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=command,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
reply = response.get('choices')
text = reply[0].get('text')
print(text)