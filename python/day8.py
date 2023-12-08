from day8_data import STEPS, FLOORS

def part1(floor_key='AAA', lamda_match=lambda v : v == 'ZZZ', steps=STEPS, floors=FLOORS):
    total_steps=0
 
    while True:
        for i in range(len(steps)):
            total_steps += 1
            step = steps[i]
            current_floor = floors[floor_key]
 
            #print(f'step={step}')
            #print(f'total_steps={total_steps}')
            #print(f'current_floor={current_floor}')

            if step == 'L':
                floor_key = current_floor[0]
            else:
                floor_key = current_floor[1]

            if lamda_match(floor_key):
                return total_steps

print(f'--- part 1 ---')
print(part1())

print(f'--- part 2 ---')
floor_keys = [x for x in FLOORS.keys() if x.endswith('A')]
print(floor_keys)
 
min_steps_per_floor_key = [part1(floor_key=x, lamda_match=lambda v : v.endswith('Z')) for x in floor_keys]
print(min_steps_per_floor_key)
 
import math
print(math.lcm(*min_steps_per_floor_key))
