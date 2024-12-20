from procesar_fatiga.procesamiento_datos.processors.hands_processor import HandsProcessor
from procesar_fatiga.procesamiento_datos.hands.second_hand.second_hand_processing import (EuclideanDistanceCalculator,
                                                                                           SecondHandPointsProcessing)


class SecondHandProcessor(HandsProcessor):
    def __init__(self):
        distance_calculator = EuclideanDistanceCalculator()
        self.processor = SecondHandPointsProcessing(distance_calculator)

    def process(self, hand_points: dict, eyes_points: dict):
        return self.processor.main(hand_points, eyes_points)
