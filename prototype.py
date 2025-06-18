import random
import time

rand_time = random.uniform(0,8)
time.sleep(rand_time)
start_timer = time.time()

input("/// ¡CLICK! ///")

end_timer = time.time()
print(f"Your reaction time was {end_timer - start_timer:.3f}s")