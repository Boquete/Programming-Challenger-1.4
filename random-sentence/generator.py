import requests

url = 'https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies'
print("Finding cool quote..")
response = requests.post(url, headers={
    "X-Mashape-Key": "6Uguti5V3WmshsxQkrg36UdP8noep12Rdgejsnj6Y9SDqbWn8J",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
})
data = response.json()
print('"', data['quote'], '"', "\n", data['author'])
