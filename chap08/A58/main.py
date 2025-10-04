import sys
from typing import Callable

N, Q = map(int, input().split())


class Cell:
    def __init__(self, start_index: int, end_index: int) -> None:
        self.min_value = 0
        self.max_value = 0
        self.start_index = start_index
        self.end_index = end_index
        self.lower_left_cell: Cell | None = None
        self.lower_right_cell: Cell | None = None
        self.upper_cell: Cell | None = None


class SegmentTree:
    def __init__(self, init_list: list[int]):
        self.cells: list[Cell] = []
        self.size = 1
        pow_num = 0
        length = len(init_list)
        while True:
            if 2**pow_num < length:
                pow_num += 1
            else:
                cells_length = 2**pow_num
                break
        while self.size < cells_length * 2:
            cells: list[Cell] = []
            for i in range(self.size):
                start_index = (cells_length // self.size) * i
                end_index = (cells_length // self.size) * (i + 1) - 1
                cells.append(Cell(start_index, end_index))
            self.cells.extend(cells)
            self.size *= 2
        self.size //= 2
        for i, cell in enumerate(self.cells):
            if i < self.size - 1:
                cell.lower_left_cell = self.cells[i * 2 + 1]
                cell.lower_right_cell = self.cells[i * 2 + 2]
            if i > 0:
                cell.upper_cell = self.cells[(i - 1) // 2]

        for i in range(cells_length):
            if i < length:
                self.update(i, init_list[i])
            else:
                self.update(i, -sys.maxsize)

    def __repr__(self):
        return str(self.cells)

    def find_cell(self, index: int):
        return self.cells[index + self.size - 1]

    def update(self, index: int, value: int):
        cell = self.find_cell(index)
        cell.max_value = value
        cell.min_value = value
        while cell.upper_cell is not None:
            cell = cell.upper_cell
            cell.max_value = max(
                cell.lower_left_cell.max_value, cell.lower_right_cell.max_value
            )
            cell.min_value = min(
                cell.lower_left_cell.min_value, cell.lower_right_cell.min_value
            )

    def max_value(self, start_index: int, end_index: int):
        return self.min_or_max_value(start_index, end_index, max)

    def min_value(self, start_index: int, end_index: int):
        return self.min_or_max_value(start_index, end_index, min)

    def min_or_max_value(self, start_index: int, end_index: int, min_or_max: Callable):
        if min_or_max == max:
            inf = -sys.maxsize
        elif min_or_max == min:
            inf = sys.maxsize

        def query(start_index: int, end_index: int, cell: Cell):
            if end_index < cell.start_index or cell.end_index < start_index:
                return -sys.maxsize
            if cell.start_index == start_index and end_index == cell.end_index:
                if min_or_max == max:
                    return cell.max_value
                elif min_or_max == min:
                    return cell.min_value
                else:
                    raise
            if cell.lower_left_cell is None or cell.lower_left_cell is None:
                raise
            # 左下
            if (
                cell.lower_left_cell is not None
                and start_index <= cell.lower_left_cell.end_index
            ):
                lower_left = query(
                    start_index,
                    min(cell.lower_left_cell.end_index, end_index),
                    cell.lower_left_cell,
                )
            else:
                lower_left = inf
            # 右下
            if (
                cell.lower_right_cell is not None
                and cell.lower_right_cell.start_index <= end_index
            ):
                lower_right = query(
                    max(start_index, cell.lower_right_cell.start_index),
                    end_index,
                    cell.lower_right_cell,
                )
            else:
                lower_right = inf
            return min_or_max(lower_left, lower_right)

        return query(start_index, end_index, self.cells[0])


init_list = [0] * N
tree = SegmentTree(init_list)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        pos = query[1] - 1
        x = query[2]
        tree.update(pos, x)
    else:
        l = query[1] - 1
        r = query[2] - 2
        print(tree.max_value(l, r))
