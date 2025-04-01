import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_NFL_annual_passing_touchdowns_leaders"

try:

    response = requests.get(url)
    response.raise_for_status() 

   
    soup = BeautifulSoup(response.content, 'html.parser')

    
    tables = soup.find_all('table', {'class': 'wikitable'})

    
    if tables:
        
        for table in tables:
            rows = table.find_all('tr')

            
            print(f"{'Year':<6} {'Player':<25} {'Team':<20} {'TDs':<5}")
            print("=" * 60)

            
            for row in rows[1:]:
                cols = [col.get_text(strip=True) for col in row.find_all(['th', 'td'])]

                
                if len(cols) >= 4:
                    year = cols[0]
                    player = cols[1]
                    team = cols[2]
                    touchdowns = cols[3]

                    
                    print(f"{year:<6} {player:<25} {team:<20} {touchdowns:<5}")
                else:
                   
                    continue

    else:
        print("Error: Could not find the statistics table on the page")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    print("Running scrapper one...")
