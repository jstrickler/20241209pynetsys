import lxml.etree as et

knights = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_tag = et.SubElement(knights, 'knight', knight_name=name)
        title_tag = et.SubElement(knight_tag, "title")
        title_tag.text = title
        et.SubElement(knight_tag, 'color').text = color
        et.SubElement(knight_tag, 'quest').text = quest
        et.SubElement(knight_tag, 'comment').text = comment

doc = et.ElementTree(knights)
doc.write('knights.xml', pretty_print=True, xml_declaration=True)




xml_doc = et.tostring(knights, xml_declaration=True, pretty_print=True)
xml_str = xml_doc.decode()
print(xml_str)

