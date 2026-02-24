def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))

    def helper(current: int) -> None:
        if current > day:
            print("Harvest time!")
            return
        print(f"Day {current}")
        helper(current + 1)
    helper(1)
