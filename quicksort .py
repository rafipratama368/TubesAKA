import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    arr = input("Masukkan beberapa data yang ingin diurutkan (pisahkan dengan spasi): ")
    arr = list(map(int, arr.split()))
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000
    print("Data yang diurutkan: ", sorted_arr)
    print("Waktu eksekusi: {:.2f} ms".format(running_time))

if __name__ == "__main__":
    main()