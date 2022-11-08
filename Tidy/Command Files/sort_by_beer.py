import pandas as pd


fluid_ounce = 29.5735295625/1000


def calc_beer_alcohol(row):
    return 12*fluid_ounce*row['beer_servings']*0.05


def recalculate_ounces_to_metric(row):
    return 12*fluid_ounce*row['beer_servings']


def sort_by_beer(df):
    litres_of_beer = df.apply(lambda row: recalculate_ounces_to_metric(row), axis=1)
    alcohol_from_beer = df.apply(lambda row: calc_beer_alcohol(row), axis=1)

    beer_table = pd.DataFrame()
    beer_table['Country'] = df['country']
    beer_table['Litres_of_beer'] = litres_of_beer
    beer_table['Alcohol_from_beer'] = alcohol_from_beer
    beer_table = beer_table.sort_values(by=['Litres_of_beer'], ascending=False)
    beer_table = beer_table.reset_index()
    beer_table = beer_table.drop(['index'], axis=1)

    return beer_table
