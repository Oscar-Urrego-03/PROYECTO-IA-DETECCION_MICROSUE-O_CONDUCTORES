from procesar_fatiga.procesamiento_datos.processors.face_processor import FaceProcessor
from procesar_fatiga.procesamiento_datos.eyes.eyes_processing import (EyesPointsProcessing,
                                                                       EuclideanDistanceCalculator)


class EyesProcessor(FaceProcessor):
    def __init__(self):
        distance_calculator = EuclideanDistanceCalculator()
        self.processor = EyesPointsProcessing(distance_calculator)

    def process(self, points: dict):
        return self.processor.main(points)
