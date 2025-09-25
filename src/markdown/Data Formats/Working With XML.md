# Working with XML

Python provides several libraries and APIs to parse, navigate, and generate XML documents. This document outlines core concepts, standard tools, quirks, and best practices for XML processing.

---

## 1. When to Use XML

* Data exchange with legacy systems
* Configuration files (less common today)
* Standards and specifications (e.g., SOAP, SVG, RSS)

Modern alternatives: JSON or YAML (more Pythonic), but XML is still relevant for structured data with schemas and namespaces.

---

## 2. Standard Library Modules

### `xml.etree.ElementTree`

* Lightweight and simple
* Part of the Python standard library

```python
import xml.etree.ElementTree as ET

xml = """
<data>
  <item name="foo" />
  <item name="bar" />
</data>
"""

root = ET.fromstring(xml)
for item in root.findall("item"):
    print(item.attrib["name"])
```

**Pros**:

* No external dependencies
* Easy for simple use cases

**Cons**:

* Limited XPath support
* No validation

### `minidom`

* DOM-style parser
* Verbose and low performance

---

## 3. Third-Party Libraries

### `lxml`

* Full-featured, C-based, fast and powerful
* Supports XPath, XSLT, schema validation

```python
from lxml import etree

tree = etree.XML("""
<data>
  <item name="foo"/>
  <item name="bar"/>
</data>
""")

names = tree.xpath("//item/@name")
print(names)  # ['foo', 'bar']
```

### `xmltodict`

* Converts XML to nested Python dictionaries
* Useful for quick interoperability

```python
import xmltodict

xml = """
<person>
  <name>John</name>
  <age>30</age>
</person>
"""

parsed = xmltodict.parse(xml)
print(parsed['person']['name'])  # John
```

---

## 4. Writing XML

### Using `ElementTree`

```python
root = ET.Element("data")
item = ET.SubElement(root, "item", name="example")
tree = ET.ElementTree(root)
tree.write("output.xml")
```

### Pretty-print with `minidom`

```python
from xml.dom import minidom

rough_string = ET.tostring(root, 'utf-8')
pretty = minidom.parseString(rough_string).toprettyxml(indent="  ")
print(pretty)
```

---

## 5. Namespaces

### Defining and Accessing

```xml
<root xmlns:h="http://example.com/hello">
  <h:tag>value</h:tag>
</root>
```

```python
ns = {'h': 'http://example.com/hello'}
root.find("h:tag", namespaces=ns)
```

Namespaces must be explicitly mapped in `ElementTree`.

---

## 6. Validation

### DTD / XML Schema

* `lxml` supports validation with DTD and XSD

```python
schema = etree.XMLSchema(etree.parse("schema.xsd"))
assert schema.validate(etree.parse("input.xml"))
```

No built-in support for validation in `ElementTree`.

---

## 7. Security Considerations

* Avoid parsing untrusted XML with `ElementTree` or `minidom`
* Prefer `defusedxml` when handling external input

```bash
pip install defusedxml
```

---

## 8. Common Pitfalls and Quirks

* `ElementTree` ignores comments and processing instructions by default
* XPath in `ElementTree` is limited (no `//` or complex queries)
* Namespace handling is verbose
* Attribute order is not preserved (XML is unordered)

---

## 9. Tools for Debugging and Exploration

* Online formatters: [https://xmlformatter.org/](https://xmlformatter.org/)
* XML linters and schema validators
* Visual Studio Code or IntelliJ with XML plugins

---

## 10. Best Practices

* Use `lxml` for production-grade parsing, especially if validation or XPath is needed
* Use `xmltodict` for quick conversions to Python objects
* Always validate external XML when possible
* Sanitize or sandbox XML input if not trusted
* Avoid writing custom XML parsers manually
