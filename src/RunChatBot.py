import GPT3ChatBot
import config

print('Starting things up...')
print(f'API Key set is: {config.api_key}')
try:
    print('Write your question. Enter to continue. Ctrl-c to quit.')
    while True:
        text = input()
        print(f'You wrote: {text}')
except KeyboardInterrupt:
    pass

print('Chatbot terminated...')