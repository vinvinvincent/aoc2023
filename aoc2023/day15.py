def calc_hash(input):
    result = 0
    for i in input:
        result += ord(i)
        result *= 17
        result %= 256
    return result


def calc_hash_sum(inputs):
    return sum(calc_hash(input) for input in inputs)


def add_to_boxes(boxes, input):
    label, step = input.split('=')
    step = int(step)
    key = calc_hash(label)
    box = boxes.setdefault(key, list())

    found = False
    for item in box:
        if item[0] == label:
            found = True
            item[1] = step  # replace step
            break
    if not found:
        box.append([label, step])


def remove_from_boxes(boxes, input):
    label, _ = input.split('-')
    key = calc_hash(label)
    box = boxes.get(key, None)
    if box:
        for i, item in enumerate(box):
            if item[0] == label:
                del box[i]
                if len(box) == 0:
                    del boxes[key]
                break


def update_boxes_operation(boxes, input):
    if '=' in input:
        add_to_boxes(boxes, input)
    elif '-' in input:
        remove_from_boxes(boxes, input)


def update_boxes_operations(boxes, inputs):
    for input in inputs:
        update_boxes_operation(boxes, input)


def get_focusing_power(boxes):
    power = 0
    for box_idx, box in boxes.items():
        for slot_num, item in enumerate(box, start=1):
            box_num = box_idx + 1
            power += box_num * slot_num * item[1]
    return power
