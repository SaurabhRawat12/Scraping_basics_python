from selenium import webdriver
from bs4 import BeautifulSoup

#to use it for chrome seperate window 
driver = webdriver.Chrome(executable_path = r'E:\Downloads\Compressed\chromedriver.exe')


driver = webdriver.PhantomJS(executable_path = r'E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://en.wikipedia.org/wiki/Wil_Wheaton')

#content loads from net
html_doc = driver.page_source

#content is being added manually
html_doc =''' <!DOCTYPE html>
<html>
<body>

<p class='title'>This is a paragraph.
</p>

<p class='story'>jsdlkjaldjlajsdlkjasld;
<a href='sdjfhshdfkjh' class='sister' id='link1'>abcd</a>
<a href='shxkshakjhajkd' class='sister' id='link2'>abcd</a>
<a href='sdjfsxaxsaxh' class='sister' id='link3'>abcdh</a>;
nasdjasjdlkasjdl
</p>

<p class='story'>jakhdjadkhaskjdh</p>



</body>
</html>'''

#creating soup object
soup = BeautifulSoup(html_doc,'lxml')

#incase the html file is in the same folder
soup = BeautifulSoup(open('sample.html'),'lxml')

#helps to make html parsed text readable
pretty_html = soup.prettify()
print(pretty_html)

#to search for any first tag by its name like p,h
first_p_tag = soup.find('p')
print(first_p_tag)

#to search for all the tags having the same name
p_tags = soup.find_all('p')
print (p_tags)
print(len(p_tags))

#search with tag name and class attribute
p_tag = soup.find('p', class_ = 'story')
p_tags = soup.find_all('p', class_ = 'story')
print(p_tag)
print(p_tags)

#to search for the other attributes like id or other use dictionary like key value pair
a_tag = soup.find('a',{'id':'link1'})
print(a_tag)

#to print the tag by the string name present inside it
a_abcd= soup.find_all('a', string = 'abcd')
print(a_abcd)

#to print by hierarchy of parent child siblings
#for child
p = soup.find('p',class_="story")
p_child = p.findChildren()
print(p_child)

#for parent
p = soup.find('p',class_="story")
p_parent = p.findParent()
print(p_parent)

#for siblings
a_first = soup.find('a')
remaining_siblings = a_first.findNextSiblings()
print(remaining_siblings)

#search scope this means we can search inside of a already searched item
first_p = soup.find('p')
print(first_p.find('a'))

#to extract the data present inside the tags
first_p = soup.find('p')
print(first_p.text)

first_a = soup.find('a')
print(first_a.text)

#to extract the links present inside the a tags

a_tags = soup.find_all('a')
for a in a_tags:
    print(a['href'])
    
#to extract data from tables
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)
    