import pandas as pd

Monthly_Expences = ['Rent', 'Electricity Bill', 'Groceries', 'News Paper',
            'Transport', 'Gas', 'Vegetables']

Rupees = ['10000', '1500', '1000', '500', '1000',
            '969', '1000']


Rupees_Series = pd.Series(Rupees, index=Monthly_Expences, name='monthly expences')

print(Rupees_Series)