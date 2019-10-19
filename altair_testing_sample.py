# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
from bs4 import BeautifulSoup as bs
import webbrowser


# %%
import altair as alt
from vega_datasets import data

class DataMaker:
    def __init__(self, path):
        self.cars = data.cars()
        self.path = path

    def data_make(self):
            
        click = alt.selection(type='multi', encodings=['x', 'y'])

        scatter1 = alt.Chart(self.cars).mark_point().encode(
            alt.X('Horsepower:Q',
                scale=alt.Scale(type='log', domain=(30, 300)),
                axis=alt.Axis(title='Horsepawer[MPa]')),
            alt.Y('Miles_per_Gallon:Q',
                scale=alt.Scale(domain=(0, 50))),
            color=alt.condition(click, 'Origin:N', alt.value(
                'lightgray'), legend=None),
            tooltip=['Name:N']
        ).properties(
            selection=click,
            title='Once a famous cars data')

        base = alt.Chart(self.cars).mark_point().encode(
            alt.X('Cylinders:N'),
            alt.Y('Origin:N'),
            color=alt.condition(click, 'Origin:N', alt.value('lightgray'), legend=None)
        ).properties(
            selection=click,
            title='Data selector with [Click + Shift-key]')

        return (base | scatter1)


    def data2html(self):
        os.makedirs('./data/', exist_ok=True)
        data = self.data_make()
        data.save('./data/plot.html')


    def data_show(self):
        webbrowser.open(self.path)


# %%

my_path = r'C:\Users\spuns\OneDrive\ドキュメント\work\altair_hmtl_editor\data\plot.html'
os.chdir(my_path.rsplit('\\',2)[0])

my_data = DataMaker(my_path)
my_data.data2html()
