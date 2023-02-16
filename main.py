import openai
from telegram.ext import *

openai.api_key = "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"

model_engine = "text-davinci-003"

API_KEY_TELEGRAM = "6043159805:AAHCzg9_IKnoDhtOAAOJhi3Jmn2MMLY_3tc"

start = input("to start press any button.. \n to suspend press x")

def message_command(update, context):
    text_from_user = str(update.message.text).lower()
    response_from_bot = response

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
    
def start_command(update, context):
    update.message.reply_text("type something and get started with lord bakul's wonderful creation!")
    
def help_command(update, context):
    update.message.reply_text("help yourself! atmnirbhar baniye!")
    
    

