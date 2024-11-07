from time import sleep


def ft_tqdm(lst: range) -> None:
    """
    This script emulates the tqdm function,
    rendering a loadind bar on the terminal output.
    """
    M = lst.stop
    percentage = 0
    count = 0
    for x in lst:
        count += 1
        percentage = int((x / M) * 100)
        bar = "█" * percentage + "-" * (100 - percentage)
        print(f"\r{percentage:3}%|[{bar}] {count + 1}/{M}", end="", flush=True)
        yield
    # Final output
    print("\r", "100%|[", "█" * 100, "] ", count, "/", M,
                sep="", end="\n", flush=True)


def main():
    for elem in ft_tqdm(range(444)):
        sleep(0.005)


if __name__ == "__main__":
    main()
