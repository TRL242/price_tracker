
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib




url = "https://www.amazon.com/Eyoyo-Portable-Underwater-Cablewith-Waterproof/dp/B07QV1F2GR/ref=sr_1_1_sspa?dchild=1&keywords=fishing+camera&qid=1613460492&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUk5HSFVLSjlKNzY0JmVuY3J5cHRlZElkPUEwMjY1NzAwM0I3UlAzUlU0UDlFSCZlbmNyeXB0ZWRBZElkPUEwMDM4NDk5ODk0WTREQVNVTDRSJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-ca"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_saleprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
#     print("True")
# else:
#     print("False")
    message = f"{title} is now {price}"

    with smtplib.SMTP(smtp.gmail.com, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )