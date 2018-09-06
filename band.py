import json
import random

data = json.loads(open("instruments.json").read())
instruments = data['instruments']

band = random.sample(instruments, 10)
print("The Randoms:\n")
for instrument in band:
    print(instrument)