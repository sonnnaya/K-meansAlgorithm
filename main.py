import numpy as np
from typing import List
from cluster import Cluster
from data import images_, standards_


def define_image(clusters: List[Cluster], image: np.ndarray) -> None:
    distances = [cluster.get_distance(image) for cluster in clusters]
    minimum = min(distances)
    index = distances.index(minimum)
    clusters[index].add(image)


def get_clustered(images: List[np.ndarray], standards: List[np.ndarray]) -> List[Cluster]:
    clusters = [Cluster(standard) for standard in standards]

    for image in images:
        define_image(clusters, image)

    return clusters


def is_equals(previous: List[np.ndarray], current: List[np.ndarray]) -> bool:
    return np.allclose(np.array(previous), np.array(current))


def k_mean(images: List[np.ndarray], standards: List[np.ndarray]) -> List[Cluster]:
    clusters = get_clustered(images, standards)
    standards = [cluster.standard for cluster in clusters]

    while True:
        means = [cluster.get_mean() for cluster in clusters]

        if is_equals(standards, means):
            break

        standards = means
        clusters = get_clustered(images, standards)

    return clusters


clusters_ = k_mean(images_, standards_)

if __name__ == '__main__':
    print(f'K-means result:')
    for i, cluster in enumerate(clusters_):
        print(f'Cluster {i + 1}: {[image.tolist() for image in cluster.images]}')
