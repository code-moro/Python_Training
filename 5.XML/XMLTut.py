import xml.etree.ElementTree as ET
mytree=ET.parse('xml1.xml')
myroot = mytree.getroot()
print(myroot)

print(myroot.tag)
print(myroot.attrib)
print(myroot[0].tag)

for x in myroot[0]:
    print(x.tag,x.attrib)

for x in myroot[0]:
    print(x.text)

# try to create small xml file and read it in same way
for x in myroot.findall('food'):
    item=x.find('item').text
    price = x.find('price').text
    print(item,price)

print(myroot[0].findtext('description'))