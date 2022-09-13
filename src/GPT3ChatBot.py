import openai
import pyttsx3
class chatBot():
    def __init__(self, apiKey):
        openai.api_key = apiKey
        self.chatLog = ''
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', 185)
    
    def Chat(self, message, printText=True, useSound=True):
        self.chatLog += 'You: ' + message + '\n'
        response = openai.Completion.create(
                      model="text-davinci-002",
                      prompt= self.chatLog,
                      temperature=0.5,
                      max_tokens=100,
                      top_p=1.0,
                      frequency_penalty=0.5,
                      presence_penalty=0.0,
                      stop=["You:"]
                    )
        responseText = response.choices[0].text.lstrip('Friend:\n\n')
        self.chatLog += 'Friend:\n\n' + responseText + '\n'
        
        if printText:
            print(responseText)
        
        if useSound:
            self.voice.say(responseText)
            self.voice.runAndWait()
        
        return responseText
    
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
        self.chatLog = ''