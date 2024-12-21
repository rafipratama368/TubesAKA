import streamlit as st
import time

def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quick_sort(left) + middle + quick_sort(right)

def main():
  st.title("Integer Ascending Sort")

  sorting_algorithm = st.radio("Pilih algoritma sorting", ("Bubble Sort", "Quick Sort"))

  input_data = st.text_input("Masukkan beberapa data yang ingin diurutkan (pisahkan dengan spasi):")

  if input_data:
    arr = list(map(int, input_data.split()))

    if sorting_algorithm == "Bubble Sort":
      start_time = time.time()
      sorted_arr = bubble_sort(arr)
      end_time = time.time()

      st.write(f"Data yang diurutkan: {sorted_arr}")
      st.write(f"Waktu eksekusi: {round((end_time - start_time) * 1000, 2)} ms")

    elif sorting_algorithm == "Quick Sort":
      start_time = time.time()
      sorted_arr = quick_sort(arr)
      end_time = time.time()

      st.write(f"Data yang diurutkan: {sorted_arr}")
      st.write(f"Waktu eksekusi: {round((end_time - start_time) * 1000, 2)} ms")

if __name__ == "__main__":
  main()
