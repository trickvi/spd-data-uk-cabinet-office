import os
import io
import csv
import operator
import requests


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'))
SOURCE_FILEPATH = os.path.join(DATA_DIR, 'sources.csv')
SOURCE_HEADERS = ['id', 'publisher_id', 'name', 'data', 'score', 'revision', 'schema', 'period_id', 'timestamp']

def run():
    response = requests.get('http://data.gov.uk/api/2/rest/package/financial-transactions-data-co')
    sources = response.json()['resources']
    sources = sorted(sources, key=operator.itemgetter('date'))
    schema = 'https://cdn.rawgit.com/okfn/spd-data-example/master/_sources/schema.json'

    with io.open(SOURCE_FILEPATH, mode='w+t', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(SOURCE_HEADERS)
        for source in sources:
            _data = [source['id'], 'gb_cabinet-office', source['id'], source['url'],
                     '', '', schema, source['date'], source['created']]
            writer.writerow(_data)

if __name__ == '__main__':
    run()
