# -*- coding: utf-8 -*-
"""02_18241010_ShababIntisharRahman

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oL64TN0BGQMS_zWgqt2o2e_JALy1kJnv
"""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
income = pd.read_csv('/content/Income Dataset (50k).csv' )
income.head()

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn import svm
income = pd.read_csv('/content/Income Dataset (50k).csv' )
income = income.dropna()
income = income.drop(['education', 'capital-gain', 'capital-loss', ], axis = 1)
enc = LabelEncoder()
income['workclass'] = enc.fit_transform(income['workclass'])
income['marital-status'] = enc.fit_transform(income['marital-status'])
income['occupation'] = enc.fit_transform(income['occupation'])
income['race'] = enc.fit_transform(income['race'])
income['gender'] = enc.fit_transform(income['gender'])
income['native-country'] = enc.fit_transform(income['native-country'])
income['relationship'] = enc.fit_transform(income['relationship'])

income_feat  = ['age', 'educational-num','hours-per-week','marital-status','occupation','relationship','race','gender','hours-per-week','native-country']


income.head()

X = income.loc[:, income_feat ].values
Y = income.loc[:, ['income_>50K']].values
X_train, X_test, Y_train, Y_test = model_selection.train_test_split (X, Y,stratify=Y, test_size=0.2, random_state=0)

Y_train.shape
Y_train.ravel()


from sklearn.svm import SVC
svc = SVC(kernel="poly")
svc.fit(X_train, Y_train.ravel())

print("Training accuracy of the model is {:.2f}".format(svc.score(X_train, Y_train)))
print("Testing accuracy of the model is {:.2f}".format(svc.score(X_test, Y_test)))

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=50)
rfc.fit(X_train, Y_train.ravel())

print("The Training accuracy of the model is {:.2f}".format(rfc.score(X_train, Y_train)))
print("The Testing accuracy of the model is {:.2f}".format(rfc.score(X_test, Y_test)))

from sklearn.neural_network import MLPClassifier
nnc=MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
nnc.fit(X_train, Y_train.ravel())

print("The Training accuracy of the model is {:.2f}".format(nnc.score(X_train, Y_train)))
print("The Testing accuracy of the model is {:.2f}".format(nnc.score(X_test, Y_test)))

from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()

scaler.fit_transform(income.loc[:, income_feat ].values)

income.corr()

from sklearn.decomposition import PCA 
pca = PCA(n_components=5)
principal_components= pca.fit_transform(income.loc[:, income_feat ].values)
print(principal_components)

pca.explained_variance_ratio_

sum(pca.explained_variance_ratio_)

principal_df = pd.DataFrame(data=principal_components, columns=["principle component 1", "principle component 2", "principle component 3", "principle component 4", "principle component 5"])
#principal_df.head()
main_df=pd.concat([principal_df, income[["income_>50K"]]], axis=1)
main_df.head()

X= main_df.drop("income_>50K" , axis=1)
Y= main_df["income_>50K"]
x_train, x_test, y_train, y_test = train_test_split(X , Y , test_size=0.2, random_state=42)
from sklearn.svm import SVC
svc = SVC(kernel="poly")
svc.fit(X_train, Y_train.ravel())

print("Training accuracy of the model is {:.2f}".format(svc.score(X_train, Y_train)))
print("Testing accuracy of the model is {:.2f}".format(svc.score(X_test, Y_test)))

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=50)
rfc.fit(X_train, Y_train.ravel())

print("The Training accuracy of the model is {:.2f}".format(rfc.score(X_train, Y_train)))
print("The Testing accuracy of the model is {:.2f}".format(rfc.score(X_test, Y_test)))

from sklearn.neural_network import MLPClassifier
nnc=MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
nnc.fit(X_train, Y_train.ravel())

print("The Training accuracy of the model is {:.2f}".format(nnc.score(X_train, Y_train)))
print("The Testing accuracy of the model is {:.2f}".format(nnc.score(X_test, Y_test)))