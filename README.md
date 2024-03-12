# Heart Disease Prediction Based on Django and Machine Learning Project Report

**A Report for Data Processing Workshop I Final Project**

### ***Collaborators:***

Henry, Nick, Peter

### ***Supervisor:***

Dr. Changjiang ZHANG, Ms. Yiqi LIU

Data Science

Faculty of Science and Technology

Beijing Normal University-Hong Kong Baptist University United International College

# 1. Project Description

## 1.1 Background

Heart disease is a broad term used to describe a range of conditions that affect the heart. These conditions can include coronary artery disease, heart defects, heart infections, and heart failure. Heart disease is a leading cause of death worldwide, and it can be caused by a variety of factors, such as high blood pressure, high cholesterol levels, smoking, and a sedentary lifestyle. Symptoms of heart disease can include chest pain, shortness of breath, and an irregular heartbeat. Treatment for heart disease can vary depending on the specific condition, but it often includes medication, lifestyle changes, and sometimes surgery. Data analysis and prediction using machine learning can be incredibly valuable in the prevention of heart disease. By analyzing large amounts of medical data, machine learning algorithms can identify patterns and trends that may not be obvious to the human eye. This can help doctors and researchers better understand the causes of heart disease, and it can also help identify individuals who may be at high risk of developing the condition. Machine learning can also be used to make predictions about a person's likelihood of developing heart disease. By analyzing a variety of factors, such as a person's age, medical history, and lifestyle, machine learning algorithms can provide doctors with a better idea of which patients may be at risk. This can help doctors and healthcare providers take steps to prevent heart disease, such as prescribing medication or recommending lifestyle changes.

## 1.2 Propose & Functionalities

The purpose of our project is to use data analysis and machine learning to help prevent heart disease. By using data analysis methods, we will be able to uncover important information about heart disease, such as potential risk factors and trends in the data. We will then use this information to build a machine learning algorithm that can predict a person's likelihood of developing heart disease. The machine learning algorithm will be integrated into a Django website, where users can input their basic information (such as age, medical history, and lifestyle factors) and receive a prediction about their likelihood of developing heart disease. This will provide users with valuable information that can help them take steps to prevent the development of heart disease.

# 2. Data Description & Data Collecting

## 2.1 Data Collecting

It can be difficult to collect heart disease data using web scraping, as patient information is often protected and not readily available online. However, web scraping can still be a useful tool for gathering relevant data on heart disease. One potential source for this type of data is Kaggle, a website that hosts data sets and competitions for data scientists. On Kaggle, you may be able to find a data set on heart disease that has been collected and made available for use.

## 2.2 Data Description

The data set may include information on various factors that can affect heart health, such as patient demographics, medical history, and lifestyle habits. This information can be useful for research and analysis of heart disease trends and risk factors. Additionally, the data set may include details on the type and severity of heart disease present in each patient, as well as any treatment they have received.

# 3. Data Preprocessing

## 3.1 Steps of Exploratory Data Analysis

The first step in any data science project is exploratory data analysis (EDA). This involves cleaning and preparing the data for further analysis, as well as exploring the underlying patterns and relationships in the data.

### 3.1.1 Read the Data

One such project might be focused on heart disease. To begin, we would need to import the necessary libraries for our analysis, such as Pandas and Numpy. We would then load the dataset, which is typically a CSV file containing the data.

### 3.1.2 Remove the Outliers

Once the data is loaded, we would need to check for any outliers in the data. Outliers are observations that are significantly different from the rest of the data, and can skew our analysis if they are not dealt with properly. We can use various statistical methods, such as the interquartile range (IQR) method, to identify and remove these outliers.

### 3.1.3 Handling Missing Values

Next, we would need to check for any missing or null values in the dataset, and fill these in as necessary. This is an important step, as missing data can also impact our analysis. There are various methods for filling in missing data, such as using the mean or median value of the data.

## 3.2 Data Visualization

Once the data is cleaned and prepared, we can begin exploring it to uncover any patterns and relationships. This might involve looking at the distribution of different variables, such as age and blood pressure, and how they relate to heart disease. We can use various visualizations, such as histograms and scatter plots, to help us understand these relationships. 

Data visualization is an important tool in the data processing of heart disease data. By creating visual representations of data, such as graphs and charts, it becomes much easier to identify trends and patterns that may not be immediately obvious in raw data. This allows healthcare professionals to quickly and effectively analyze large amounts of data, and make informed decisions about how to treat and prevent heart disease. In addition, data visualization can also be used to communicate information to patients and the general public, making it easier for them to understand complex medical concepts and make informed decisions about their own health.

## 3.3 The Preparation for Future Work

The work we do in the initial exploratory data analysis phase is also beneficial for our later work in machine learning and building a Django website. By cleaning and preparing the data, we ensure that it is in a usable format for building predictive models. We also gain a better understanding of the data through our exploration, which can inform our machine learning algorithms and help us build a more effective Django website. Overall, the EDA phase is an important foundation for the rest of our project, and sets us up for success in our subsequent work.

# 4. Feature Engineering

## 4.1 Data Balancing

![截屏2022-12-12 下午5.41.07.png](Heart%20Disease%20Prediction%20Based%20on%20Django%20and%20Machi%204072f2c8c6444a11be5573c97397fe61/%25E6%2588%25AA%25E5%25B1%258F2022-12-12_%25E4%25B8%258B%25E5%258D%25885.41.07.png)

Our dataset is unbalanced in terms of targets, and the Target Figure shows that there are fewer 1's than 0's, so we randomly select the rows with targets equal to 1 and randomly place them in the dataset, placing the number of 0's equal to 1

Having a balanced dataset is important in machine learning because it helps the model to learn to classify the different target classes more accurately. This is because the model will have an equal number of examples of each class to learn from, so it is less likely to bias towards one class over the others.

Because dataset is balanced, the model is less likely to bias towards predicting one class over the others. As a result, the model's predictions on the test set are likely to be more accurate, and the overall performance of the model is likely to be better.

Having a balanced dataset is important for machine learning models to learn to classify the different target classes accurately. In the case of a heart disease prediction model, a balanced dataset can improve the model's performance and help it to make more accurate predictions.

## 4.2 Data Splitting

We split the heart disease dataset into 70% training set and 30% test set.

Dividing a dataset into a training set and a test set is important in machine learning because it allows us to train a model on a subset of the data and evaluate its performance on a separate, independent subset of the data. This is essential for developing accurate and reliable machine learning models for heart disease prediction.

## 4.3 Data Normalization

Data normalization is the process of transforming a dataset into a form that is more suitable for analysis.

There are several reasons why data normalization is important for a heart disease dataset. First, normalization can help to make the data more consistent and easier to work with, which can make it more straightforward to perform statistical analyses or to build machine learning models. Second, normalization can help to improve the accuracy and reliability of these analyses and models, by ensuring that the data is in a form that is more suitable for the specific tasks at hand. Finally, normalization can help to identify and remove any errors, inconsistencies, or other issues in the dataset that might otherwise bias or distort the results.

# 5. Machine Learning

## 5.1 Model Training

Model training is the process of building a machine learning model based on a given dataset. In the context of heart disease prediction, this would involve using a variety of different algorithms and techniques to build models that can accurately predict the presence or absence of heart disease based on a set of input data.

Select an algorithm and technique: Next, the specific algorithm and technique that will be used to train the model must be selected. In the context of heart disease prediction, this might include algorithms such as logistic regression, support vector machines (SVM), k-nearest neighbors (kNN), decision trees, random forests, and gradient boosting.

Once the algorithm and technique have been selected, the model can be trained using the prepared data. This involves applying the selected algorithm and technique to the data, and adjusting the model's parameters and settings to optimize its performance.

## 5.2 Model **Evaluation**

### 5.2.1 Confusion Matrix & Classification Report

In order to evaluate the performance of a machine learning model for predicting heart disease, several metrics can be used. Our evaluate the model is by using a confusion matrix, which is a table that shows the number of true positive, true negative, false positive, and false negative predictions made by the model. The classification report is another way to evaluate the model, and it provides several metrics such as precision, recall, and f1-score for each class. 

### 5.2.2 ROC-AUC

Another metric that we used to evaluate a binary classification model such as one for predicting heart disease is the receiver operating characteristic (ROC) curve and the area under the curve (AUC) metric. The ROC curve plots the true positive rate (TPR) against the false positive rate (FPR) at different classification thresholds, and the AUC metric provides a single number that represents the model's ability to distinguish between the positive and negative classes.

![截屏2022-12-14 上午10.07.46.png](Heart%20Disease%20Prediction%20Based%20on%20Django%20and%20Machi%204072f2c8c6444a11be5573c97397fe61/%25E6%2588%25AA%25E5%25B1%258F2022-12-14_%25E4%25B8%258A%25E5%258D%258810.07.46.png)

### 5.2.3 K-Fold Cross-Validation

In addition to these metrics, it is also to use k-fold cross-validation to evaluate the performance of a machine learning model. In k-fold cross-validation, the original dataset is split into k smaller subsets, and the model is trained and evaluated k times, each time using a different subset as the test set and the remaining k-1 subsets as the training set. The final evaluation score is the average of the k scores obtained from the k iterations. This method helps to reduce the variance in the model's performance and provides a more reliable evaluation of the model.

### 5.2.4 Model **Evaluation Summary**

![截屏2022-12-14 上午10.30.41.png](Heart%20Disease%20Prediction%20Based%20on%20Django%20and%20Machi%204072f2c8c6444a11be5573c97397fe61/%25E6%2588%25AA%25E5%25B1%258F2022-12-14_%25E4%25B8%258A%25E5%258D%258810.30.41.png)

## 5.3 Model Turning

### 5.3.1 Model Turning Principle

The Model Turning for heart disease dataset by GridSearchCV involves using a dataset of patient data to train a model that can predict heart disease. The dataset typically contains information about patients, such as their age, sex, and various medical measurements, such as blood pressure and cholesterol levels. The goal of the model is to learn from this data and make accurate predictions about whether a patient has heart disease or not

The Model Turning process involves splitting the dataset into training and validation sets, and then using the training set to fit a model with various combinations of parameters. The fitted models are then evaluated on the validation set using a performance metric, such as accuracy or precision. The model with the best performance on the validation set is then chosen as the final model. This trained model can then be used to make predictions on new, unseen data.

### 5.3.2 Models After Model Turning:

![截屏2022-12-14 上午10.31.06.png](Heart%20Disease%20Prediction%20Based%20on%20Django%20and%20Machi%204072f2c8c6444a11be5573c97397fe61/%25E6%2588%25AA%25E5%25B1%258F2022-12-14_%25E4%25B8%258A%25E5%258D%258810.31.06.png)

## 5.4 Model Weighting

In order to combine the predictions of multiple machine learning models for a heart disease dataset, we can use a method called ensemble learning. One way to do this is by using a VotingClassifier, which allows us to train multiple models and combine their predictions by majority vote.

We have trained a logistic regression model, a support vector machine (SVM) model, a k-nearest neighbors (kNN) model, a decision tree model, a random forest model, and a gradient boosting model for the heart disease dataset, and then use a VotingClassifier to combine their predictions. We can specify different weights for each model's contribution to the final prediction, and the VotingClassifier will use these weights to determine the final prediction.

This approach can often improve the performance of the individual models by leveraging their complementary strengths and reducing their overfitting to the training data. However, it is important to carefully evaluate the performance of the ensemble model to ensure that it is not under-fitting or overfitting to the data.

The graph shows below demonstrate the Accuracy, Precision, Recall, F1-Score and AUC value after model weighting. 

![截屏2022-12-14 上午10.09.35.png](Heart%20Disease%20Prediction%20Based%20on%20Django%20and%20Machi%204072f2c8c6444a11be5573c97397fe61/%25E6%2588%25AA%25E5%25B1%258F2022-12-14_%25E4%25B8%258A%25E5%258D%258810.09.35.png)

# 6. Web Development

Our Django website allows users to learn more about heart disease and its potential risks. 

## 6.1 Login & Register

Our website has a login and a registration screen where you can enter your username, password (which is hidden when you enter it) and choose your identity (patient alive doctor). The login screen allows you to enter your username and password, and automatically detects your identity at the time of registration.

## 6.2 Users

For registered patients, the website provides a prediction tool that uses machine learning algorithms to assess their potential for developing heart disease. For doctors, the website provides access to a database of patient information, allowing them to easily view and manage their patients' data.

## 6.3 Heart Disease Prediction

One of the key features of our Django website is its predictive tool for registered patients. Using machine learning algorithms trained on our cleaned and prepared heart disease data, the tool provides an assessment of a user's potential for developing heart disease. This can help patients and their doctors make informed decisions about their health and treatment plans. 

## 6.4 HDP Database

Additionally, the website's database of patient information allows doctors to easily view and manage their patients' data, improving the efficiency and effectiveness of their care. Overall, our Django website provides valuable resources for both patients and doctors in managing heart disease.

# 7. Difficulties & Solutions

As with any data science project, there were several challenges and difficulties that we encountered during our work on heart disease. One of the main challenges was our lack of familiarity with data processing techniques and machine learning algorithms. To address this, we spent time researching and learning about these topics, and sought guidance from experts in the field.

Another challenge was our limited experience with building websites, particularly using the Django framework. To overcome this challenge, we spent time learning and researching the necessary skills on our own, and were able to gain proficiency in web development and the Django framework.

To conclude, while there were challenges along the way, we were able to overcome them through determination, research, and seeking guidance from teachers. This allowed us to successfully complete our project and build a valuable resource for patients and doctors alike.

## Reference

[1] Yahaya, L., Oye, N. D., & Garba, E. J. (2020). A comprehensive review on heart disease prediction using data mining and machine learning techniques. *American Journal of Artificial Intelligence*, *4*(1), 20-29.

[2] Sekar, J., Aruchamy, P., Sulaima Lebbe Abdul, H., Mohammed, A. S., & Khamuruddeen, S. (2022). An efficient clinical support system for heart disease prediction using TANFIS classifier. *Computational Intelligence*, *38*(2), 610-640.

[3] Ramalingam, V. V., Dandapath, A., & Raja, M. K. (2018). Heart disease prediction using machine learning techniques: a survey. *International Journal of Engineering & Technology*, *7*(2.8), 684-687.

[4] Narkhede, S. (2018). Understanding auc-roc curve. *Towards Data Science*, *26*(1), 220-227.

[5] Huang, J., & Ling, C. X. (2005). Using AUC and accuracy in evaluating learning algorithms. *IEEE Transactions on knowledge and Data Engineering*, *17*(3), 299-310.

[6] Fushiki, T. (2011). Estimation of prediction error by using K-fold cross-validation. *Statistics and Computing*, *21*(2), 137-146.

[7 ] Vladislavleva, E., Smits, G., & Den Hertog, D. (2009). On the importance of data balancing for symbolic regression. *IEEE Transactions on Evolutionary Computation*, *14*(2), 252-277.
