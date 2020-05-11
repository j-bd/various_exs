#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import cv2
from tensorflow.keras.models import load_model

from masked_face.settings import base


class GetModels:
    def __init__(self, type_detection):
        """Class initialisation
        Parameters
        ----------
        type_detection : str.
            user specification
        """
        self.type_input = type_detection

    def models_loading(self):
        """
        Provide the detector model and the classifier model ready to use

        Returns
        -------
        detector
            caffe model
        classifier
            Keras model user choice
        """
        if self.type_input == 'webcam':
            model_classification = base.WEBC_MODEL_CLASSIFIER_FILE
            model_detection_structure = base.WEBC_MODEL_DETECTION_STRUCTURE
            model_detection_weights = base.WEBC_MODEL_DETECTION_WEIGHT
            detector = cv2.dnn.readNet(
                model_detection_structure, model_detection_weights
            )
            classifier = load_model(model_classification)
            return detector, classifier
        elif self.type_input == 'video':
#            model_classification = base.MODEL_FILE
#            model_detection_structure = base.WEBC_MODEL_DETECTION_STRUCTURE
#            model_detection_weights = base.WEBC_MODEL_DETECTION_WEIGHT
#            detector = cv2.dnn.readNet(
#                model_detection_structure, model_detection_weights
#            )
#            classifier = load_model(model_classification)
            return detector, classifier