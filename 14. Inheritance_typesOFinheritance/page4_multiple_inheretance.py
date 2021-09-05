class Faculty:
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject


class LabAssistant:
    def __init__(self, name, lab):
        self._name = name
        self._lab = lab


class FacultyLabAssistant(Faculty, LabAssistant):
    def __init__(self, name, subject, lab):
        Faculty.__init__(self, name, subject)
        LabAssistant.__init__(self, name, lab)


f1 = Faculty('f1', 'python')
la1 = LabAssistant('la1', 'python-lab')
fla1 = FacultyLabAssistant('fla1', 'python', 'python-lab')


class Developer:
    def __init__(self, name, technology):
        self._name = name
        self._technology = technology


class Tester:
    def __init__(self, name, application):
        self._name = name
        self._application = application


class MyDeveloper(Developer, Tester):
    def __init__(self, name, technology, application):
        Developer.__init__(self, name, technology)
        Tester.__init__(self, name, application)
