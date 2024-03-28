import pandas as pd
import requests
from bs4 import BeautifulSoup

def webScrapMoviesH():

    url = 'https://www.imdb.com/list/ls005534943/'

    # Define the user-agent header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send a GET request to the URL with the specified user-agent
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lists to store data
    serial_numbers = []
    movie_name = []
    year = []
    time = []

    # Find all the movie data containers on the webpage
    movie_data = soup.find_all('div', class_='lister-item-content')

    for index, store in enumerate(movie_data, start=101):
        serial_numbers.append(index)  # Serial number
        name = store.h3.a.text.strip()  # Extract movie name
        movie_name.append(name)

        year_of_release = store.find('span', class_='lister-item-year').text.strip('()')  # Extract year of release
        year.append(year_of_release)
    

      
    

        runtime_element = store.p.find('span', class_='runtime')  # Find runtime element
        runtime = runtime_element.text.strip().replace(' min', '') if runtime_element else None  # Extract movie runtime
        time.append(runtime)

    # Create a DataFrame
    movie_list = pd.DataFrame({"Serial No": serial_numbers, "Movie Name": movie_name, "Year of Release": year, "Watch Time": time})

    # Save the data in Excel format
    # movie_list.to_excel("movies_in_letter_H.xlsx", index=False)

    # Save the data in CSV format
    movie_list.to_csv("movies_in_letter_H.csv", index=False)

    # Display the first 5 rows of the DataFrame
    print(movie_list.tail())
    
def webScrapMoviesS():
    url = 'https://www.imdb.com/list/ls005751100/'

    # Define the user-agent header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send a GET request to the URL with the specified user-agent
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lists to store data
    serial_numbers = []
    movie_name = []
    year = []
    time = []

    # Find all the movie data containers on the webpage
    movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-detail'})

    for index, store in enumerate(movie_data, start=1):
        serial_numbers.append(index)  # Serial number
        name = store.h3.a.text.strip()  # Extract movie name
        movie_name.append(name)

        year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.strip().replace('(', '').replace(')', '')  # Extract year of release
        year.append(year_of_release)

    
    

        runtime = store.p.find('span', class_='runtime').text.strip().replace(' min', '')  # Extract movie runtime
        time.append(runtime)

    # Create a DataFrame
    movie_list = pd.DataFrame({"Serial No": serial_numbers, "Movie Name": movie_name, "Year of Release": year, "Watch Time": time})

    # Save the data in Excel format
    #movie_list.to_excel("movies_in_letter_s.xlsx", index=False)

    # Save the data in CSV format
    movie_list.to_csv("movies_in_letter_s.csv", index=False)

    # Display the first 5 rows of the DataFrame
    print(movie_list.head())

if __name__ == '__main__': 
    webScrapMoviesH()
    webScrapMoviesS()
