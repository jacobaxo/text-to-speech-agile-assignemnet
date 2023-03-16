import tkinter as tk
from gtts import gTTS
from playsound import playsound
class texttospeech:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("text to speech")
        
        self.text_input = tk.Entry(self.window, width=50)
        self.text_input.pack()

        self.read_button = tk.Button(self.window, text="read", command=self.read_text)
        self.read_button.pack()
        
        self.clear_button = tk.Button(self.window, text="clear", command=self.clear_text)
        self.clear_button.pack()
        
        self.window.mainloop()
    
    def read_text(self):
        text = self.text_input.get()
        speech = gTTS(text)
        speech.save("story.mp3")
        playsound("story.mp3")
    def clear_text(self):
        self.text_input.delete(0, tk.END)
texttospeech()