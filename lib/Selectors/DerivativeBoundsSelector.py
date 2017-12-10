class DerivativeBoundsSelector:
    def select(self, features, params):
        features_selected = []
        feature_prev = None
        for feature in features:
            if feature_prev:
                discrete_derivative = feature_prev[1] - feature[1]

                if discrete_derivative < params['point'] - params['deviation'] or discrete_derivative > params['point'] + params['deviation']:
                    features_selected.append(feature)

            feature_prev = feature

        return features_selected
