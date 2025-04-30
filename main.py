import speech_recognition as sr
import pyautogui
import time
import sys


def get_audio(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print(prompt)
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                text = text.lower().strip()
                if "stop" in text:
                    print("Program terminated by command.")
                    
                    sys.exit()
                return text
            except (sr.UnknownValueError, sr.RequestError):
                continue  # silently retry

            

def main():
    print("You have 5 seconds to focus your cursor in the text editor...")
    
    time.sleep(5)

    # TITLE
    while True:
        
        title = get_audio("Speak the title:")
        
        if title == "skip":
            break
        elif title != "stop":
            pyautogui.hotkey('ctrl', 'b')
            for _ in range(4):
               pyautogui.hotkey('ctrl', 'shift', '>')
            pyautogui.write(f"{title.upper()}\n", interval=0.05)
            for _ in range(4):
               pyautogui.hotkey('ctrl', 'shift', '<')
            pyautogui.hotkey('ctrl', 'b')
            break

    # SUBTITLE
    while True:
        
        subtitle = get_audio("Speak the subtitle:")
        
        if subtitle == "skip":
            pyautogui.hotkey('tab')
            break
        elif subtitle != "stop":
            pyautogui.hotkey('ctrl', 'b')
            for _ in range(2):
               pyautogui.hotkey('ctrl', 'shift', '>')
            pyautogui.write(f"{subtitle[0].upper()+subtitle[1:]}\n", interval=0.05)
            for _ in range(2):
               pyautogui.hotkey('ctrl', 'shift', '<')
            pyautogui.hotkey('ctrl', 'b')
            pyautogui.press("tab")
            break

    # CONTENT
    print("Start speaking content. Say 'next line' to break line. Say 'stop the program' to exit.")
    
    first = True
    while True:
        
        text = get_audio("Speak:")
        
        if text == "next subtitle":
            
            while True:
               
               subtitle = get_audio("Speak the subtitle:")
               
               if subtitle == "skip":
                   pyautogui.hotkey('tab')
                   break
               elif subtitle != "stop":
                    pyautogui.write("\n", interval=0.05)
                    pyautogui.hotkey('ctrl', 'b')
                    for _ in range(2):
                      pyautogui.hotkey('ctrl', 'shift', '>')
                    pyautogui.write(f"{subtitle[0].upper()+subtitle[1:]}\n", interval=0.05)
                    for _ in range(2):
                      pyautogui.hotkey('ctrl', 'shift', '<')
                    pyautogui.hotkey('ctrl', 'b')
                    pyautogui.press("tab")
                    break
        elif text == "next line":
            pyautogui.typewrite(".")
            pyautogui.write("\n")
            pyautogui.press("tab")
            first = True
        elif text == "full stop":
            pyautogui.typewrite(".")
            first = True
        elif text == "delete":
            pyautogui.hotkey('ctrl', 'backspace')
            first = True
        elif text == "redo":
            pyautogui.hotkey('ctrl', 'y')
            first = True
        elif text == "undo":
            pyautogui.hotkey('ctrl', 'z')
        elif text == "title":
            while True:
                pyautogui.write("\n", interval=0.05)
                
                title = get_audio("Speak the title:")
                
                if title == "skip":
                  pyautogui.hotkey('tab')
                  break
                elif title != "stop":
                    pyautogui.hotkey('ctrl', 'b')
                    for _ in range(4):
                        pyautogui.hotkey('ctrl', 'shift', '>')
                    pyautogui.write(f"{title.upper()}\n", interval=0.05)
                    for _ in range(4):
                        pyautogui.hotkey('ctrl', 'shift', '<')
                    pyautogui.hotkey('ctrl', 'b')
                    break
            while True:
                subtitle = get_audio("Speak the subtitle:")
                print("Speak the subtitle:")
               
                if subtitle == "skip":
                   pyautogui.hotkey('tab')
                   break
                elif subtitle != "stop":
                    pyautogui.hotkey('ctrl', 'b')
                    for _ in range(2):
                       pyautogui.hotkey('ctrl', 'shift', '>')
                    pyautogui.write(f"{subtitle[0].upper()+subtitle[1:]}\n\n", interval=0.05)
                    for _ in range(2):
                        pyautogui.hotkey('ctrl', 'shift', '<')
                    pyautogui.hotkey('ctrl', 'b')
                    pyautogui.press("tab")
                    break
        else:
            if first:
                text = text.capitalize()
                pyautogui.write(text, interval=0.05)
                first = False
            else:
                pyautogui.write(f", {text}", interval=0.05)

if __name__ == "__main__":
    main() 