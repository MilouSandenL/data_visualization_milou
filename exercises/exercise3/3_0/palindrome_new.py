from taipy.gui import Gui
import taipy.gui.builder as tgb

user_input = ""
result_text = ""
score = 0
last_result = ""
history = []
string_history = ""
image_url = ""

def is_palindrome(text):
    clean = ''.join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

def check_palindrome(state):
    user_text = state.user_input.strip()
    
    if not user_text:
        state.result_text = "Skriv något först!"
        return

    state.result_text = f"Du skrev: '{user_text}'"
    
    if is_palindrome(user_text):
        state.score += 1
        state.last_result = "✅ +1 poäng"
        state.image_url = "assets/fake_cat.png"
        icon = "⭐"
    else:
        state.score -= 1
        state.last_result = "❌ -1 poäng"
        state.image_url = "assets/fake_sad_rabbit.png"
        icon = "💔"

    state.history.append(f"{icon} {user_text}")
    state.string_history = "\n".join(state.history)
    state.user_input = "" 

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# PALINDROME SPELET", mode="md")
        tgb.text("Skriv ett ord eller mening. Få ⭐ för rätt, förlora 💔 för fel!")

        tgb.input("{user_input}", label="Din text")
        tgb.button("KONTROLLERA", on_action=check_palindrome)

        tgb.text("**Senaste svar:** {result_text}", mode="md")
        tgb.text("**Resultat:** {last_result}", mode="md")
        tgb.text("**Total poäng:** {score} ⭐", mode="md")

        tgb.image("{image_url}", width="300px")

        tgb.text("## Spelhistorik", mode="md")
        tgb.text("{string_history}")
        
if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)

        
    