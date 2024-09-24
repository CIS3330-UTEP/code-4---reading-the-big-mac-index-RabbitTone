import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    return round(df[df.date.str.contains(year)].dollar_price.mean(), 2)

def get_big_mac_price_by_country(country_code):
    return round(df[df.iso_a3 == country_code.upper()].dollar_price.mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    price = df.loc[
        df[df.date.str.contains(year)].dollar_price.idxmin()
    ]

    print(f'{price[3]}({price.iso_a3}): ${round(price.dollar_price,2)}')

def get_the_most_expensive_big_mac_price_by_year(year):
    price = df.loc[
        df[df.date.str.contains(year)].dollar_price.idxmax()
    ]

    print(f'{price[3]}({price.iso_a3}): ${round(price.dollar_price,2)}')


if __name__ == "__main__":
    print(get_big_mac_price_by_year('2005', 'BRA'))
    print(get_big_mac_price_by_country('aus'))
    print(get_the_cheapest_big_mac_price_by_year('2008'))
    print(get_the_most_expensive_big_mac_price_by_year('2003'))