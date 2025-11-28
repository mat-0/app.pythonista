"""
Get the latest 10 days of covid data from the uk GOV API
for a given city defaulted to Cheltenham.
V1 of the API, now broken
"""

import os
import pathlib

from requests import get


def get_covid_data(num_days):
    """
    Get the latest 10 days of covid data for a given city
    """
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        f'filters=areaType=ltla;areaName={city}&'
        'structure={"date":"date",'
        '"newCases":"newCasesByPublishDate",'
        '"deaths":"newDeathsByDeathDate"}'
    )
    response = get(endpoint, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
    string_builder = ""
    data = response.json()['data'][:num_days]
    for i in range(0, num_days):
        string_builder += f"{data[i]['date']} - {data[i]['newCases']}\n"
    return string_builder


if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()
    city = os.getenv('city_code') or 'Cheltenham'
    string_output = get_covid_data(10)
    print(string_output)
