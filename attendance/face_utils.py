# attendance/face_utils.py

import os
import numpy as np
import cv2
import face_recognition
from django.conf import settings
from students.models import Student

ENC_DIR = settings.MEDIA_ROOT / 'encodings'


def load_known_faces():
    known_encodings = []
    known_ids = []

    if not os.path.exists(ENC_DIR):
        print("ENC_DIR does not exist:", ENC_DIR)
        return known_encodings, known_ids

    for student in Student.objects.all():
        prefix = f"student_{student.id}_"
        for fname in os.listdir(ENC_DIR):
            if fname.startswith(prefix) and fname.endswith(".npy"):
                path = ENC_DIR / fname
                enc = np.load(path)
                known_encodings.append(enc)
                known_ids.append(student.id)

    print("Total known encodings:", len(known_encodings))
    return known_encodings, known_ids


def recognize_from_frame(frame, known_encodings, known_ids, tolerance=0.6):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    recognized_student_ids = set()

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"

        if known_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=tolerance)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                student_id = known_ids[best_match_index]
                recognized_student_ids.add(student_id)
                student = Student.objects.get(id=student_id)
                name = student.name

        # draw green box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # label background
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(
            frame,
            name,
            (left + 2, bottom - 7),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            1,
        )

    return recognized_student_ids, frame
