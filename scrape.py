import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a GET request to the URL and store the response in 'r'
r = requests.get('http://pythonhow.com/example.html')

# Check if the request was successful (status code 200)
if r.status_code == 200:
    # Access the content of the response and store it in 'c'
    c = r.content

    # Use BeautifulSoup to parse the content
    soup = BeautifulSoup(c, 'html.parser')

    # Find all elements with class 'propertyRow' within the parsed content
    all_properties = soup.find_all('div', {'class': 'propertyRow'})

    property_list = []

    # Iterate through each property element
    for item in all_properties:
        property_dict = {}
        property_dict['Price'] = item.find('h4', {'class': 'propPrice'}).text.strip()
        property_dict['Address'] = item.find_all('span', {'class': 'propAddressCollapse'})[0].text
        property_dict['Locality'] = item.find_all('span', {'class': 'propAddressCollapse'})[1].text

        # Handling exceptions for missing data
        property_dict['Beds'] = item.find('span', {'class': 'infoBed'}).find('b').text if item.find('span', {
            'class': 'infoBed'}) else None
        property_dict['Area'] = item.find('span', {'class': 'infoSqft'}).find('b').text if item.find('span', {
            'class': 'infoSqft'}) else None
        property_dict['Half Bath'] = item.find('span', {'class': 'infoValueHalfBath'}).find('b').text if item.find(
            'span', {'class': 'infoValueHalfBath'}) else None
        property_dict['Full Bath'] = item.find('span', {'class': 'infoValueFullBath'}).find('b').text if item.find(
            'span', {'class': 'infoValueFullBath'}) else None

        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            for feature_group, feature_name in zip(column_group.find_all('span', {'class': 'featureGroup'}),
                                                   column_group.find_all('span', {'class': 'featureName'})):
                if 'lot Side' in feature_group.text:
                    property_dict['Lot Size'] = feature_name.text

        property_list.append(property_dict)

    # Create a DataFrame from the list of property dictionaries
    df = pd.DataFrame(property_list)

    # Print the DataFrame and save it to a CSV file
    print(df)
    df.to_csv('Output.csv', index=False)

else:
    print('Failed to fetch data from the website:', r.status_code)
