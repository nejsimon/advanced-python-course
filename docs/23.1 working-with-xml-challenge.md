# Working with XML in Python: Coding Challenges

These challenges are designed to build practical experience with XML parsing, generation, navigation, and validation using different tools available in Python.

---

## Challenge 1: Parse and Extract Attributes

**Objective:** Use `xml.etree.ElementTree` to parse an XML string and print all `name` attributes from `<item>` tags.

```xml
<data>
  <item name="foo" />
  <item name="bar" />
</data>
```

**Tasks:**

* Parse the XML using `ET.fromstring()`.
* Use `.findall()` to extract and print each name.

---

## Challenge 2: Build and Write XML Tree

**Objective:** Use `ElementTree` to programmatically construct the following XML and write it to a file:

```xml
<library>
  <book title="1984" author="George Orwell" />
  <book title="Brave New World" author="Aldous Huxley" />
</library>
```

**Tasks:**

* Create root and sub-elements.
* Write to `library.xml` using `ElementTree.write()`.

---

## Challenge 3: Pretty-Print XML

**Objective:** Given an `ElementTree`, use `minidom` to output a nicely formatted version to the console.

**Tasks:**

* Use `ET.tostring()` to get raw XML.
* Use `minidom.parseString()` and `.toprettyxml()`.

---

## Challenge 4: Extract Data with XPath (lxml)

**Objective:** Use `lxml.etree` to extract all `<item>` tag `name` attributes using XPath.

**Tasks:**

* Use `.xpath('//item/@name')`.
* Return list of names.

---

## Challenge 5: Convert XML to Dictionary

**Objective:** Convert the following XML into a Python dictionary using `xmltodict`:

```xml
<user>
  <id>123</id>
  <email>user@example.com</email>
</user>
```

**Tasks:**

* Use `xmltodict.parse()`
* Access and print the email address.

---

## Challenge 6: Handle Namespaces

**Objective:** Extract a namespaced tag from this XML using `ElementTree`:

```xml
<root xmlns:h="http://example.com/ns">
  <h:title>Main</h:title>
</root>
```

**Tasks:**

* Define a namespace dictionary.
* Use `.find('h:title', namespaces=...)`.

---

## Challenge 7: Validate XML Against XSD

**Objective:** Use `lxml.etree` to validate an XML document against a schema.

**Tasks:**

* Write a simple `schema.xsd`.
* Parse the XML and schema.
* Use `XMLSchema.validate()`.

---

## Challenge 8: Secure Parsing with defusedxml

**Objective:** Safely parse external XML input using `defusedxml.ElementTree`.

**Tasks:**

* Install `defusedxml`
* Replace standard `ElementTree` with `defusedxml.ElementTree`

---

## Challenge 9: Round-Trip: Dict → XML → Dict

**Objective:** Use `xmltodict` to:

* Convert a dictionary to XML.
* Convert the generated XML back to a dictionary.

**Tasks:**

* Use `xmltodict.unparse()`.
* Validate data integrity.

---

## Challenge 10: Compare `ElementTree` and `lxml`

**Objective:** Given a sample XML, perform the same data extraction using both libraries:

**Tasks:**

* Parse with both `ElementTree` and `lxml.etree`.
* Extract a list of elements and compare behavior and syntax.
