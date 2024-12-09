from potus import get_info

for i in range(1, 47):
    print(f'PRESIDENT {i}:')
    for field, value in get_info(i).items():
        print(field, value)
    print()

