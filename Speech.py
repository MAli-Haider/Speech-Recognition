import tkinter as tk
import speech_recognition as s
import random
import threading

def main():
    
    HEIGHT = 600
    WIDTH = 800

    root = tk.Tk()
    
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    
    background_image = tk.PhotoImage(file='background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    
    frame = tk.Frame(root, bg='#80c1ff',  bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)
    
    def s2t():
        
        r = s.Recognizer()

        with s.Microphone() as source:
            
                print('Speak Anything :')
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    print(text)
                
                except:
                    print('Sorry could not recognize your voice')
                
                label = tk.Label(lower_frame,text="You said : "+str(text), font=60)
                label.place(relwidth=1, relheight=1)
                
                with open("recorded.wav", "wb") as f:
                    f.write(audio.get_wav_data())
    
    button = tk.Button(frame,command=s2t, text="Speak", font=40)
    button.place(relx=0.7, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='#80c1ff',  bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6,  anchor='n')
    
    label = tk.Label(lower_frame,text="Press Speak", font=70 )
    label.place(relwidth=1, relheight=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()
