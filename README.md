This Python script performs web scraping on Century21's real estate listings for San Francisco, CA, extracting property details such as price, number of beds, baths, square footage, address, and locality. 
It utilizes the Requests library for making HTTP requests and BeautifulSoup for parsing HTML content.

Features
Data Extraction: Retrieves property details from Century21's website.
Data Representation: Stores the extracted data in a Pandas DataFrame.
Export to CSV: Saves the collected property information to a CSV file named 'Output.csv'.

How to Use
Prerequisites
Python: Ensure Python 3.x is installed on your system.
Dependencies: Install necessary packages listed in requirements.txt.

Usage
Clone the repository:
git clone https://github.com/your-username/real-estate-data-extractor.git
cd real-estate-data-extractor

Set up a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt


Contributing
Contributions are welcome! Feel free to open issues or pull requests for any enhancements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

