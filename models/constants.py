class MedicalSpecialties:
    SPECIALTIES = {
        "cardiology": "Cardiología",
        "neurology": "Neurología",
        "dermatology": "Dermatología",
        "pediatrics": "Pediatría",
        "orthopedics": "Ortopedia",
        "oncology": "Oncología",
        "urology": "Urología",
        "gastroenterology": "Gastroenterología",
        "ophthalmology": "Oftalmología",
        "psychiatry": "Psiquiatría"
    }

    @staticmethod
    def get_specialties():
        return MedicalSpecialties.SPECIALTIES
