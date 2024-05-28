import requests
import click


@click.command()
@click.option('--coin_id', default="bitcoin", help="The coin id")
@click.option('--currency', default="usd", help="The currency")
def get_coin_price(coin_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url).json()
    coin_price = response[coin_id][currency]    
    print(f"The price of {coin_id} in {currency} is {coin_price}")
    
if __name__ == "__main__":
    get_coin_price()