import pandas as pd
import matplotlib.pyplot as plt
import gsw

# cria o dataframe
data = pd.read_csv('/dados/resultado_binado.csv')

# calcula salinidade absoluta a partir da salinidade prática (salinidade, pressão, lon, lat)
sa = gsw.conversions.SA_from_SP(data['salinity'], data['pressure'], data['pressure'], )

# calcula a temperatura conservativa (salinidade absoluta, temperatura in-situ, sea pressure)
ct = gsw.conversions.CT_from_t(sa, data['temperature'], data['pressure'])

# calcula a freqência de brunt-vaisalla (salinidade absoluta, temperatura conservativa, sea pressure, lat=None, axis=0)
n2 = gsw.Nsquared(sa, ct, data['pressure'])
