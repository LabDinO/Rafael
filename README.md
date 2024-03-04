*Repositório do aluno Rafael S. Bittencourt*

<h1 align="center"> CTD Processing Package</h1>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=Versão&message=V.1.7.11&color=GREEN&style=for-the-badge)

# Descrption
This is a project developed by Rafael S. Bittencourt, oceanography student working at the Ocean Dynamics Laboratory at UFSC.
The objective is to develop a python program for pre-processing CTD data.

# How to install it
```pip install CTDProcessingPackage```

# Requirements
To be able to use all the CTDProcessingPackage functions, the CTD data file must be a Pandas dataframe, so don't forget to: 
```Python
import pandas as pd

data = pd.read_csv('PATH')
```

# How to use it
```Python
import ctdmodule as ctd
```
# Package functions
- plot: plot a simple temperature profile
- plot_perfil_termosal: plot a temperature and salinity profile together
- diagramats: plot a T-S diagram with density isolines
- convert: convert the decimal and thousands separator
- downcast: overwrite the data maintaining only the CTD dowcast data
- remove_outliers: remove the data outliers using the 3-sigma method
- above_sea_level: remove the data collected above the sea level
- pressure_loops: remove the pressure loops from the data
- bin_average: bin averaging

# Attention!
The pressure, temperature and salinity columns MUST be named respectively as: PRESSURE;DBAR , TEMPERATURE;C , Calc. SALINITY; PSU 

# Quick Start
Check the quickstart.ipynb notebook at the CTDProcessingPackage folder for a quick start guide on the package functions.

# Examples
Here is a temperature profile of a data without any pre-processing:

![Perfil de dados brutos](https://github.com/faelvulgo/CTDprocessing/blob/master/perfis/Perfil_bruto.png)

We can see noises and loops in this data, so after using some functions of the package we will have something like this:

![Perfil depois de todas as etapas de processamento](https://github.com/faelvulgo/CTDprocessing/blob/master/perfis/Perfil_binado.png)

<h1 align="center"> Internal Waves </h1>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=Versão&message=V.1.1.2&color=GREEN&style=for-the-badge)

# Descrição
Projeto para calcular a frequência de Brunt-vaisalla para ser usado na identificação de ondas internas.
É utilizado o toolbox GSW (Gibbs SeaWater) para calcular a salinidade absoluta, temperatura conservativa e por fim a frequência de flutuabilidade.

O código consiste de três funções: bruntvaisala, plotvaisala e timecounter

- bruntvaisala: calcula a salinidade absoluta a partir da salinidade prática, temperatura conservativa a partir da salinidade absoluta e temperatura in situ, retorna uma tupla com N2 e pressão;
- plotvaisala: plota o gráfico da frequência de flutuabilidade (N2) em função da pressão;
- timecounter: executa todas as funções cronometrando seu tempo de resposta.

# Exemplo
Exemplo abaixo da imagem gerada depois de todas as funções serem executadas:
![Plot da Frequência de Flutuabilidade](InternalWaves/Perfis/bruntvaisala.png)

