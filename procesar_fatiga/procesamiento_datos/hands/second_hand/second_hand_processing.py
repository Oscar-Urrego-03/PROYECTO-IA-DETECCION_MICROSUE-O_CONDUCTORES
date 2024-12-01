import numpy as np
from abc import ABC, abstractmethod
from collections import deque


class DistanceCalculator(ABC):
    @abstractmethod
    def calculate_distance(self, point1, point2):
        pass


class EuclideanDistanceCalculator(DistanceCalculator):
    def calculate_distance(self, point1, point2):
        return np.linalg.norm(np.array(point1) - np.array(point2))


class DistanceSmoother:
    def __init__(self, window_size=5):
        self.distances = deque(maxlen=window_size)

    def smooth(self, new_distance):
        if new_distance != float('inf'):
            self.distances.append(new_distance)
        return sum(self.distances) / len(self.distances) if self.distances else float('inf')


class FingerEyeDistanceCalculator:
    def __init__(self, distance_calculator: DistanceCalculator):
        self.distance_calculator = distance_calculator
        self.smoothers = {
            finger: DistanceSmoother(5)
            for finger in ['thumb', 'index_finger', 'middle_finger', 'ring_finger', 'little_finger']
        }

    def calculate_finger_eye_distances(self, finger_points: dict, eye_point: list) -> dict:
        raw_distances = {
            'thumb': self.distance_calculator.calculate_distance(finger_points[0], eye_point),
            'index_finger': self.distance_calculator.calculate_distance(finger_points[1], eye_point),
            'middle_finger': self.distance_calculator.calculate_distance(finger_points[2], eye_point),
            'ring_finger': self.distance_calculator.calculate_distance(finger_points[3], eye_point),
            'little_finger': self.distance_calculator.calculate_distance(finger_points[4], eye_point),
        }
        # Suavizar las distancias
        return {
            finger: self.smoothers[finger].smooth(distance)
            for finger, distance in raw_distances.items()
        }


class SecondHandPointsProcessing:
    def __init__(self, distance_calculator: DistanceCalculator):
        self.distance_calculator = distance_calculator
        self.finger_eye_calculator = FingerEyeDistanceCalculator(distance_calculator)
        self.hands: dict = {}

    def main(self, hand_points: dict, eyes_points: dict):
        # Validación de datos
        if not hand_points or 'distances' not in hand_points or 'distances' not in eyes_points:
            return {}

        self.hands['hand_to_right_eye'] = self.finger_eye_calculator.calculate_finger_eye_distances(
            hand_points['distances'], eyes_points['distances'][8]
        )
        self.hands['hand_to_left_eye'] = self.finger_eye_calculator.calculate_finger_eye_distances(
            hand_points['distances'], eyes_points['distances'][9]
        )
        return self.hands
