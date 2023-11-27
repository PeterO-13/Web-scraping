import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a GET request to the URL and store the response in 'r'
r = requests.get('https://www.century21.com/real-estate/san-francisco-ca/LCCASANFRANCISCO/')

# Check if the request was successful (status code 200)
if r.status_code == 200:
    # Access the content of the response and store it in 'c'
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all_properties = soup.find_all('div', {'class': 'property-card'})

    # Create an empty list to store property data
    property_list = []

    for item in all_properties:
        d = {}
        d['Price'] = item.find('a', {'class': 'listing-price'}).text.replace('\n', '').replace(' ', '')
        d['Beds'] = item.find('div', {'class': 'property-beds'}).text.strip() if item.find('div', {'class': 'property-beds'}) else 'Bed information not found'

        # Handle 'property-baths'
        if item.find('div', {'class': 'property-beds'}):
            d['Baths'] = item.find('div', {'class': 'property-baths'}).text.strip()
        else:
            d['Baths'] = 'Bath information not found'

        # Handle 'property-sqft'
        property_sqft = item.find('div', {'class': 'property-sqft'})
        d['Area'] = property_sqft.text.strip() if property_sqft else 'Property square footage not available'

        d['Address'] = item.find('div', {'class': 'property-address'}).text.replace('\n', '')
        d['Locality'] = item.find('div', {'class': 'property-city'}).text.replace('\n', '')

        # Append the property data to the list
        property_list.append(d)

    # Create a DataFrame from the property list
    df = pd.DataFrame(property_list)

    # Print the DataFrame
    print(df)

    # Save the DataFrame to a CSV file named 'Output.csv'
    df.to_csv('Output.csv', index=False)

else:
    print('Failed to fetch data from the website:', r.status_code)
