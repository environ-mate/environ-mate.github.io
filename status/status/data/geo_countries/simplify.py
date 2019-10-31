import os
import json
from glob import glob

import geodaisy.converters as convert
import visvalingamwyatt as vw

for json_file in glob('*.json'):
    print(json_file)

    with open(json_file, 'r') as fh_in:
        j = json.load(fh_in)
        shape = j['View'][0]['Result'][0]['Location']['Shape']['Value']

        try:
            shape = json.loads(convert.wkt_to_geojson(shape))
            shape = vw.simplify_geometry(shape, ratio=0.2)
            j['View'][0]['Result'][0]['Location']['Shape']['Value'] = convert.geojson_to_wkt(shape)
        except (ValueError, TypeError):
            print('>>>>')

        with open('{}-simplified{}'.format(*os.path.splitext(json_file)), 'w') as fh_out:
            json.dump(j, fh_out)

