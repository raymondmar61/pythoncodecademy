#https://www.codecademy.com/learn/machine-learning

#Why Use Machine Learning?  Interactive lesson.
'''
The year is 2049...

Neo York is overrun by bots and web crawlers. The capabilities of Machine Learning have reached new heights and the world as we know it will never be the same:

Facial recognition technology that helps users tag and share photos of friends can now tag future friends; night drones are on the prowl.

Machine learning powered self-driving cars (and flying cars) are now massively available to consumers. The steering wheel has become a thing of the past.

Recommendation engines that suggest what VR shows to watch and what products to buy will now display a different environment for each user group.

At the dawn of a new age, you can't help but wonder, what is Machine Learning and how did it pivot our world so drastically?
'''
'''
What is Machine Learning?

While at IBM, Arthur Samuel developed a program that learned how to play checkers. He called it — "the field of study that gives computers the ability to learn without being explicitly programmed" (1959).

What does this mean?

As programmers, we often approach problems in a methodical, logic-based way. We try to determine what our desired outputs should be, and then create the proper rules that will transform our inputs into those outputs.

Machine learning flips the script. We want the program itself to learn the rules that describe our data the best, by finding patterns in what we know and applying those patterns to what we don't know.

These algorithms are able to learn. Their performance gets better and better with each iteration, as it uncovers more hidden trends in the data.
'''
'''
Supervised Learning
Machine learning can be branched out into the following categories:  Supervised Learning and Unsupervised Learning.

Supervised Learning is where the data is labeled and the program learns to predict the output from the input data. For instance, a supervised learning algorithm for credit card fraud detection would take as input a set of recorded transactions. For each transaction, the program would predict if it is fraudulent or not.

Supervised learning problems can be further grouped into regression and classification problems.

Regression:  In regression problems, we are trying to predict a continuous-valued output. Examples are:  What is the housing price in Neo York?  What is the value of cryptocurrencies?

Classification:  In classification problems, we are trying to predict a discrete number of values. Examples are:  Is this a picture of a human or a picture of an AI?  Is this email spam?
'''
'''
Unsupervised Learning
Unsupervised Learning is a type of machine learning where the program learns the inherent structure of the data based on unlabeled examples.

Clustering is a common unsupervised machine learning approach that finds patterns and structures in unlabeled data by grouping them into clusters.  Some examples:  Social networks clustering topics in their news feed, Consumer sites clustering users for recommendations, Search engines to group similar objects in one cluster.
'''
'''
Supervised Learning: data is labeled and the program learns to predict the output from the input data
Unsupervised Learning: data is unlabeled and the program learns to recognize the inherent structure in the input data
'''
'''
Scikit-Learn Cheatsheet
Open-source ML library for Python. Built on NumPy, SciPy, and Matplotlib.  https://scikit-learn.org/stable/

Linear Regression
Import and create the model:  from sklearn.linear_model import LinearRegression; your_model = LinearRegression()
Fit:  your_model.fit(x_training_data, y_training_data)
	.coef_: contains the coefficients
	.intercept_: contains the intercept
Predict:  predictions = your_model.predict(your_x_data)
	.score(): returns the coefficient of determination R²

Naive Bayes
Import and create the model:  from sklearn.naive_bayes import MultinomialNB; your_model = MultinomialNB()
Fit:  your_model.fit(x_training_data, y_training_data)
Predict:  # Returns a list of predicted classes - one prediction for every data point; predictions = your_model.predict(your_x_data); # For every data point, returns a list of probabilities of each class; probabilities = your_model.predict_proba(your_x_data)

K-Nearest Neighbors
Import and create the model:  from sklearn.neigbors import KNeighborsClassifier; your_model = KNeighborsClassifier()
Fit: your_model.fit(x_training_data, y_training_data)
Predict:  # Returns a list of predicted classes - one prediction for every data point;  predictions = your_model.predict(your_x_data); # For every data point, returns a list of probabilities of each class; probabilities = your_model.predict_proba(your_x_data)

K-Means
Import and create the model:  from sklearn.cluster import KMeans; your_model = KMeans(n_clusters=4, init='random')
	n_clusters: number of clusters to form and number of centroids to generate
	init: method for initialization
		k-means++: K-Means++ [default]
		random: K-Means
	random_state: the seed used by the random number generator [optional]
Fit:  your_model.fit(x_training_data)
Predict:  predictions = your_model.predict(your_x_data)

Validating the Model
Import and print accuracy, recall, precision, and F1 score: from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score; print(accuracy_score(true_labels, guesses)); print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses)); print(f1_score(true_labels, guesses))
Import and print the confusion matrix:  from sklearn.metrics import confusion_matrix; print(confusion_matrix(true_labels, guesses))

Training Sets and Test Sets
from sklearn.model_selection import train_test_split;  x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
	train_size: the proportion of the dataset to include in the train split
	test_size: the proportion of the dataset to include in the test split
	random_state: the seed used by the random number generator [optional]
'''