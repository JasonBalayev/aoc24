test, ex_one, unordered_updates = "5/input.txt", "5/ex_one.txt", []
file = test

def read_input(file):
    ordering, updates = [], []
    with open(file) as f:
        # read ordering until an empty line is encountered
        for line in f:
            line = line.strip()
            if line == "": break
            else:
                a, b = line.split("|")
                ordering.append((int(a), int(b)))
        
        # read updates
        for line in f:
            line = line.strip()
            if line == "": continue
            updates.append(list(map(int, line.split(","))))
    return 0, ordering, updates

def get_middle_number(lst):
    return lst[len(lst) // 2]

# P1
def print_queue():
    cnt, ordering, updates = read_input(file)

    for i in range(len(updates)):
        # check if a page in an update list is before the page in the ordering
        is_before = True
        for a, b in ordering:
            if a in updates[i]:
                try:
                    pos_b = updates[i].index(b)
                    pos_a = updates[i].index(a)

                    if pos_b < pos_a:
                        is_before = False
                        if updates[i] not in unordered_updates:
                            unordered_updates.append(updates[i])
                except ValueError:
                    pass

        # check if a page in an update list is after the page in the ordering
        is_after = True
        for a, b in ordering:
            if b in updates[i]:
                try:    
                    pos_a = updates[i].index(a)
                    pos_b = updates[i].index(b)
                
                    if pos_b < pos_a:
                        is_after = False
                        if updates[i] not in unordered_updates:
                            unordered_updates.append(updates[i])
                except ValueError:
                    pass

        # if a update list has all pages follow the order rules, 
        # then we add the middle page number to the count
        if is_before and is_after:
            cnt += get_middle_number(updates[i])

    return cnt

print(print_queue())

def find_orders(lst, ordering):
    orders = []
    for a, b in ordering:
        if a in lst or b in lst:
            orders.append((a, b))
    return orders

def order_update(lst, orders):
    while not is_ordered(lst, orders):
        for a, b in orders:
            if a in lst and b in lst:
                if lst.index(a) > lst.index(b):
                    # swap a and b if a is after b
                    lst.remove(a)
                    lst.insert(lst.index(b), a)
    return lst

def is_ordered(lst, orders):
    for a, b in orders:
        if a in lst and b in lst:
            if lst.index(a) > lst.index(b):
                return False
    return True

# P2
def order_unordered_updates():
    cnt, ordering, _ = read_input(file)
    upts = unordered_updates
    
    for lst in upts:
        orders = find_orders(lst, ordering)
        lst = order_update(lst, orders)
        cnt += get_middle_number(lst)
        
    return cnt

print(order_unordered_updates())