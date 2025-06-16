import re
import webbrowser
from Automation import automation
from Chatbot import general_quries
from Realtimesearchengine import ask_groq, brave_search
from TextTospeech import txt_to_speak
from vs_automation import vs_code_sasta_automation, generate_code
from whatsapp_automation import whatsapp_sasta_automation
from youtube_automation import youtube_sasta_automation
from trying_to_make_ppt import generate_content_for_ppt, sasta_ppt_maker
from speech_to_text import listen_and_convert
print("hwellllllllllllllllllllllllllll")
text = "time"

general_pattern = r"\b(hello|hi|thanks|goodbye|bye|introduce|joke|name|date|time|fact|space|explain|describe|define|mean|meaning|info|information|question|ask)\b"
automation_pattern = r"\b(open|launch|start|begin|initiate|close|shut|turn|on|off|play|stop|pause|resume|call|dial|message|text|email|remind|set|schedule|create|make|run|search|navigate|go|find|install|uninstall|delete|send|post)\b"
realtime_pattern = r"\b(weather|temperature|forecast|humidity|air|quality|pollution|price|rate|value|stock|market|today|now|current|news|headlines|traffic|covid|cases|score|match|matches|exchange|convert|currency|bitcoin|crypto|population|sunrise|sunset|trending|live|update|event|events|happening|ongoing|stats|statistics|standing|rank|ranking|winner|result|results|ipl|election|vote|alert|signal|data|how|what|who|when|why|where)\b"

vs_automation_pattern = r"create\s+(?:a\s+)?folder\s+of\s+name\s+(\w+)\s+and\s+file\s+name\s+([\w\.]+).*?generate\s+a\s+code\s+for\s+(.+)"
ppt_format = r"generate\s+a\s+ppt\s+on\s+topic\s+(.+?)\s+and\s+save\s+it\s+as\s+(\w+)"
whatsapp_pattern = r"whatsapp\s+and\s+send\s+message\s+to\s+(\w+)\s+saying\s+(.+)"
youtube_pattern = r"youtube\s+and\s+search\s+for\s+(.+)"
sasta_search_optimization = r"\b(open|launch|start)\s+(\w+)(?:\s+(?:and\s+)?search\s+for\s+(.+))?"

executed = False

if match := re.search(vs_automation_pattern, text, re.IGNORECASE):
    foldername, filename, task = match.groups()
    code = generate_code(task)
    vs_code_sasta_automation(foldername, filename, code)
    executed = True

elif match := re.search(ppt_format, text, re.IGNORECASE):
    topic, filename = match.groups()
    filename += ".pptx"
    titles, contents, images = generate_content_for_ppt(topic)
    sasta_ppt_maker(filename, titles, contents)
    executed = True

elif match := re.search(whatsapp_pattern, text, re.IGNORECASE):
    whatsapp_sasta_automation(*match.groups())
    executed = True

elif match := re.search(youtube_pattern, text, re.IGNORECASE):
    youtube_sasta_automation(match.group(1))
    executed = True

elif match := re.search(sasta_search_optimization, text, re.IGNORECASE):
    app, _, query = match.groups()
    if app and query:
        webbrowser.open(f"https://www.{app}.com/results?search_query={query}")
        executed = True

if not executed:
    chunks = re.split(r"\b(?:and then|then|also|finally|after that|and)\b", text, flags=re.IGNORECASE)
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    general, automation_tasks, realtime = [], [], []

    for chunk in chunks:
        g = len(re.findall(general_pattern, chunk))
        a = len(re.findall(automation_pattern, chunk))
        r = len(re.findall(realtime_pattern, chunk))

        if r >= g and r >= a:
            realtime.append(chunk)
        elif a >= g and a >= r:
            automation_tasks.append(chunk)
        else:
            general.append(chunk)

    for task in general:
        result = general_quries(task)
        txt_to_speak(result)

    for task in automation_tasks:
        automation(task)

    for task in realtime:
        search_result = brave_search(task)
        final_answer = ask_groq(search_result)
        txt_to_speak(final_answer)
