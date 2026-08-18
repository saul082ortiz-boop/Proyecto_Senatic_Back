import os
import uuid

def RutaLogoEmpresa(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f"LOGOS/{uuid.uuid4()}{extension}"