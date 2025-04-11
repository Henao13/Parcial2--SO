def first_fit(memory, required, index):
    pass

def best_fit(memory, required, index):
    pass

def worst_fit(memory, required, index):
    n = len(memory)
    if n == 0:
        return None
    candidate_index = None
    max_limit = -1
    for i, (base, limit) in enumerate(memory):
        if limit >= required and limit > max_limit:
            candidate_index = i
            max_limit = limit
    if candidate_index is None:
        return None
    base, limit = memory[candidate_index]
    allocated_base = base
    new_limit = limit - required
    if new_limit > 0:
        memory[candidate_index] = (base + required, new_limit)
        new_index = candidate_index
    else:
        memory.pop(candidate_index)
        new_index = candidate_index % len(memory) if memory else 0

    return memory, allocated_base, new_limit, new_index



