import speech_recognition as sr

def listen_and_convert(audio,timeout=5, phrase_time_limit=7):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Please speak now.")
        
        try:
            
            text = recognizer.recognize_google(audio)
            print("✅ You said:", text)
            return text
        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"⚠️ Could not request results from Google STT; {e}")
            return None
listen_and_convert()