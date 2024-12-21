import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
       for j in range(0, n-i-1):
          if arr[j] > arr[j+1]:
             arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr         

def main():
    n = int(input("Enter the number of data: "))
    arr = input("Enter the data separated by spaces: ").split()
    arr = [int(x) for x in arr]

    start_time = time.time()
    sorted_arr = bubble_sort(arr)
    end_time = time.time()

    print("Sorted data:")
    print(sorted_arr)
    print("Running time: {:.2f} ms".format((end_time - start_time) * 1000))

    if __name__ == "__main__":
        main()