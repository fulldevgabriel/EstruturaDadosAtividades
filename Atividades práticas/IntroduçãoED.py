#HelipontosDF

import pandas as pd

colunas = ['Nome', 'localizacao']
nomeHeliporto = [
  "Península",
  "Parque Cidade",
  "Condomínio Brasil 21",
  "Raul Saboia",
  "SENAI/SESI/CNI",
  "Toca PCDF",
  "Base Resgate",
  "Parkway",
  "Residência Oficial de Águas Claras I",
  "Figaro"
]

locHeliporto = [
  "Ilha Serpente",
  "Vila Nova Horizonte",
  "Condomínio Estrela do Sul",
  "Rua dos Ventos",
  "Instituto Andrómeda",
  "Refúgio Lua Cheia",
  "Base Aurora",
  "Vale Encantado",
  "Palácio das Nuvens",
  "Aldeia dos Sonhos"
]

coordHeliporto = [
  "-15.7392, -47.9393",
  "-15.7334, -47.9055",
  "-15.7128, -47.9221",
  "-15.7204, -47.9882",
  "-15.7558, -47.9754",
  "-15.7357, -47.9809",
  "-15.6982, -47.8903",
  "-15.6847, -47.9517",
  "-15.7101, -47.9730",
  "-15.7253, -47.9334"
]



data = {
    'Nome': nomeHeliporto,
    'Localização': locHeliporto,
    'Coordenadas': coordHeliporto
}

df = pd.DataFrame(data)

print(df)