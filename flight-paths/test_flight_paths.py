import pytest
from __future__ import unicode_literals


TEST_JSON = [

    {
        'airport': 'Goma International Airport',
        'city': 'Goma',
        'connection_urls': ['https://en.wikipedia.org/wiki/Kindu_Airport',
        'https://en.wikipedia.org/wiki/Bangoka_International_Airport',
        'https://en.wikipedia.org/wiki/N%27djili_Airport',
        'https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport'],
        'country': 'Democratic Republic of the Congo',
        'destination_airports': ["N'djili Airport",
        'Bangoka International Airport',
        'Addis Ababa Bole International Airport'],
        'destination_cities': ['Kinshasa', 'Kisangani', 'Addis Ababa'],
        'destination_cities': ['Kisangani'],
        'lat_lon': [-1.669889, 29.238278],
        'url': 'https://en.wikipedia.org/wiki/Goma_International_Airport'
    },
    {
        'airport': 'Bangoka International Airport',
        'city': 'Kisangani',
        'connection_urls': ['https://en.wikipedia.org/wiki/Goma_International_Airport',
        'https://en.wikipedia.org/wiki/Kindu_Airport',
        'https://en.wikipedia.org/wiki/N%27djili_Airport'],
        'country': 'Democratic Republic of the Congo',
        'destination_airports': ['Goma International Airport', "N'djili Airport"],
        'destination_cities': ['Goma'],
        'lat_lon': [0.48167, 25.33806],
        'url': 'https://en.wikipedia.org/wiki/Bangoka_International_Airport'
    },
]
