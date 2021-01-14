import matplotlib.pyplot as plt
from main import clusters_

image_clusters = [cluster.images for cluster in clusters_]

x_es = [[image[0] for image in images] for images in image_clusters]
y_es = [[image[1] for image in images] for images in image_clusters]

names = [' z' + str(i + 1) for i in range(len(image_clusters))]

standards = [cluster.standard for cluster in clusters_]

x_s = [standard[0] for standard in standards]
y_s = [standard[1] for standard in standards]

for i in range(len(x_es)):
    plt.scatter(x_es[i], y_es[i])

for i, txt in enumerate(names):
    for j in range(len(x_es[i])):
        plt.annotate(txt, (x_es[i][j], y_es[i][j]))

for i in range(len(x_s)):
    plt.scatter(x_s[i], y_s[i], s=10, marker='*')

plt.show()
