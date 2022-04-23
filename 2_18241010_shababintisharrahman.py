# -*- coding: utf-8 -*-
"""2_18241010_shababIntisharRahman

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qe3FuOofLUMSb-nET4Sp03iHMsRolQVC
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
income = income.drop(['education', 'relationship', 'capital-gain', 'capital-loss', 'native-country', ], axis = 1)
enc = LabelEncoder()
work_enc = pd.get_dummies(income['workclass'])
work_enc.head()
income['workclass'].head()
mar_enc = pd.get_dummies(income['marital-status'])
mar_enc.head()
race_enc = pd.get_dummies(income['race'])
gen_enc = pd.get_dummies(income['gender'])
occ_enc = pd.get_dummies(income['occupation'])
income_feat  = ['age', 'educational-num','hours-per-week']



income.head()

X = income.loc[:, income_feat ].values
#X = income.loc[:, : -1 ].values
Y = income.loc[:, ['income_>50K']].values
#Y = income.loc[:, -1 ].values
X_train, X_test, Y_train, Y_test = model_selection.train_test_split (X, Y, test_size=0.2, random_state=0)
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train, Y_train)
prediction = model.predict(X_test)
print(prediction)

pre = accuracy_score(Y_test, prediction)
print(pre)

from pandas.core.common import random_state
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = income.loc[:, income_feat ].values
#X = income.loc[:, : -1 ].values
Y = income.loc[:, ['income_>50K']].values
#Y = income.loc[:, -1 ].values
X_train, X_test, Y_train, Y_test = model_selection.train_test_split (X, Y, test_size=0.2, random_state=0)

clf = DecisionTreeClassifier(criterion = 'entropy', random_state = 1)
clf.fit(X_train, Y_train)
ypred = clf.predict(X_test)
score = accuracy_score(Y_test, prediction)
print (score)

import numpy as np
import matplotlib.pyplot as plt
 
data = {'Decision Tree':score, 'Regression': pre}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 

plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("methods")
plt.ylabel("accuracy")
plt.title("accuracy comparison")
plt.show()