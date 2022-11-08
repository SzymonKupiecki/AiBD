import pandas as pd


fluid_ounce = 29.5735295625/1000


def calc_wine_alcohol(row):
    return 5*fluid_ounce*row['wine_servings']*0.12


def recalculate_ounces_to_metric(row):
    return 12*fluid_ounce*row['wine_servings']


def sort_by_wine(df):
    litres_of_wine = df.apply(lambda row: recalculate_ounces_to_metric(row), axis=1)
    alcohol_from_wine = df.apply(lambda row: calc_wine_alcohol(row), axis=1)

    wine_table = pd.DataFrame()
    wine_table['Country'] = df['country']
    wine_table['Litres_of_wine'] = litres_of_wine
    wine_table['Alcohol_from_wine'] = alcohol_from_wine
    wine_table = wine_table.sort_values(by=['Litres_of_wine'], ascending=False)
    wine_table = wine_table.reset_index()
    wine_table = wine_table.drop(['index'], axis=1)

    return wine_table
