import random
import time

print("--Welcome to the reaction test--")
print("**When you see the message press Enter to register the attempt**")
user = input("Are you ready? (Press Enter to start)")

while True:
    rand_time = random.uniform(0,8)
    time.sleep(rand_time)
    s_timer = time.time()
    
    input("/// ¡NOW! ///")
    
    e_timer = time.time()
    print(f"Your reaction time was {e_timer - s_timer:.3f}s")
    ####
    rand_time = random.uniform(0,8)
    time.sleep(rand_time)
    s_timer = time.time()
    
    input("/// ¡NOW! ///")
    
    e_timer = time.time()
    print(f"Your reaction time was {e_timer - s_timer:.3f}s")
    ####
    rand_time = random.uniform(0,8)
    time.sleep(rand_time)
    s_timer = time.time()
    
    input("/// ¡NOW! ///")
    
    e_timer = time.time()
    print(f"Your reaction time was {e_timer - s_timer:.3f}s")
    
    break