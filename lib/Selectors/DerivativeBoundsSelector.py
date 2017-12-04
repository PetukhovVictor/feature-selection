import numpy as np
from scipy import interpolate


class DerivativeBoundsSelector:
    def select(self, features, params):
        x_lin = np.linspace(0, 1, len(features))
        y = []
        for feature in features:
            y.append(feature[1])

        f = interpolate.CubicSpline(x_lin, y)

        dfdx = f.derivative()
        dydx = dfdx(x_lin)
        indexes = np.where(
            (dydx > params['point'] - params['deviation']) & (dydx < params['point'] + params['deviation']))[0]

        if len(indexes) == 0:
            return features

        return features[0:indexes[0]] + features[:indexes[len(indexes) - 1]:len(features) - 1]
