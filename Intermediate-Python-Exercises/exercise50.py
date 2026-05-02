import time
import threading

def task(name, t):
    print(f"Downloading {name}...")
    time.sleep(t)
    print(f"Finished download {name}")
if __name__ == "__main__":
    t_spend = 3
    t1 = threading.Thread(target=task, args=("File-1",t_spend))
    t2 = threading.Thread(target=task, args=("File-2",t_spend))
    start_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time} seconds (instead of {t_spend*2} seconds).")
