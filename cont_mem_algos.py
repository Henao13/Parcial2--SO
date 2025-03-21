def worst_fit(memory, required, index):
    n = len(memory)
    if n == 0:
        return None
    candidate_index = None
    max_limit = -1
    for i in range(n):
        idx = (index + i) % n 
        base, limit = memory[idx]
        if limit >= required and limit > max_limit:
            candidate_index = idx
            max_limit = limit
    if candidate_index is None:
        return None
    base, limit = memory[candidate_index]
    new_base = base + required
    new_limit = limit - required
    if new_limit > 0:
        memory[candidate_index] = (new_base, new_limit)
        new_index = candidate_index
    else:
        memory.pop(candidate_index)
        new_index = candidate_index % len(memory) if memory else 0

    return memory, new_base, new_limit, new_index



