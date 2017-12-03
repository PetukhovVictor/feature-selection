import json
import argparse
from os.path import isfile
from scipy import *

from lib.FeatureSelector import FeatureSelector

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', nargs=1, type=str, help='file with feature statistic')
parser.add_argument('--output', '-o', nargs=1, type=str, help='file with selected features')

args = parser.parse_args()

input = args.input[0]
output = args.output[0]

criteria = [
    {
        'type': 'bottom',
        'params': {
            'by': 'value',
            'bound': 50
        }
    },
    {
        'type': 'top',
        'params': {
            'by': 'value',
            'bound': 50000
        }
    },
    {
        'type': 'derivative_bounds',
        'params': {
            'value': math.tan(math.pi / 4),
            'deviation': 0.178
        }
    }
]

if not isfile(input):
    raise Exception('Input file dosn\'t exist')
f = open(input, 'r')
features = json.loads(f.read())
f.close()

fs = FeatureSelector(features, criteria)
features_selected = fs.select()
print(len(features_selected))

f = open(output, 'w')
features_selected_json = json.dumps(features_selected)
f.write(features_selected_json)
f.close()
