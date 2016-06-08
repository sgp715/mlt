from sklearn import tree
import pickle

def load(filename):
    f = open(filename, 'r')
    u = pickle.Unpickler(f)
    obj = u.load()
    return obj

test_matches_features = load('test_matches_features')
test_result = load('test_result')
matches_features = load('matches_features')
result = load('result')


clf = tree.DecisionTreeClassifier()
clf = clf.fit(matches_features, result)
prediction_list = clf.predict(test_matches_features)

correct = 0
for i, prediction in enumerate(prediction_list):
    print "prediction: " + str(prediction)
    print "result: " + str(result[i])
    if prediction == result[i]:
        correct += 1
        
accuracy = float(correct) / float(len(test_result))

print accuracy
        


