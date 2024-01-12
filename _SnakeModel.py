import tensorflow as tf
import keras
import numpy as np

class SnakeModel:
    blocked_data = np.ndarray = np.empty([])
    food_distance_data = np.ndarray = np.array([])
    direction_data = np.ndarray = np.array([])

    def __init__(self):
        blocked_input = keras.Input(shape = (4,), name = "blocked")
        food_distance_input = keras.Input(shape = (2,), name = "food_distance")

        blocked_features = keras.layers.Embedding(1024, 4)(blocked_input)
        food_distance_features = keras.layers.Embedding(1024, 2)(food_distance_input)
        x = keras.layers.concatenate([blocked_features, food_distance_features])

        direction_prediction = keras.layers.Dense(4, name = "direction")(x)

        self.model = keras.Model(
            inputs = [blocked_input, food_distance_input],
            outputs = [direction_prediction],
        )
    
    def add_data(self, blocked: tuple, food_distance: tuple, direction: int):
        np.append(self.blocked_data, blocked)
        np.append(self.food_distance_data, food_distance)
        np.append(self.direction_data, direction)
    
    def train(self):
        self.model.fit(
            {
                "blocked": self.blocked_data,
                "food_distance": self.food_distance_data
            },
            {
                "direction": self.direction_data
            },
            epochs = 2,
            batch_size = 32
        )
    
    def predict(self, blocked: tuple, food_distance: tuple):
        prediction = self.model.predict({
            "blocked": [blocked],
            "food_distance": [food_distance],
        })
        print(prediction)
        return prediction