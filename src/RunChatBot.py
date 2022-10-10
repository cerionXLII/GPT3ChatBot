from GPT3ChatBot import chatBot
import config #Add a local file called config.py and set the variable api_key = "YOUR API KEY"

apiKey = config.api_key
print('Starting things up...')
chatBot = chatBot(apiKey)
voices = chatBot.ListVoices(False)
chatBot.SetVoice(voices[1].id)

try:
    print('Write your question followed by enter. Ctrl-c to quit.')

    while True:
        text = input()
        chatBot.Chat(text)        

except KeyboardInterrupt:
    pass

print('Chat bot terminated...')
