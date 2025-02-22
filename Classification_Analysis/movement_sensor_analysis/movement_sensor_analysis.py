import numpy as np
import pandas as pd
#피처 이름 파일 읽어오기
feature_name_df = pd.read_csv('./UCI_HAR_Dataset/features.txt', sep = ' ',
                                           header = None, names = ['index',
                                           'feature_name'], engine = 'python')
#index 제거하고, feature_name만 리스트로 저장
feature_name = feature_name_df['feature_name'].tolist()
feature_name_tuple = tuple(feature_name)

unique_feature_name = []
feature_count = {}
for name in feature_name: 
    if name in feature_count:
        feature_count[name] += 1
        unique_feature_name.append(f"{name}_{feature_count[name]}")
    else:
        feature_count[name] = 0
        unique_feature_name.append(name)
feature_name_tuple=unique_feature_name

X_train = pd.read_csv('./UCI_HAR_Dataset/train/X_train.txt', sep='\s+', names = feature_name_tuple, engine = 'python')
X_test = pd.read_csv('./UCI_HAR_Dataset/test/X_test.txt', sep='\s+', names = feature_name_tuple, engine = 'python')
Y_train = pd.read_csv('./UCI_HAR_Dataset/train/y_train.txt', sep='\s+', header = None, names = ['action'], engine = 'python')
Y_test = pd.read_csv('./UCI_HAR_Dataset/test/y_test.txt' , sep = '\s+', header = None, names = ['action'], engine = 'python')
label_name_df = pd.read_csv('./UCI_HAR_Dataset/activity_labels.txt', sep = '\s+', header = None, names = ['index', 'label'], engine = 'python')
label_name = label_name_df.iloc[:, 1].values.tolist()
from sklearn.tree import DecisionTreeClassifier
dt_HAR = DecisionTreeClassifier(random_state=156)
dt_HAR.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

params = {
 'max_depth' : [8, 16, 20],
 'min_samples_split' : [8, 16, 24]
}

grid_cv = GridSearchCV(dt_HAR, param_grid = params, scoring = 'accuracy', cv = 5, return_train_score = True)
grid_cv.fit(X_train, Y_train)
GridSearchCV(cv = 5, estimator = DecisionTreeClassifier(random_state = 156), param_grid = {'max_depth': [8, 16, 20],
                  'min_samples_split': [8, 16, 24]}, return_train_score
                  = True, scoring = 'accuracy')
cv_results_df = pd.DataFrame(grid_cv.cv_results_)

print(cv_results_df[['param_max_depth', 'param_min_samples_split', 'mean_test_score', 'mean_train_score']])

best_dt_HAR = grid_cv.best_estimator_
best_Y_predict = best_dt_HAR.predict(X_test)
best_accuracy = accuracy_score(Y_test, best_Y_predict)

print('best 결정 트리 예측 정확도: {0:.4f}'.format(best_accuracy))

