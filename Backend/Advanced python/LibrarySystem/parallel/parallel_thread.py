import threading
import time

# Function to do add and subtraction
def cal(a: float, b:float, operation : str) -> float:
    if operation == "add":
        time.sleep(2) # simu;ation a time consuming operation
        results = a + b
        print(f"Addition: {results}")
    elif operation == "sub":
        time.sleep(2)
        results = a - b
        print(f"Subtraction: {results}")
    else:
        raise ValueError("Unsupported Operation")
    

# lets create the thread
t1 = threading.Thread(target=cal, args = (10,5,"add"))
t2 = threading.Thread(target=cal, args = (10,5,"sub"))

t1.start()
t2.start()


t1.join()
t2.join()

print("Threading tasked OVER!!!!!")