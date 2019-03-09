import requests

response = requests.get('https://www.dropbox.com/s/3tlfdh7ws54dum3/user.json?dl=0   ')
print(response.text)