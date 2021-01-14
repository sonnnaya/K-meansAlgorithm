from typing import List
import numpy as np


def get_euclid(image1: np.ndarray, image2: np.ndarray) -> float:
    return np.linalg.norm(np.array(image1) - np.array(image2))


class Cluster:
    def __init__(self, standard: np.ndarray):
        self.standard: np.ndarray = np.array(standard)
        self.images: List[np.ndarray] = []

    def get_distance(self, image: np.ndarray) -> float:
        return get_euclid(image, self.standard)

    def get_mean(self) -> np.ndarray:
        return np.mean(np.array(self.images), axis=0)

    def get_deviation(self) -> float:
        return sum(map(lambda x: get_euclid(x, self.standard) ** 2, self.images))

    def add(self, image: np.ndarray) -> None:
        self.images.append(np.array(image))
