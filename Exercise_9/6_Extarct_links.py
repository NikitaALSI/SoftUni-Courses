import re

site_pat = r'(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)'
while text := input():
    websites = re.finditer(site_pat, text)
    for website in websites:
        print(website.group(1))