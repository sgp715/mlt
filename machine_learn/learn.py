import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import NearestNeighbors
from utility import *
from sklearn import cross_validation
    
# get features
features = np.asarray(load('data'))
results = np.asarray(load('data_result'))

def cross(clf, features, results):

    scores = cross_validation.cross_val_score(clf, features, results, cv = 10)  
    avg_score = 0.0
    for score in scores:
        avg_score += score
    avg_score /= float(len(scores))
    
    return avg_score
    

def train(clf, name):

    # do cross-validation
    score = cross(clf, features, results)
    #print "cross-validation: " + str(score)

    # train a model on all the data and save
    clf = clf.fit(features, results) 
    save(clf, name)
    
    return (clf, score)


# creat the classifier
tree_clf = tree.DecisionTreeClassifier()
bayes_clf = GaussianNB()
#nearest_clf = NearestNeighbors()
#neural_clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

trained_tree = train(tree_clf, "tree_clf")
trained_bayes = train(bayes_clf, "bayes")
#trained_nearest = train(nearest_clf, "nearest")
#trained_neural = train(neural_clf,"neural")

positive = 0
negative = 0
for result in results: 
    if result  == 1:
        positive += 1
    elif result == 0:
        negative +=1

print "base score: " + str(positive/ float(positive + negative))
print "cross validation on tree: " + str(trained_tree[1])
print "cross validation on bayes: " + str(trained_bayes[1])
#print "cross validation on bayes: " + str(trained_nearest[1])
#print "cross validation on :" + str()


#with open("tree.dot", 'w') as f:
#    f = tree.export_graphviz(clf, out_file=f)


