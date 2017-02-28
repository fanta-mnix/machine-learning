from sklearn.feature_selection import f_regression


def create_interactions(X):
    interactions = X.copy()
    for feature_a in X:
        for feature_b in X:
            if feature_a > feature_b:
                interactions['{} * {}'.format(feature_a, feature_b)] = X[feature_a] * X[feature_b]
        interactions['{} * {}'.format(feature_a, feature_a)] = X[feature_a] * X[feature_a]

    return interactions


def score_features(X, y):
    f_regression(X, y)


#  F-test
# [(460.65647274586092, 'RM'),
#  (668.7235158135851, 'LSTAT'),
#  (179.57156528039974, 'PTRATIO'),
#  (632.59314407749389, 'RM * LSTAT'),
#  (1.7387467537056727, 'RM * PTRATIO'),
#  (533.63937869220888, 'RM * RM'),
#  (365.17851177390713, 'LSTAT * LSTAT'),
#  (748.91444579648237, 'PTRATIO * LSTAT'),
#  (186.86355836745318, 'PTRATIO * PTRATIO')]