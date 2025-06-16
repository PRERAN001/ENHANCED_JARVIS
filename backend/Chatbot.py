import datetime
import random

def general_quries(querry):
    

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer show up late to work? It had a hard drive!",
        "Why was the math book sad? Because it had too many problems.",
        "Parallel lines have so much in common... it's a shame they'll never meet."
    ]
    user_input = querry

    if user_input == 'bye':
        return(" Goodbye!")

    elif 'hello' in user_input or 'hi' in user_input:
        return("Hello there!")

    elif 'how are you' in user_input:
        return("I'm just a bunch of code, but I'm doing great!")

    elif 'your name' in user_input:
        return("I'm ChatBot, your friendly assistant.")

    elif 'who created you' in user_input:
        return("No one created me, haha. I just popped into existence! siuuuuuuuuuuuuuuuuuuuuuu")

    elif 'my age' in user_input:
         return("I'd guess you're 19. Just a lucky guess!")

    elif 'time' in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return(f"The current time is {current_time}.")

    elif 'date' in user_input or 'today\'s date' in user_input:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return(f"Today's date is {current_date}.")

    elif 'day of the week' in user_input or 'what day is it' in user_input:
        day_name = datetime.datetime.now().strftime("%A")
        return(f"Today is {day_name}.")

    elif 'joke' in user_input:
        return(f" {random.choice(jokes)}")

    elif 'weather' in user_input:
        return("It's always sunny in code world!")

    elif 'thank you' in user_input or 'thanks' in user_input:
        return("You're welcome!")

    elif 'favourite color' in user_input or 'favorite color' in user_input:
        return("I like blue – reminds me of the terminal screen!")

    elif 'favourite food' in user_input or 'favorite food' in user_input:
        return("Binary bites and code crunchers 😄")

    else:
        return("ChatBot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    general_quries()
