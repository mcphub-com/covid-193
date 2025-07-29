import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api-sports/api/covid-193'

mcp = FastMCP('covid-193')

@mcp.tool()
def countries(search: Annotated[Union[str, None], Field(description='allows to search for a country')] = None) -> dict: 
    '''Get all available countries'''
    url = 'https://covid-193.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'covid-193.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def statistics(country: Annotated[Union[str, None], Field(description='Name of the country')] = None) -> dict: 
    '''Get all current statistics for all countries'''
    url = 'https://covid-193.p.rapidapi.com/statistics'
    headers = {'x-rapidapi-host': 'covid-193.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def history(country: Annotated[str, Field(description='Name of the country, [All] For global History')],
            day: Annotated[Union[str, datetime, None], Field(description='Filter by day')] = None) -> dict: 
    '''Get historical statistics for a country'''
    url = 'https://covid-193.p.rapidapi.com/history'
    headers = {'x-rapidapi-host': 'covid-193.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'day': day,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
