from procesar_fatiga.procesamiento_datos.processors.hands_processor import HandsProcessor
from procesar_fatiga.procesamiento_datos.hands.first_hand.first_hand_processing import (EuclideanDistanceCalculator,
                                                                                         FirstHandPointsProcessing)


class FirstHandProcessor(HandsProcessor):
    def __init__(self):
        distance_calculator = EuclideanDistanceCalculator()
        self.processor = FirstHandPointsProcessing(distance_calculator)

    def process(self, hand_points: dict, eyes_points: dict):
        return self.processor.main(hand_points, eyes_points)
