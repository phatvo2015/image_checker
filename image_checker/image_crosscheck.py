import face_recognition
import numpy
import glob
from django.conf import settings

def crosscheckPerson(target, given):    
    # Check the same person
    picture_of_me = face_recognition.load_image_file(target)
    known_encodings = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    unknown_picture = face_recognition.load_image_file(given)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces([known_encodings], unknown_face_encoding)

    matchingResult = [False,'']
    if results[0] == True:
        matchingResult = [True, target]

    # https://stackoverflow.com/questions/61487936/how-to-get-face-matching-percentage-instead-of-boolean-value-in-face-recognition
    face_distances = face_recognition.face_distance([known_encodings], unknown_face_encoding)
    face_match_percentage = (1-face_distances)*100
    matchingResult.append(face_match_percentage[0])
    return matchingResult


def crosscheckPersonDB(given):
    existingPeopple = []
    # for f in glob.glob("/home/phatvo/Code/python-getting-started/project/media/static_media/*"):
    # print(settings.BASE_DIR + "/media/static_media/")
    for f in glob.glob(settings.BASE_DIR + "/media/static_media/*"):
        existingPeopple.append(f)

    for target in existingPeopple:
        res = crosscheckPerson(target, given)
        if res[0] == True:
            return "User is found", res
        
    return "User not found",[]

# if __name__ == "__main__":
#     print("Running")
#     crosscheckPersonDB("/home/phatvo/Code/python-getting-started/project/media/crosscheck_media/vy_2.jpg")