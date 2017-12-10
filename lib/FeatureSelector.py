from .Selectors.EndsSelector import EndsSelector
from .Selectors.DerivativeBoundsSelector import DerivativeBoundsSelector


class FeatureSelector:
    supported_selectors = {
        'head': EndsSelector('head'),
        'tail': EndsSelector('tail'),
        'derivative_bounds': DerivativeBoundsSelector()
    }

    def __init__(self, features, criteria):
        self.features = features
        self.criteria = criteria

    def select(self):
        feature_selected = self.features
        for selector in self.criteria:
            if selector['type'] not in self.supported_selectors:
                raise Exception('Unsupported selector')
            feature_selected = self.supported_selectors[selector['type']]\
                .select(feature_selected, selector['params'])

        return feature_selected
