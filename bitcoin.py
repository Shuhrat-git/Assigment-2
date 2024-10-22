import sys
import requests

def main():
    # Ensure the user has provided exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: bitcoin.py <number_of_bitcoins>")
    try:
        # Attempt to convert the argument to a float (number of Bitcoins)
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid number of Bitcoins")

    # URL for CoinDesk API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        # Make a GET request to the CoinDesk API
        response = requests.get(url)
        # Raise an exception if the request fails
        response.raise_for_status()

        # Parse the JSON data from the response
        data = response.json()

        # Get the current Bitcoin price in USD
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
        print(bitcoin_price_usd)

        # Calculate the total cost
        total_cost = num_bitcoins * bitcoin_price_usd

        # Output the total cost, formatted with a thousands separator and 4 decimal places
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Error: Unable to retrieve Bitcoin price")

if __name__ == "__main__":
    main()
