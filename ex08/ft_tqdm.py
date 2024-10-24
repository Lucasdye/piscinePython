from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range)->None:
  
  M = lst.stop
  percentage = 0
  count = 0
  for x in lst:
    print("\t" * 13, " " * 2, "] ", count, "/", M, sep="", end="\r", flush=True)
    count += 1
    tmp = int((x / M) * 100)
    # print(tmp, sep="", end="")
    if (tmp > percentage):
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
  print("\r", "100%|[", "█" * 100, "] ", count, "/", M, sep="", end="", flush=True)  # Final output

def main():
  for elem in ft_tqdm(range(333)):
    # print(elem)
    sleep(0.005)
      
  
if __name__ == "__main__":
  main()