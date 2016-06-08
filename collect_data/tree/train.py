from sklearn import tree
from sklearn.externals.six import StringIO
import pickle

def load(filename):
    f = open(filename, 'r')
    u = pickle.Unpickler(f)
    obj = u.load()
    return obj
    
matches_features = load('matches_features')
result = load('result')
clf = tree.DecisionTreeClassifier()
clf = clf.fit(matches_features, result)

with open("matches.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)


