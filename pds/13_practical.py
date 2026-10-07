import requests
from bs4 import BeautifulSoup

search_query = "laptops"
page_no = 1

while True:
    url = f"https://www.flipkart.com/search?q={search_query}&page={page_no}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", {"class": "ZFwe0M row"})

        if not products:
            print("No products found on the page.")
            break

        for item in products:
            name_elem = item.find("div", {"class": "RG5Slk"})
            price_elem = item.find("div", {"class": "hZ3P6w DeU9vF"})
            discount_elem = item.find("div", {"class": "HQe8jr"})

            if name_elem and price_elem and discount_elem:
                print("Product:", name_elem.get_text(strip=True))
                print("Price:", price_elem.get_text(strip=True))
                print("Discount:", discount_elem.get_text(strip=True))
                print("-" * 40)

        print("Page no:", page_no)

    else:
        print("Failed to fetch page. Status code:", response.status_code)
        break

    page_no += 1