import pandas as pd


data = {
    'Kraj': ['Polska', 'Niemcy', 'USA', 'Chiny', 'Indie'],
    'Przyrost Ludności 2022': [100000, 250000, 300000, 50000, 200000]
}


df = pd.DataFrame(data)


kraj_max_przyrost = df['Przyrost Ludności 2022'].idxmax()


kraj_max_przyrost_nazwa = df.loc[kraj_max_przyrost, 'Kraj']
przyrost_max = df.loc[kraj_max_przyrost, 'Przyrost Ludności 2022']

print(f"Kraj z największym przyrostem ludności w 2022 roku to: {kraj_max_przyrost_nazwa}")
print(f"Przyrost ludności: {przyrost_max}")
