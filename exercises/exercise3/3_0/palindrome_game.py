from taipy import Gui
import taipy.gui.builder as tgb

user_input = ""
result_text = ""
score = 0
image_url = ""

def palindrome(text):
    clean = ''.join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

def check_palindrome(state):
    state.result_text = f"Du skrev: '{state.user_input}'"
    if palindrome(state.user_input):
        state.score += 1
        state.image_url = "../assets/fake_cat.png"
    else:
        state.score -= 1
        state.image_url = "../assets/fake_sad_rabbit.png"
    
    state.user_input = ""
    
with tgb.Page() as page:
    with tgb.part(class_name="containers card"):
        tgb.text("# PALINDROME GAME", mode="md")
        tgb.text("Skriv ett ord eller en mening och tryck sedan på knappen: ")
        
        tgb.input("{user_input}", label="Din text")
        tgb.button("Kontrollera", on_action=check_palindrome)
        
        tgb.text("{result_text}")
        tgb.text("Poäng: {score}")
        
        tgb.image("{image_url}", width="300px")
        
if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
        
