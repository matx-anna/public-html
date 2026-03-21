import yaml
import xml.etree.ElementTree as xml_tree

with open('hello.yml', 'r') as file:
    dt = yaml.safe_load(file)

elem1 = xml_tree.Element("elem1", {
    "version" : "1.0"
})

subelem1 = xml_tree.SubElement(elem1, "subelem1")

xml_tree.SubElement(subelem1, "title").text = dt["title"]

output_tree = xml_tree.ElementTree(elem1)
output_tree.write("hello.xml", encoding="UTF-8", xml_declaration=True)

print ("hello!")