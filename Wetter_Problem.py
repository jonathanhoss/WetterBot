from bs4 import BeautifulSoup


html_doc = '''<div class="header"><h1>Header</h1></div>
<div class="container">
    <div class="header"><h1>Sub Header</h1></div>
    <p>Target_2</p>
    <p>Target_3</p>
    <p>Target_4</p>
</div>'''

soup = BeautifulSoup(html_doc, 'html.parser')

targets = soup.find_all("div", class_=["header", "container"])

for tag in targets:
    if tag.find_parent(attrs={'class':'container'}):
        continue
    print(tag.text.strip())