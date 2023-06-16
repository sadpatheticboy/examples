import time

start = time.time()
file_path = 'racing_fast.txt'

with open(file_path, 'a') as f:
    for i in range(50):
        f.write(f'line {i}\n')

print(time.time() - start)
print("done")
