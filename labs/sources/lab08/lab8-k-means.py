from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def color_code(targets):
    code = {
        0: 'red',
        1: 'green',
        2: 'blue'
    }

    return [code[target] for target in targets]


iris_df = datasets.load_iris()
input_data = iris_df.data
selected_data = iris_df.data[:, [0, 2]]

x_axis = iris_df.data[:, 0]  # sepal length
y_axis = iris_df.data[:, 2]  # sepal width

model = KMeans(n_clusters=3)

model.fit(input_data)

all_predictions = model.predict(input_data)

fig, axs = plt.subplots(1, 2, figsize=(18, 9), sharey=True)
axs[0].scatter(x_axis, y_axis, c=color_code(iris_df.target))
axs[0].set_xlabel("sepal length")
axs[0].set_ylabel("sepal width")

axs[1].scatter(x_axis, y_axis, c=color_code(all_predictions))
axs[1].set_xlabel("sepal length")
axs[1].set_ylabel("sepal width")

plt.show()
