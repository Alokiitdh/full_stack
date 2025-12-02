class Person:

    def __init__(self, name, age, gender, contact_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info

    def Display_info(self):
        return f"Name: {self.name} \nAge: {self.age} \ngender: {self.gender} \nContact Info: {self.contact_info}"

        
class Patient(Person):

    def __init__(self, name, age, gender, contact_info, patient_id, disease):
        super().__init__(name, age,gender, contact_info)
        self.patient_id = patient_id        
        self.disease = disease        
        self.medical_record = []  

    def add_medical_record(self):
        """Adding patient Medical Record"""
        record = {
            'Patient ID': self.patient_id,
            'Name': self.name,
            'Age': self.age,
            'Gender': self.gender,
            'Contact Info': self.contact_info,
            'Diseases': self.disease
        }
        self.medical_record.append(record)


    def get_medical_history(self):
        """ getting medical records"""
        for rec in self.medical_record:
            print(f"Record: {rec}")








pat1 = Patient(name="John Doe",
                   age=30,
                   gender='Male',
                   contact_info='USA',
                   patient_id='1',
                   disease='Flue')

pat2 = Patient(name="Syfr Doe",
                   age=40,
                   gender='Male',
                   contact_info='USA',
                   patient_id='2',
                   disease='Cold')

pat1.add_medical_record()
pat2.add_medical_record()

Patient.get_medical_history(pat1)