from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px 

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden"), x = "year", y = "pop")

slider_value = 20
selected_fruit = "avocado"
number_one = 5
number_two = 8

sum_ = number_one + number_two


# vi kommer åt alla våra variabler i state
def perform_calculation(state):
    print(state.number_one)

    state.sum_ = int(state.number_ont) + (state.number_two)
    # TODO: addera minus, multiplication, och delat med.


def clear_results(state):
    state.sum_ = ""

# man börjar med en page, det är grunden - sedan lägger man in mer så man får en hierarkisk struktur
with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        with tgb.layout(columns="1 1 1"):
            with tgb.part() as column_fruit:
                tgb.text("# Hello there taipy", mode="md")
                tgb.text("Welcome to the world of reactive programming")

                # binds slider_value, makes it dynamic
                # om vi drar den så ändras
                tgb.slider(value="{slider_value}", min=1, max=50, step=1, continuous=False)
                tgb.text("Slider value is at {slider_value}")
                tgb.text("Slider value again is at {slider_value}")

                tgb.text("Select your favorite fruit", mode="md")
                tgb.selector(
                    value="{selected_fruit}",
                    lov=["tomato", "apple", "avocado", "banana"],
                    dropdown=True,
                )
                tgb.text("Yummy{selected_fruit}")
                tgb.image("assets/{selected_fruit}.jpg")

            with tgb.part() as column_calculator:
                tgb.text("## Coolu calcuratoru", mode="md")
                tgb.text("Type in a number")
                tgb.input("{number_one}", on_change=clear_results)

                # on_change -> this function will run when value is changed
                tgb.text("Type in another number")
                tgb.input("{number_two}", on_change=clear_results)

                tgb.text("You have typed in {number_one} and {number_two}")

                # on_action -> this function will run when button is clicked
                tgb.button(label="CALCULATU", class_name="plain", on_action=perform_calculation)

                tgb.text("{number_one} + {number_two} 0 {sum_}")
            
            with tgb.part() as column_data:
                tgb.table("{df}", page_size=15)
                tgb.chart(figure="{fig}")

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloder=True, port=8080)
