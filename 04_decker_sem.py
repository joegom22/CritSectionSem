from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import BoundedSemaphore
import time
import random

N = 8


def task(common, tid, sem):
	a = 0
	for i in range(100):
		print(f'{tid}−{i}: Non−critical Section', flush=True)
		time.sleep(random.random())
		print(f'{tid}−{i}: End of non−critical Section', flush=True)
		sem.acquire()
		print(f'{tid}−{i}: Critical section', flush=True)
		v = common.value + 1
		time.sleep(random.random())
		print(f'{tid}−{i}: Inside critical section', flush=True)
		common.value = v
		print(f'{tid}−{i}: End of critical section', flush=True)
		sem.release()

def main():
	lp = []
	common = Value('i', 0)
	critical = Array('i', [0]*N)
	turn = Value('i', 0)
	sem = BoundedSemaphore(1)
	for tid in range(N):
		lp.append(Process(target=task, args=(common, tid, sem)))
	print (f"Valor inicial del contador {common.value}", flush=True)
	for p in lp:
		p.start()
	for p in lp:
		p.join()
	print (f"Valor final del contador {common.value}", flush=True)
	print ("fin")
if __name__ == "__main__":
	main()
