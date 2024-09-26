import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'   

df = pd.read_csv(big_mac_file)              # Convert csv to a dataframe


# return mean value in the specific year of the big mac in dollars ('dollar_pice' column)
def get_big_mac_price_by_year(year,country_code):
    return round(df[df.date.str.contains(year)].dollar_price.mean(), 2)

'''
The function receives the country_code in lower case
The function should return mean value of the big mac in dollars ('dollar_pice' column)
The value must be rounded to 2 decimal numbers
'''
def get_big_mac_price_by_country(country_code):
    return round(df[df.iso_a3 == country_code.upper()].dollar_price.mean(), 2)

'''
The function receives the year 
The function should return the following output from the place that has the cheapest big mac: 
"country_name(country_code): $dollar_price" 
'''
def get_the_cheapest_big_mac_price_by_year(year):
    price = df.loc[
        df[df.date.str.contains(year)].dollar_price.idxmin()
    ]

    return f'{price[3]}({price.iso_a3}): ${round(price.dollar_price,2)}'


'''
The function receives the **year** 
The function should return the following output from the place that has the most expensive big mac:
"country_name(country_code): $dollar_price" (replace the appropriate values)
'''
def get_the_most_expensive_big_mac_price_by_year(year):
    price = df.loc[
        df[df.date.str.contains(year)].dollar_price.idxmax()
    ]

    return f'{price[3]}({price.iso_a3}): ${round(price.dollar_price,2)}'


if __name__ == "__main__":
    pass