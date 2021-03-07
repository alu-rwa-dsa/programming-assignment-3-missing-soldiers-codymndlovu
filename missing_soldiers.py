def count_blocked(barriers):
    barriers.sort(key=lambda x: x[0])
    num_blocked, last_blocked = barriers[0][1] + 1 - barriers[0][0]
    last_blocked = barriers[0][1]

    for i in range(1, len(barriers)):
        if barriers[i][1] <= lastblocked:
            continue

        x1, x2 = barriers[i][0], barriers[i][1]
        if barriers[i][0] > lastblocked:
            num_blocked += x2 + 1 - x1
        else:
            num_blocked += x2 - lastblocked
        lastblocked = x2
    return num_blocked
        

if __name__ == "__main__":
    num_barriers = int(input())
    barriers = []

    for _ in range(num_barriers):
        args = list(map(int, input().rstrip().split()))
        barriers.append([args[0], args[0] + args[2]])
    print(count_blocked(barriers))
