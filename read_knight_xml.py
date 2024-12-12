import lxml.etree as et

doc = et.parse('knights.xml')

root = doc.getroot()
print(f"{root.tag = }")
for knight in root.findall('knight'):
    name = knight.get('knight_name')
    title = knight.findtext('title')
    color = knight.findtext('color')
    quest = knight.findtext('quest')
    comment = knight.findtext('comment')
    print(title, name, color, quest, comment)
print('-' * 60)
for knight in doc.findall('.//knight'):
    print(knight.find('title').text, knight.get('knight_name'))
