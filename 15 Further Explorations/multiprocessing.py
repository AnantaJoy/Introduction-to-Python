# from multiprocessing import Process, Queue
# import os

# processes = []
# num_processes = os.cpu_count()

# # create processes
# for i in range(num_processes):
#     p = Process(target=worker, args=(i, queue))
#     p.start()
#     processes.append(p)

# for i in range(num_processes):
#     queue.put(i)