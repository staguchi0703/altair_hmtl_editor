
#%%
import os
from bs4 import BeautifulSoup as bs4
import webbrowser

#%%

class html_editor:
    def __init__(self, path, title, items_dic):
        '''
        path:       place where html is.
        title_txt: txt
        items_dic:  items_dict = {'item1':'ほげほっふぇ', 'item': 'fuga'} 
        '''

        self.path = path
        self.title = title_txt
        self.items_dic = items_dic

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
        title_txt.string = self.title

        # h1 tag
        h1_txt = bs4().new_tag("h1")
        h1_txt.string = self.title

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


        items_dic = self.items_dic
        for k, v in items_dic.items():
            # li tag
            li_tag = bs4().new_tag("li")
            li_tag.string = k +': ' + v
            html_txt.body.ul.append(li_tag)

        return html_txt


#%%
my_path = r'C:\Users\spuns\OneDrive\ドキュメント\work\altair_hmtl_editor\data\plot.html'

# 以下に変数で設定
items_dic = {'goal':'target', 'geha': ['fugafuga11111111', 'hegehege222222222222']}
title_txt = 'Wow plot!'

my_edited_html = html_editor(my_path, title_txt, items_dic)
edited_txt = my_edited_html.add_items().contents[-1]

#%%
with open(my_path, mode='w') as outf:
    outf.write(str(edited_txt))
#%%
# kome
webbrowser.open(my_path)


#%%


