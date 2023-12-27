def tower_of_hanoi(n, source, target, auxiliary):
    """
    Parameters:
    - n: Number of disks
    - source: Source rod
    - target: Target rod
    - auxiliary: Auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        # Move n-1 disks from source to auxiliary rod
        tower_of_hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target rod
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary rod to target rod
        tower_of_hanoi(n - 1, auxiliary, target, source)


# Example usage:
tower_of_hanoi(3, "A", "C", "B")
