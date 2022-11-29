import openai
import pyttsx3


class chatBot():
    def __init__(self, apiKey):
        openai.api_key = apiKey       
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', 185)
        self.history = []
        self.maxRowsInHistory = 42
        self.maxPromtLength = 4096
    
    def Chat(self, message, printText=True, useSound=True):
        self.history.append('You: ' + message + '\n')
        response = openai.Completion.create(
                      model="text-davinci-003",
                      prompt= self.GetChatHistory(),
                      temperature=0.5,
                      max_tokens=150,
                      top_p=1.0,
                      frequency_penalty=0.5,
                      presence_penalty=0.5,
                      stop=["You:"]
                    )        
        responseText = response.choices[0].text.lstrip('Friend:\n\n').lstrip('Bot:')
        self.history.append('Friend:\n\n' + responseText + '\n')
        
        if printText:
            print(responseText)
        
        if useSound:
            self.voice.say(responseText)
            self.voice.runAndWait()
        
        #Prune history to avoid overflow
        self.PruneHistory()
        
        return responseText

    def GetChatHistory(self):
        return ''.join(self.history)[-self.maxPromtLength:]

    def PruneHistory(self):
        while(len(self.history) > self.maxRowsInHistory):
            self.history.pop()

    
    def ListVoices(self, testVoices = True):
        currentVoiceId = self.voice.getProperty('voice')
        print(f'CurrentVoiceId: {currentVoiceId}')
        voices = self.voice.getProperty('voices')
        
        for voice in voices:
            print(f'voiceId: {voice.id}. Name: {voice.name}')
            self.voice.setProperty('voice', voice.id)
            if testVoices:
                self.voice.say('The quick brown fox jumped over the lazy dog.')
                self.voice.runAndWait()
                
        self.voice.setProperty('voice', currentVoiceId)
        return voices
        
    def SetVoice(self, voiceId):
        self.voice.setProperty('voice', voiceId)
    
    def TestVoice(self, message):
        self.voice.say(message)
        self.voice.runAndWait()
        
        
    
    def ClearChatLog(self):
        self.history.clear()
        self.chatLog = ''