import psutil
import time
sec = input("Enter time period in seconds:")
fname = input("Filename:")
while True:
    try:
        with open(fname, 'w') as f:
            print("-------------------------------",file=f)
            print("CPU%: ",psutil.cpu_percent(),file=f)
            print("RSS: ",psutil.Process().memory_info().rss,file=f)
            print("VMS: ",psutil.Process().memory_info().vms,file=f)
            print("FD: ",psutil.Process().num_fds(),file=f)
        time.sleep(int(sec))
        print('Done')
    except KeyboardInterrupt:
        break
