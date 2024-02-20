import random

def make_triangular_partition(n):
    """
    Create a partition with n squares by adding squares
    to allowed places.
    """
    partition = [1]
    for i in range(n-1):
        spots = [0, None] + [i for i in range(1, len(partition)) if partition[i] < partition[i-1]]
        new_spot = random.choice(spots)
        if new_spot is None:
            partition.append(1)
        else:
            partition[new_spot] += 1
    return partition


if __name__ == "__main__":
    print(make_triangular_partition(20))