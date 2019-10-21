# %%
from bs4 import BeautifulSoup as bs4

body_html = bs4()
#%%
div_tag = bs4().new_tag('div')
div_tag.string = 'hello world'

body_html.append(div_tag)
#%%
ul_tag = bs4().new_tag('ul')

body_html.div.append(ul_tag)

#%%
li_tag = bs4().new_tag('li')
li_tag.string = 'item1'
body_html.div.ul.append(li_tag)

#%%
li_tag = bs4().new_tag('li')
li_tag.string = 'item2'
body_html.div.ul.append(li_tag)


#%%
print(body_html.prettify())

#%%
