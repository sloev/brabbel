
class Policy():
    __policyname__ = "policy"
    __history__ = []

    def __init__(self, debug=True):
        self.debug=debug

    def enforce(self, subject, resource, environment):
        pass

    def _equals(self, a,b):
        res = a == b
        if self.debug:
            msg = "{} equals {}: {}".format(a,b,res)
            self.__history__.append(msg)
        return res

    def _in(self, a, b):
        res = a in b
        if self.debug:
            msg = "{} in {}: {}".format(a,b,res)
            self.__history__.append(msg)
        return res

    def _not_in(self, a,b):
        res = not(a in b)
        if self.debug:
            msg = "{} not in {}: {}".format(a,b,res)
            self.__history__.append(msg)
        return res

    def _intersect(self, a,b):
        res = any(e in a for e in b)
        if self.debug:
            msg = "{} intersect {}: {}".format(a,b,res)
            self.__history__.append(msg)
        return res

    @property
    def history(self):
        return self.__history__

class ReadPatientJournals(Policy):
    def enforce(self, subject, resource, environment=None):
        if (self._intersect(subject.roles, ["author","admin"]) and
            self._intersect(subject.municipalities, resource.municipalities) and
            (self._intersect(subject.roles, ["admin"]) or self._equals(subject.id, resource.author_id))):
            return True
        elif self.debug:
            print self.__history__
        return False

class Subject():
    def __init__(self, id, roles=["author", "admin"], municipalities=["odense"]):
        self.id = id
        self.roles = roles
        self.municipalities = municipalities

class Resource():
    def __init__(self, author_id, municipalities=["odense"]):
        self.author_id = author_id
        self.municipalities = municipalities

subject_a = Subject(1, roles=["author"])
subject_b = Subject(2, roles=["admin"])
resource_a = Resource(1)

policy = ReadPatientJournals(True)
print "a", policy.enforce(subject_a, resource_a)
print "b", policy.enforce(subject_b, resource_a)
print "history", policy.history

a = """
user attrs:
    role:author
    municipalities:[odense, roskilde]
    policies: ["read_patient_journals","write_patient_journals"]

environment attrs:
    time: 8pm

resource:"patient_journal"
    municipality:odense
    title:lolcat
    secrets:many
    author_id: ivan

policies:
    "read_patient_journals":
        resource_name: patient_journal
        policy = "user.role__in==[author, admin] && user.role__equal 
        policies: [
                    user.role__in: [author, admin]
                    user.role__equal: admin
                    user.id__equal: resource.author_id
        user.municipalities__intersect:resource.municipalities


    user.role__in: [admin, author]
    subject.municipalities__intersect: True
    context.time
"""
