class WrongStudentNameError(Exception):
    pass


class WrongLineError(WrongStudentNameError):
    def __init__(self, wrongline, message):
        WrongStudentNameError.__init__(self, message)
        self.wrongline = wrongline


class EmptyFileError(WrongStudentNameError):
    def __init__(self, emptyfile, message):
        WrongStudentNameError.__init__(self, message)
        self.emptyfile = emptyfile


def count_students_points(name_source):
    students_points = {}
    source = open(name_source, "rt")
    line = source.readline()
    if not line or line.isspace():
        raise EmptyFileError(name_source, "Error! Empty file.")
    else:
        while line != "":
            student = line.rsplit(maxsplit=1)
            name = student[0]
            points = float(student[1])
            if not (name.replace(" ", "").isalpha() and isinstance(points, float)):
                raise WrongLineError(line, "Error! Wrong line.")
            elif name not in students_points.keys():
                students_points.update({name: points})
            elif name in students_points.keys():
                sum_points = float(students_points.get(name))
                sum_points = points
                students_points.update({name: sum_points})
            line = source.readline()
        for name, points in students_points.items():
            print(name, points)


try:
    name_source = input("Name a file: ")
    count_students_points(name_source)
except WrongLineError as w:
    print(w, ":", w.wrongline)
except EmptyFileError as e:
    print(e, ":", e.emptyfile)
