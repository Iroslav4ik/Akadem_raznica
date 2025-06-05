import re


with open('task2.html', 'r', encoding='utf-8') as file:
    content = file.read()

href_pattern = r'href="(.*?)"'
all_links = re.findall(href_pattern, content)

com_links = []
domain_pattern = r'^(https?://|//)[^?#/]*\.com([:/?#]|$)'

for link in all_links:
    if re.match(domain_pattern, link):
        com_links.append(link)

for link in com_links:
    print(link)