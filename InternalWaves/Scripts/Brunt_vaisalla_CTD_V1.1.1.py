import pandas as pd
import matplotlib.pyplot as plt
import gsw
import time

# cria o dataframe
data = pd.read_csv('/home/labdino/PycharmProjects/CTDprocessing/dados/01. Dados Brutos/02_radial_LADCP/0635_29072019_2033/FILE15_binado.csv')

# extrai as colunas do dataframe para um array NumPy
salinidade = data['Calc. SALINITY; PSU'].values
pressao = data['PRESSURE;DBAR'].values
temperatura = data['TEMPERATURE;C'].values

def bruntvaisala():
    # calcula salinidade absoluta a partir da salinidade prática (salinidade, pressão, lon, lat)
    sa = gsw.conversions.SA_from_SP(salinidade, pressao, 42, 23)

    # calcula a temperatura conservativa (salinidade absoluta, temperatura in-situ, sea pressure)
    ct = gsw.conversions.CT_from_t(sa, temperatura, pressao)

    # calcula a freqência de brunt-vaisalla (salinidade absoluta, temperatura conservativa, sea pressure, lat=None, axis=0)
    n2 = gsw.Nsquared(sa, ct, pressao, 23)
    print(type(n2))
    print(n2)

    # como n2 é uma tupla, n2[0] é a frequência e n2[1] é a pressão, tramsforma em um dataframe do pandas de novo e salva em csv
    n2_df = pd.DataFrame({'Brunt-Väisälä Frequency': n2[0], 'Mid-Pressure': n2[1]})
    n2_df.to_csv('/home/labdino/PycharmProjects/CTDprocessing/dados/01. Dados Brutos/02_radial_LADCP/0635_29072019_2033/bruntvaisala.csv', index=False)

    return n2

def plotvaisala(n2):
    # plot da frequência de flutuabilidade, o output de n2 é uma tupla então n2[1] é a pressão e n2 [0] é a frequência
    pressures = n2[1]  # Extract pressures
    n2_values = n2[0]   # Extract Brunt-Väisälä frequency values

    plt.plot(pressures, n2_values)
    plt.xlabel('Pressão (dBar)')
    plt.ylabel('Frequência de Brunt-Väisälä (N^2)')
    plt.title('Perfil de Frequência de Brunt-Väisälä - 635')
    plt.grid(True)
    plt.savefig('/home/labdino/PycharmProjects/CTDprocessing/dados/01. Dados Brutos/02_radial_LADCP/0635_29072019_2033/bruntvaisala.png', format='png', dpi=900, transparent=False)

    plt.show()

def timecounter():
    # executa e cronometra cada função
    start_time = time.perf_counter()
    vaisala_result = bruntvaisala()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"bruntvaisala elapsed time: {elapsed_time} seconds")

    start_time = time.perf_counter()
    plotvaisala(vaisala_result)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"plotvaisala elapsed time: {elapsed_time} seconds")

timecounter()
