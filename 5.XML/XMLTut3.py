import xml.etree.ElementTree as ET
mytree=ET.parse('xml1.xml')
myroot=mytree.getroot()

for prices in myroot.iter('price'):
    prices.text=str(float(prices.text)+10)
    prices.set('newprices','yes')

# to add new tag
ET.SubElement(myroot[0],"tasty")
for temp in myroot.iter('tasty'):
    temp.text=("YES")
mytree.write('modified.xml')

#poping the element
print(myroot[1][0].attrib.pop('name'))
print(myroot.remove(myroot[1]))
mytree.write('modified.xml')
