def pack(items):
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    free = [3, 3, 3]
    grid = [[None] * 3 for _ in range(3)]

    for symbol, size in sorted_items:
        placed = False
        for i in range(3):
            if free[i] >= size:
                start = 3 - free[i]
                for j in range(start, start + size):
                    grid[i][j] = symbol
                free[i] -= size
                placed = True
                break
        if not placed:
            return False, None
    return True, grid

def main():
    items_list = [
        ('r', 3, 25), ('p', 2, 15), ('a', 2, 15),
        ('m', 2, 20), ('i', 1, 5), ('k', 1, 15),
        ('x', 3, 20), ('t', 1, 25), ('f', 1, 15),
        ('d', 1, 10), ('s', 2, 20), ('c', 2, 20)
    ]
    total_points_all = 205
    base_score = 15
    n = len(items_list)
    found = False

    for mask in range(1 << n):
        subset = []
        total_size = 0
        total_points = 0
        for j in range(n):
            if mask & (1 << j):
                symbol, size, points = items_list[j]
                subset.append((symbol, size))
                total_size += size
                total_points += points

        if total_size > 9 or total_points <= 95:
            continue

        success, grid = pack(subset)
        if success:
            final_score = base_score + 2 * total_points - total_points_all
            found = True
            break

    if not found:
        print("Не удалось найти подходящую комбинацию предметов.")
        return

    for i in range(3):
        row = []
        for j in range(3):
            if grid[i][j] is not None:
                row.append(f"[{grid[i][j]}]")
            else:
                row.append("[]")
        print(','.join(row))
    print(f"Итоговые очки выживания: {final_score}")

if __name__ == "__main__":
    main()