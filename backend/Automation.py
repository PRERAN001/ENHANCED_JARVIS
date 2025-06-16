from AppOpener import open
import webbrowser
import shutil
common_websites = [
    "google",
    "youtube",
    "facebook",
    "instagram",
    "twitter",
    "linkedin",
    "github",
    "stackoverflow",
    "amazon",
    "flipkart",
    "wikipedia",
    "netflix",
    "gmail",
    "reddit",
    "quora",
    "microsoft",
    "apple",
    "zoom",
    "whatsapp",
    "spotify"
]
actual_website_names=[]
def automation(task):
    seperated_words=task.lower().split()
    if "open" in seperated_words:
            word_open=seperated_words.index("open")
            website_names=seperated_words[word_open+1:len(seperated_words):]
            for i in website_names  :
                if i in common_websites: 
                    actual_website_names.append(i)
            for i in actual_website_names:
                open(i)
                webbrowser.open(f"https://{i}.com")
    else:
        print("no websites were asked to open")


   

