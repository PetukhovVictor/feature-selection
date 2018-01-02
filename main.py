import json
import argparse
import operator
from os.path import isfile
from scipy import *

from lib.FeatureSelector import FeatureSelector
from lib.Helpers.TimeLogger import TimeLogger

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', nargs=1, type=str, help='file with feature statistic')
parser.add_argument('--output', '-o', nargs=1, type=str, help='file with selected features')

args = parser.parse_args()

input = args.input[0]
output = args.output[0]

criteria = [
    {
        'type': 'tail',
        'params': {
            'by': 'value',
            'bound': 50
        }
    },
    {
        'type': 'head',
        'params': {
            'by': 'value',
            'bound': 100000
        }
    },
    {
        'type': 'derivative_bounds',
        'params': {
            'point': math.tan(math.pi / 4),
            'deviation': 2
        }
    }
]

if not isfile(input):
    raise Exception('Input file dosn\'t exist')

time_logger = TimeLogger()

with open(input, 'r') as f:
    features = json.loads(f.read())

features_sorted = sorted(features.items(), key=operator.itemgetter(1))

fs = FeatureSelector(features_sorted, criteria)
features_selected = fs.select()
features_selected_json = json.dumps(features_selected)

with open(output, 'w') as f:
    f.write(features_selected_json)

total_time = time_logger.finish()
print(str(len(features_selected)) + ' of ' + str(len(features_sorted)) + ' features selected, total time: ' +
      str(total_time))
