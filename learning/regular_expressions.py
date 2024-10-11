import re

text = "agent phone number is 408-555-1234"
print("phone" in text)
pattern2 = r"(\d{3})-\d{3}-\d{4}"
patter = "phone"
match = re.search(pattern2, text)
print(match.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(2))
print(results.group(1))
print(results.group(3))
