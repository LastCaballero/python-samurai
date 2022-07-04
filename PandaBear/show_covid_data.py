#! /usr/bin/python3.8

import pandas as pd
import os
import requests

filename = 'owid-covid-data.csv' 
url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'

if ( not os.path.exists( filename ) ):
	resp = requests.get( url, "wb" )
	open(filename, "wb").write(resp.content)

cov = pd.read_csv("owid-covid-data.csv")

germany = cov.location == 'Germany'
desired_columns = [
	"date",
	"reproduction_rate",
	"icu_patients_per_million",
	"positive_rate"
]

germany_sev_columns = cov[ germany ][ desired_columns ].tail(200)
print( "data from germany:" )
print( germany_sev_columns.to_string(),"\n" )

countries = cov.groupby("location")
populus = countries.population.last().sort_values().to_string()
print( "world population comparison: " )
print( populus, "\n" )

populus_and_density = countries[["population","population_density"]].last().sort_values(by=["population_density"]).to_string()
print( "\npopulation and density compared: " )
print( populus_and_density )

