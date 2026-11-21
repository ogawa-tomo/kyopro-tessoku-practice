import sys


class Cell:
    def __init__(self, start_index: int, end_index: int) -> None:
        self.min_value = 0
        self.max_value = 0
        self.sum_value = 0
        self.start_index = start_index
        self.end_index = end_index
        self.lower_left_cell: Cell | None = None
        self.lower_right_cell: Cell | None = None
        self.upper_cell: Cell | None = None

    def __repr__(self) -> str:
        return str((self.start_index, self.end_index))


class Query:
    def __init__(self, start_index: int, end_index: int, cell: Cell, func: str) -> None:
        self.start_index = start_index
        self.end_index = end_index
        self.cell = cell
        self.func = func


# スタックで管理
class SegmentTree:
    def __init__(self, init_list: list[int]):
        self.length = len(init_list)
        self.cells: list[Cell] = []
        self.size = 1
        pow_num = 0
        while True:
            if 2**pow_num < self.length:
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

        for i in range(self.length):
            self.update(i, init_list[i])

        self.answer = 0

    def __repr__(self):
        return str(self.cells)

    def find_cell(self, index: int):
        return self.cells[index + self.size - 1]

    def value(self, index):
        return self.find_cell(index).min_value

    def update(self, index: int, value: int):
        if index >= self.length:
            raise
        cell = self.find_cell(index)
        cell.max_value = value
        cell.min_value = value
        cell.sum_value = value
        while cell.upper_cell is not None:
            cell = cell.upper_cell
            lower_left_cell = cell.lower_left_cell
            lower_right_cell = cell.lower_right_cell
            if lower_left_cell is None or lower_right_cell is None:
                raise
            cell.max_value = max(lower_left_cell.max_value, lower_right_cell.max_value)
            cell.min_value = min(lower_left_cell.min_value, lower_right_cell.min_value)
            cell.sum_value = lower_left_cell.sum_value + lower_right_cell.sum_value

    def range_max(self, start_index: int, end_index: int):
        query = Query(start_index, end_index, self.cells[0], "max")
        return self.query(query)

    def range_min(self, start_index: int, end_index: int):
        query = Query(start_index, end_index, self.cells[0], "min")
        return self.query(query)

    def range_sum(self, start_index: int, end_index: int):
        query = Query(start_index, end_index, self.cells[0], "sum")
        return self.query(query)

    def query(self, first_query: Query) -> int:
        match first_query.func:
            case "max":
                self.answer = -sys.maxsize
            case "min":
                self.answer = sys.maxsize
            case "sum":
                self.answer = 0
            case _:
                raise

        def set_answer(value: int):
            match func:
                case "max":
                    self.answer = max(self.answer, value)
                case "min":
                    self.answer = min(self.answer, value)
                case "sum":
                    self.answer += value
                case _:
                    raise

        stack: list[Query] = []
        stack.append(first_query)
        while stack:
            query = stack.pop()
            start_index = query.start_index
            end_index = query.end_index
            cell = query.cell
            func = query.func

            if start_index < 0 or self.length <= end_index:
                raise

            if end_index < cell.start_index or cell.end_index < start_index:
                continue

            if cell.start_index == start_index and end_index == cell.end_index:
                match func:
                    case "max":
                        set_answer(cell.max_value)
                    case "min":
                        set_answer(cell.min_value)
                    case "sum":
                        set_answer(cell.sum_value)
                continue

            # 左下
            lower_left_cell = cell.lower_left_cell
            if lower_left_cell is not None and start_index <= lower_left_cell.end_index:
                query = Query(
                    start_index,
                    min(lower_left_cell.end_index, end_index),
                    lower_left_cell,
                    func,
                )
                stack.append(query)

            # 右下
            lower_right_cell = cell.lower_right_cell
            if (
                lower_right_cell is not None
                and lower_right_cell.start_index <= end_index
            ):
                query = Query(
                    max(start_index, lower_right_cell.start_index),
                    end_index,
                    lower_right_cell,
                    func,
                )
                stack.append(query)

        return self.answer


N, L, R = map(int, input().split())
X = list(map(int, input().split()))


# スタートからの距離がd以上である最小のインデックス
def get_smallest_index_more_than_or_equal(d: int):
    ok = N
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if X[mid] >= d:
            ok = mid
        else:
            ng = mid
    return ok


# スタートからの距離がd以下である最大のインデックス
def get_largest_index_less_than_or_equal(d: int):
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if X[mid] <= d:
            ok = mid
        else:
            ng = mid
    return ok


# dp[i]: i番目の足場に到達できる最小のジャンプ回数
dp = [0] * N
tree = SegmentTree(dp)
for i in range(1, N):
    left = get_smallest_index_more_than_or_equal(X[i] - R)
    right = get_largest_index_less_than_or_equal(X[i] - L)
    min_step = tree.range_min(left, right)
    tree.update(i, min_step + 1)

print(tree.value(N - 1))
