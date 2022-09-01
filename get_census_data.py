import requests
import json

# Set base url
base_url = "https://api.census.gov/data/2018/{data_source}"

# Get api-key and format url
with open('keyfile.txt') as file:
    my_key = file.read().strip()

my_key = "1b7f00b83378b54ab35dc2419b2f3c6e574aa447"

data_url = base_url+"?get={cols}&for={level}:{level_selection}&key={api_key}"

def format_cols_for_query(*fields):
    res = ""
    for field in fields:
        res += field+","
    
    return res[:-1]

def query_census_api(source, *cols, geography, geography_selection='*'):
    query_url = data_url.format(data_source=source, cols=format_cols_for_query(*cols), level=geography, level_selection=geography_selection, api_key=my_key)
    res = requests.get(query_url)
    return res

def format_api_res(res):
    # Takes the string returned by query_census_api and returns it as df
    data_list = json.loads(res)

def get_query_url(source, *cols, geography, geography_selection='*'):
    query_url = data_url.format(data_source=source, cols=format_cols_for_query(*cols), level=geography, level_selection=geography_selection, api_key=my_key)
    return query_url

query_res = query_census_api('abscs', 'GEO_ID', 'NAME', 'NAICS2017', 'NAICS2017_LABEL', 'EMP', geography='state', geography_selection=34)

print(query_res)
with open('sample_response.json', 'w') as outfile:
    outfile.write(json.dumps(query_res.json()))