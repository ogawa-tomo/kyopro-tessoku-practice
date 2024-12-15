N, K = map(int, input().split())


class Student:
    def __init__(self, physical, mental):
        self.physical = physical
        self.mental = mental

    def __repr__(self):
        return f"[physical: {self.physical}, mental: {self.mental}]"


students: list[Student] = []
for i in range(N):
    A, B = map(int, input().split())
    students.append(Student(A, B))


def student_num(min_physical, max_physical, min_mental, max_mental):
    num = 0
    for student in students:
        if (
            min_physical <= student.physical
            and student.physical <= max_physical
            and min_mental <= student.mental
            and student.mental <= max_mental
        ):
            num += 1
    return num


answer = 0
for min_physical in range(1, 100 - K + 1):
    for min_mental in range(1, 100 - K + 1):
        max_physical = min_physical + K
        max_mental = min_mental + K
        answer = max(
            answer, student_num(min_physical, max_physical, min_mental, max_mental)
        )

print(answer)
