class EndsSelector:
    def __init__(self, end_type):
        self.end_type = end_type

    def get_residue_by_order(self, features, bound):
        if self.end_type == 'head':
            return features[:len(features) - bound]
        elif self.end_type == 'tail':
            return features[:bound]
        else:
            raise Exception('Unsupported EndsSelector type')

    def get_residue_by_value(self, features, bound):
        if self.end_type == 'head':
            index = 0
            for feature in reversed(features):
                if feature[1] <= bound:
                    break
                index += 1
            return features[:len(features) - index]
        elif self.end_type == 'tail':
            index = 0
            for feature in features:
                if feature[1] >= bound:
                    break
                index += 1
            return features[index:]
        else:
            raise Exception('Unsupported EndsSelector type')

    def select(self, features, params):
        features_selected = {}

        if params['by'] == 'order':
            features_selected = self.get_residue_by_order(features, params['bound'])
        elif params['by'] == 'value':
            features_selected = self.get_residue_by_value(features, params['bound'])

        return features_selected
