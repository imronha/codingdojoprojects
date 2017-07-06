class Patient(object):
    def __init__(self, id_num, name, allergies, bed_num=None):
        self.id_num = id_num
        self.name = name
        self.allergies = allergies
        self.bed_num = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.hospital_name = name
        self.capacity = capacity
    def admit(self, new_pt):
        if len(self.patients) < self.capacity:
            self.patients.append(new_pt)
            print "Patient added"
        else:
            print "Not enough space."
        # print self.patients
        return self

    def discharge(self, discharge_pt):
        for i in range(0,len(self.patients)-1):
            if self.patients[i] == discharge_pt:
                self.patients.pop(i)
                print "Discharged: "+str(self.patients[i])
        print self.patients

imron = Patient(10001, "Imron", "No allergies")
vinney = Patient(10002, "Vinney", "No allergies")
ethan = Patient(10002, "Ethan", "No allergies")

UCDMC = Hospital("UCDMC", 2)

UCDMC.admit(imron)
UCDMC.admit(vinney)
UCDMC.admit(ethan)
UCDMC.discharge(imron)

# UCDMC.display_all()
