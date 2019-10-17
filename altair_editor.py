
#%%
import os
from bs4 import BeautifulSoup as bs4
import webbrowser

#%%

class html_editor:
    def __init__(self, path):
        self.path = path

    def open_html(self):
        with open(self.path) as f:
            return f.read()

    def read_all(self):
        return bs4(self.open_html(),'html.parser')

    def print_all(self):
        print(self.read_all())

    def show_head(self):
        return self.read_all().head

    def add_header(self):
        '''
        headにtitle-tagを追加する
        bodyにh1-tagを使いしてtitleと同じ見出しを付ける
        '''

        # title tag
        title_txt = bs4().new_tag("title")
        title_txt.string = 'New plot!'

        # h1 tag
        h1_txt = bs4().new_tag("h1")
        h1_txt.string = 'New plot!'

        # htmlへ追加
        html_txt = self.read_all()
        html_txt.head.style.insert_before(title_txt)

        html_txt.body.div.insert_before(h1_txt)

        return html_txt


#%%
my_path = 'C:/Users/stagu/Documents/work/visualization/data/plot.html'
my_edited_html = html_editor(my_path)
edited_txt = my_edited_html.add_header().contents[-1]

#%%
with open(my_path, mode='w') as outf:
    outf.write(str(edited_txt))
#%%
# kome
webbrowser.open(my_path)


#%%


