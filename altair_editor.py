
#%%
import os
from bs4 import BeautifulSoup as bs4
import webbrowser

#%%

class html_editor:
    def __init__(self, path, contents):
        '''
        path:       place where html is.
        contents:   dict-type (contentsはdictがネストされている)
                    items = {'item1':'ほげほっふぇ', 'item': 'fugafuga'}
                    contents = {'title':'New plot!', 'items': items} 
        '''

        self.path = path
        self.contents = contents

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
        title_txt.string = self.contents['title']

        # h1 tag
        h1_txt = bs4().new_tag("h1")
        h1_txt.string = self.contents['title']

        # htmlへ追加
        html_txt = self.read_all()
        html_txt.head.style.insert_before(title_txt)

        html_txt.body.div.insert_before(h1_txt)

        return html_txt

    def add_items(self):
        '''
        itemsのkeyをリストにする
        itemsのvalueをネストしたリストにする
        '''

        # ul tag
        ul_tag = bs4().new_tag("ul")

        # item key tag
        html_txt = self.add_header()

        html_txt.body.h1.insert_after(ul_tag)


        items = self.contents['items']
        for k, v in items.items():
            # li tag
            li_tag = bs4().new_tag("li")
            li_tag.string = k +': ' + v
            html_txt.body.ul.append(li_tag)

        return html_txt


#%%
my_path = 'C:/Users/stagu/Documents/work/visualization/data/plot.html'

# 以下に変数で設定
items = {'goal':'target', 'geha': 'fugafuga'}
title_txt = 'Wow plot!'

# contents はいじらない
contents = {'title':title_txt, 'items': items} 

my_edited_html = html_editor(my_path, contents)
edited_txt = my_edited_html.add_items().contents[-1]

#%%
with open(my_path, mode='w') as outf:
    outf.write(str(edited_txt))
#%%
# kome
webbrowser.open(my_path)


#%%


