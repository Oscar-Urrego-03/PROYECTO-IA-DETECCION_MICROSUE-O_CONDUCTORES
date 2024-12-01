from procesar_fatiga.procesamiento_datos.processors.face_processor import FaceProcessor
from procesar_fatiga.procesamiento_datos.head.head_processing import (EuclideanDistanceCalculator,
                                                                       HeadPointsProcessing)


class HeadProcessor(FaceProcessor):
    def __init__(self):
        distance_calculator = EuclideanDistanceCalculator()
        self.processor = HeadPointsProcessing(distance_calculator)

    def process(self, points: dict):
        return self.processor.main(points)
