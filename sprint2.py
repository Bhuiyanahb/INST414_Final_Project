import pandas as pd
import seaborn as sns

# Load the data
data = pd.read_csv('smmh.csv')

summary_stats = data.describe()
print(summary_stats)



#calc mean and median
average_daily_usage = data['8. What is the average time you spend on social media every day?'].mean()
median_mental_health_score = data['18. How often do you feel depressed or down?'].median()
print("Average daily usage:", average_daily_usage, "hours.")
print("Median mental health score:", median_mental_health_score)

#calc standard deviation for depression
depression_std = data['18. How often do you feel depressed or down?'].std()
print("Standard deviation is:", depression_std)

# Frequency distribution for using social media without a specific purpose
usage_without_purpose_freq = data['9. How often do you find yourself using Social media without a specific purpose?'].value_counts()
print("Usage without purpose distribution:", usage_without_purpose_freq)

#Skewness of the data
sleep_issue_skew = data['20. On a scale of 1 to 5, how often do you face issues regarding sleep?'].skew()
print("Skewness of the sleep issues:", sleep_issue_skew)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('smmh.csv')

X = data[['8. What is the average time you spend on social media every day?']]  # Predictor
y = data['18. How often do you feel depressed or down?']  # Response

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

tree_model = DecisionTreeRegressor(random_state=42)
tree_model.fit(X_train, y_train)

# Linear Regression
cv_scores_lr = cross_val_score(linear_model, X, y, cv=10, scoring='neg_mean_squared_error')
print(f"CV RMSE Linear Regression: {np.sqrt(-cv_scores_lr.mean())}")

# Decision Tree
cv_scores_dt = cross_val_score(tree_model, X, y, cv=10, scoring='neg_mean_squared_error')
print(f"CV RMSE Decision Tree: {np.sqrt(-cv_scores_dt.mean())}")

# Predictions
pred_lr = linear_model.predict(X_test)
pred_dt = tree_model.predict(X_test)

# Metrics
rmse_lr = np.sqrt(mean_squared_error(y_test, pred_lr))
r2_lr = r2_score(y_test, pred_lr)
rmse_dt = np.sqrt(mean_squared_error(y_test, pred_dt))
r2_dt = r2_score(y_test, pred_dt)

print(f"Linear Regression RMSE: {rmse_lr}, R²: {r2_lr}")
print(f"Decision Tree RMSE: {rmse_dt}, R²: {r2_dt}")

models = ['Linear Regression', 'Decision Tree']
rmses = [rmse_lr, rmse_dt]

plt.bar(models, rmses, color=['blue', 'green'])
plt.ylabel('RMSE')
plt.title('Comparison of Model Performance')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data['Depression_Score'], bins=5, kde=True)
plt.title("Distribution of Depression Scores")
plt.xlabel("Depression Score (1-5)")
plt.ylabel("Frequency")
plt.show()