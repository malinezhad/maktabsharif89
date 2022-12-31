import re

text = "HelloWorld"
pattern = r"[A-Z][^A-Z]+"
result = re.findall(pattern, text)
print(result)
