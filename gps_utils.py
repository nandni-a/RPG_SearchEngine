import openlocationcode

def get_plus_code(lat, lon):
    return openlocationcode.encode(lat, lon)