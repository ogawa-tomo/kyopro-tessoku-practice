N = int(input())

divided_by_3 = N // 3
divided_by_5 = N // 5
divided_by_7 = N // 7

divided_by_15 = N // 15
divided_by_21 = N // 21
divided_by_35 = N // 35

divided_by_105 = N // 105

print(
    divided_by_3
    + divided_by_5
    + divided_by_7
    - divided_by_15
    - divided_by_21
    - divided_by_35
    + divided_by_105
)
