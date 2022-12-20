import os
import openai

openai.api_key = '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'

def oai_questions(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  result = response.get('choices')[0].get('text')
  return result
print(oai_questions('air ticket price from dhaka to sydny,AU in bdt'))