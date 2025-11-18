# Doel: objecten in een dict opslaan voor snelle lookup.

class Student:
    def __init__(self, student_id, naam):
        self.student_id = student_id
        self.naam = naam
    def __repr__(self):
        return f"Student(id={self.student_id!r}, naam={self.naam!r})"

index = {
    101: Student(101, "Ali"),
    102: Student(102, "Bo"),
}
print(index[101])
