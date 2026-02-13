import pandas as pd

# Sample data
data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(data)

powers_data = {'X':[1,2,3,4,5], 'Y':[2,3,4,1,2],'Z':[3,2,1,2,1]}
powers_df = pd.DataFrame(powers_data)

result_df = df ** powers_df

print(result_df)
