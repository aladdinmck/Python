<<<<<<< HEAD
# I've created this in order to 
# learn Scikit-learn briefly 

# Python script using Scikit-learn 
# for Decision Tree Classifier

# Sample Decision Tree Classifier 
from sklearn import datasets
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier

# load the iris datasets 
dataset = datasets.load_iris()

# fit a CART model to the data 
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(model)

# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
=======
# Python script using Scikit-learn  
# for Decision Tree Clasifier 
  
# Sample Decision Tree Classifier 
from sklearn import datasets 
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier 
  
# load the iris datasets 
dataset = datasets.load_iris() 
  
# fit a CART model to the data 
model = DecisionTreeClassifier() 
model.fit(dataset.data, dataset.target) 
print(model) 
  
# make predictions 
expected = dataset.target 
predicted = model.predict(dataset.data) 
  
# summarize the fit of the model 
print(metrics.classification_report(expected, predicted)) 
>>>>>>> 0c931757d53680396fa67280d6b527ca93ad188b
print(metrics.confusion_matrix(expected, predicted))
