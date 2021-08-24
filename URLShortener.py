# Here we build a URL shortener

import pyshorteners


url = input("Enter your URL")
output = pyshorteners.Shortener().tinyurl.short(url)

print(output)
