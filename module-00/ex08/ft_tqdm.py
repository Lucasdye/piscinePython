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
        print("\t" * 13, " " * 2, "] ", count, "/", M, sep="",
              end="\r", flush=True)
        count += 1
        tmp = int((x / M) * 100)
        # print(tmp, sep="", end="")
        if (tmp > percentage or tmp == 0):
            percentage = tmp
            print(" ", percentage, "%", sep="", end="", flush=True)
            print("|[", sep="", end="", flush=True)
            i = 0
            while i <= percentage:
                print("█", sep="", end="", flush=True)
                i += 1
            if count < M - 1:
                print(end="\r", flush=True)
        yield
    # Final output
    print("\r", "100%|[", "█" * 100, "] ", count, "/", M,
                sep="", end="", flush=True)


def main():
    for elem in ft_tqdm(range(100000)):
        sleep(0.005)


if __name__ == "__main__":
    main()
