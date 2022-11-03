import pandas as pd


# Importando o csv
paises = pd.read_csv('Paises.csv', delimiter=';')


# pega todas as 'Region' que possui 'OCEANIA'
oceania = paises.loc[paises['Region'].str.contains("OCEANIA")]
print ("\nOs países da Oceania são:")
print(oceania['Country'])
print(f"\nA Oceania possui {len(oceania['Country'])} países.")


# pega todas as linhas da coluna 9
literacy = paises.iloc[:,9]
worldLiteracy = pd.Series(literacy)
print(f"\nA taxa média de alfabetização do planeta é de {worldLiteracy.mean():.4f} %.")


populacao = paises['Population'].idxmax()
regiao = paises['Region'].values[populacao]
pais = paises['Country'].values[populacao]
maiorPopulacao = paises['Population'].values[populacao]
print(f"\n{pais}, que se localiza na {regiao}, possui a maior população com {maiorPopulacao} habitantes.")


semCosta = paises.loc[paises['Coastline (coast/area ratio)'] == 0]
paisesSemCosta = semCosta ['Country']
print(f"\nPaíses que não possuem costa marítima: ")
print(paisesSemCosta)
paisesSemCosta.to_csv('noCoast.csv', sep=';', header=False) # salvando em um novo arquivo