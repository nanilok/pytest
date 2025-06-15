import re

#text="im an indian"
#pattern="i love python"
#
#search = re.search(text, pattern)
#if search:
#    print("exp text", search.group())
#else:
#    print("exp not found")

#text = "The quick brown fox lokesh"
#pattern = "lokesh"
#
#search = re.search(pattern, text)
#if search:
#    print("Pattern found:", search.group())
#else:
#    print("Pattern not found")

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)