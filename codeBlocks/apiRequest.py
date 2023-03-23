import openai as ai
ai.api_key = "*********************"

text = "<Aquí va la pregunta>"

response = ai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0.1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response
response.choices[0].text