import openai

openai.api_key = "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"

model_engine = "text-davinci-003"



start = input("to start press any button.. \n to suspend press x")
while start != "x":
    prompt = input("you >>")
    
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    response = completion.choices[0].text
    print(response)

    if prompt == "exit":
        break