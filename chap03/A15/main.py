N = int(input())
A = list(map(int, input().split()))


class Element:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __repr__(self):
        return f"[index: {self.index}, value: {self.value}]"

    def __lt__(self, other):
        return self.value < other.value


elements = []
for i, a in enumerate(A):
    elements.append(Element(a, i))

sorted_elements = sorted(elements)
# print(elements)
# print(sorted_elements)

i = 0
current_value = sorted_elements[0].value
result_value = 1
for element in sorted_elements:
    index = element.index
    value = element.value
    if value > current_value:
        result_value += 1
        current_value = value
    A[index] = result_value

print(" ".join(map(str, A)))
