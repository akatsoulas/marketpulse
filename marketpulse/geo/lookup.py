from django.conf import settings

import requests


MAPBOX_URL = 'http://api.tiles.mapbox.com/v4/%s/geocode/%s.json'


def get_first_mapbox_geocode_result(query):
    """
    Pass `query` string as the query to mapbox reverse geocoding API.
    Returns the first result, converted to a dictionary keyed on type
    (e.g. 'city', 'province', 'country', etc.)

    If an error happens, requests raises HTTPError.

    If no results are returned, returns an empty dictionary.
    """
    map_id = settings.MAPBOX_MAP_ID
    url = MAPBOX_URL % (map_id, query)

    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    # Convert first result to a dictionary indexed by result type
    if data.get('results'):
        result = data['results'][0]
        result = dict([(item['type'], item) for item in result])
        return result
    return {}
