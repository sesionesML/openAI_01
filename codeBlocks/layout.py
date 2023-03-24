import openai

def call(input, engine = 'text-davinci-003', stored = False):
    #getAccess()
    openai.api_key = "#####" 

    response = openai.Completion.create(
        model= engine,
        #getContext()
        prompt="########",
        temperature=0.6,
        max_tokens = 256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = response.choices[0].text
    #if stored: getSave()
    return (response)