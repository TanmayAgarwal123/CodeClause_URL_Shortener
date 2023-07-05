import pyshorteners

url =input('Enter the URL: ')

shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(url))
