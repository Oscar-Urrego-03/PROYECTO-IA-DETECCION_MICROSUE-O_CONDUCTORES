from procesar_fatiga.procesamiento_datos.processors.face_processor import FaceProcessor
from procesar_fatiga.procesamiento_datos.processors.hands_processor import HandsProcessor
from procesar_fatiga.procesamiento_datos.eyes.eyes_processor import EyesProcessor
from procesar_fatiga.procesamiento_datos.hands.first_hand.first_hand_processor import FirstHandProcessor
from procesar_fatiga.procesamiento_datos.hands.second_hand.second_hand_processor import SecondHandProcessor
from procesar_fatiga.procesamiento_datos.head.head_processor import HeadProcessor
from procesar_fatiga.procesamiento_datos.mouth.mouth_processor import MouthProcessor


class PointsProcessing:
    def __init__(self):
        self.face_processors: dict[str, FaceProcessor] = {
            'eyes': EyesProcessor(),
            'head': HeadProcessor(),
            'mouth': MouthProcessor()
        }
        self.hands_processors: dict[str, HandsProcessor] = {
            'first_hand': FirstHandProcessor(),
            'second_hand': SecondHandProcessor(),
        }
        self.processed_points: dict = {}

    def main(self, points: dict):
        self.processed_points = {}
        self.processed_points['eyes'] = self.face_processors['eyes'].process(points.get('eyes', {}))

        if 'first_hand' in points:
            self.processed_points['first_hand'] = (self.hands_processors['first_hand'].process(points['first_hand'],
                                                                                               points.get('eyes', {})))

        if 'second_hand' in points:
            self.processed_points['second_hand'] = (self.hands_processors['second_hand'].process(points['second_hand'],
                                                                                                 points.get('eyes',
                                                                                                            {})))

        self.processed_points['head'] = self.face_processors['head'].process(points.get('head', {}))
        self.processed_points['mouth'] = self.face_processors['mouth'].process(points.get('mouth', {}))

        return self.processed_points
