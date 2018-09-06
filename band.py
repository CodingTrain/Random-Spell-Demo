import json
import random

data = json.loads(open("instruments.json").read())
instruments = data['instruments']

band = random.sample(instruments, 10)

output = "The Randoms: \n"

for instrument in band:
    output += instrument + "\n"

print(output)

with open('theband.txt', 'w') as file:
    file.write(output)
