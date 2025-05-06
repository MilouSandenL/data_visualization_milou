import numpy as np
import pandas as pd
import plotly.express as px
from taipy import Gui
import taipy.gui.builder as tgb

num_dices = 5
num_rows = 1000

df = pd.DataFrame()
mean_theoretical = 3.5
mean_calculated = 0.0
mean_difference = 0.0
fig = px.histogram()

def simulate_dice(state):
    state.df = pd.DataFrame(
        np.random.randint(1, 7, size=(state.num_throws, state.num_dices)),
        columns=[f"Dice {i+1}" for i in range(state.num_dices)]
    )
    state.df.insert(0, "Throw", range(state.num_throws))
    
    means = state.df.iloc[:, 1:].mean(axis=1)
    state.mean_culculated = round(means.mean(), 3)
    state.mean_difference = round(abs(state.mean_theoretical - state.mean_calculated, 3))
    
    hist_df = pd.DataFrame({"value": means})
    state.fig = px.histogram(hist_df, x = "value", nbins=20)
    
with tgb.Page() as page:
    tgb.text("# DICE SIMULATIONS", mode="md")
    
    with tgb.layout(columns="1 1")