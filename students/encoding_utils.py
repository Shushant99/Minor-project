# students/encoding_utils.py

import os
import numpy as np
import face_recognition
from django.conf import settings
from .models import StudentImage

ENC_DIR = settings.MEDIA_ROOT / 'encodings'


def create_and_save_encoding(student):
    """
    Legacy helper: create encoding only for the main photo
    and store path on the student model (if you still use face_encoding_file).
    """
    if not student.photo:
        return

    image = face_recognition.load_image_file(student.photo.path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return

    encoding = encodings[0]

    os.makedirs(ENC_DIR, exist_ok=True)

    filename = f'student_{student.id}.npy'
    filepath = ENC_DIR / filename
    np.save(filepath, encoding)

    # Only if your Student model has face_encoding_file
    if hasattr(student, 'face_encoding_file'):
        student.face_encoding_file = str(filepath)
        student.save(update_fields=['face_encoding_file'])


def create_encodings_for_student(student):
    """
    Preferred helper: create encodings for main photo + all extra photos.
    Called from student_create/student_update views.
    """
    os.makedirs(ENC_DIR, exist_ok=True)

    # main photo
    if student.photo:
        _encode_and_save(student, student.photo.path, suffix='main')

    # extra photos (StudentImage objects)
    for img in student.images.all():
        _encode_and_save(student, img.image.path, instance=img)


def _encode_and_save(student, img_path, suffix=None, instance: StudentImage = None):
    image = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return

    encoding = encodings[0]

    if suffix is None and instance:
        suffix = f'extra_{instance.id}'
    elif suffix is None:
        suffix = 'main'

    filename = f'student_{student.id}_{suffix}.npy'
    filepath = ENC_DIR / filename
    np.save(filepath, encoding)

    # If this is an extra image, remember its file path on the StudentImage record
    if instance is not None:
        instance.encoding_file = str(filepath)
        instance.save(update_fields=['encoding_file'])
