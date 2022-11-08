import pandas as pd


fluid_ounce = 29.5735295625/1000


def calc_spirit_alcohol(row):
    return 1.5*fluid_ounce*row['spirit_servings']*0.4


def recalculate_ounces_to_metric(row):
    return 1.5*fluid_ounce*row['spirit_servings']


def sort_by_spirit(df):
    litres_of_spirit = df.apply(lambda row: recalculate_ounces_to_metric(row), axis=1)
    alcohol_from_spirit = df.apply(lambda row: calc_spirit_alcohol(row), axis=1)

    spirit_table = pd.DataFrame()
    spirit_table['Country'] = df['country']
    spirit_table['Litres_of_spirit'] = litres_of_spirit
    spirit_table['Alcohol_from_spirit'] = alcohol_from_spirit
    spirit_table = spirit_table.sort_values(by=['Litres_of_spirit'], ascending=False)
    spirit_table = spirit_table.reset_index()
    spirit_table = spirit_table.drop(['index'], axis=1)

    return spirit_table
