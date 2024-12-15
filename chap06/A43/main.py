from typing import Union

N, L = map(int, input().split())


class Person:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction


people: list[Person] = []
for _ in range(N):
    input_position, direction = input().split()
    position = int(input_position)
    person = Person(position, direction)
    people.append(person)

most_west_person_going_east: Union[None, Person] = None
current_position = L
for person in people:
    if person.direction == "E" and person.position < current_position:
        most_west_person_going_east = person
        current_position = person.position

most_east_person_going_west: Union[None, Person] = None
current_position = 0
for person in people:
    if person.direction == "W" and person.position > current_position:
        most_east_person_going_west = person
        current_position = person.position

time_for_most_east_person_going_west = (
    most_east_person_going_west.position
    if most_east_person_going_west is not None
    else 0
)

time_for_most_west_person_going_east = (
    L - most_west_person_going_east.position
    if most_west_person_going_east is not None
    else 0
)

print(max(time_for_most_east_person_going_west, time_for_most_west_person_going_east))
