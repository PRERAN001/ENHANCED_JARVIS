import requests
from bs4 import BeautifulSoup
GROQ_API_KEY = "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"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
import re
## clean responsse code is of gpt bcs the ask_groq functionn was returning random shit so i wanted to clean the response
def clean_response(text):
    # Remove code blocks, markdown symbols, extra spaces, etc.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)  # remove code blocks
    text = re.sub(r"[*_`#>-]", "", text)  # remove markdown formatting
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    text = re.sub(r"[^\x00-\x7F]+", "", text)  # remove non-ASCII characters (if TTS struggles)
    text = text.strip()
    return text

def brave_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://search.brave.com/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for result in soup.find_all("div", class_="snippet"):
        snippet_text = result.get_text()
        results.append(snippet_text)

    return results[:3]  
def ask_groq(question):
    headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

    json_data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {
            "role": "system",
            "content": (
                f"answer only to this  {question} dont give unnecessay answers"
            )
        },
        {
            "role": "user",
            "content": f"{question}"
        }
    ]
}
    response = requests.post(GROQ_ENDPOINT, headers=headers, json=json_data)
    response.raise_for_status()
    raw_output = response.json()['choices'][0]['message']['content']
    return clean_response(raw_output)

