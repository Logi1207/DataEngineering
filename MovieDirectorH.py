import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://m.imdb.com/list/ls005534943/'

# Define the user-agent header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a GET request to the URL with the specified user-agent
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store data
serial_numbers = []
movie_name = []
directors = []
rate=[]

# Find all the movie data containers on the webpage
movie_data = soup.findAll('li', attrs={'class': 'ipc-metadata-list-summary-item'})

for index, store in enumerate(movie_data, start=1):
    serial_numbers.append(index)  # Serial number
    name = store.h3.a.text.strip()  # Extract movie name
    movie_name.append(name)
    director_tag = store.find('p', class_='text-muted text-small').find('a')
    if director_tag:
        director = director_tag.text.strip()  # Extract director
    else:
        director = "N/A"
    directors.append(director)

    rating = store.find('div', class_='inline-block ratings-imdb-rating').text.strip()  # Extract IMDb rating
    rate.append(rating)
# Create a DataFrame
movie_list = pd.DataFrame({"Serial No": serial_numbers, "Movie Name": movie_name, "Director": directors,"rate":rate})

# Save the data in Excel format
movie_list.to_excel("Directors_of_movie_s.xlsx", index=False)

# Save the data in CSV format
movie_list.to_csv("Directors_of_movie_h.csv", index=False)

# Display the first 5 rows of the DataFrame
print(movie_list.head())
