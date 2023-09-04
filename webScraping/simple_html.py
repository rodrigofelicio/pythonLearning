from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
    <head></head>
    <body>
        <h1>This is a title</h1>
        <p class="subtitle"> This is a Paragraph element with a css class.</p>
        <p>Here's another p without a css class</p>
        <ul>
            <li>Rolf</li>
            <li>Charlie</li>
            <li>Jen</li>
            <li>Jose</li>                        
        </ul>
    </body>
</html>
'''
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
#print(simple_soup.find('h1'))
#print(simple_soup.find('h1').string)

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [item.string for item in list_items]
    #content_items = []
    #for item in list_items:
    #    content_items.append(item.string)
    
    print(list_items)
    print(list_contents)
    #print(content_items)
    

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)
    

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    other_paragraph = [p for p in paragraphs if not 'subtile' in p.attrs.get('class', [])]
    print(other_paragraph[1].string)

find_title()
find_list_items()
find_subtitle()
find_other_paragraph()