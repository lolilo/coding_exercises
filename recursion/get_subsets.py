def get_subsets(l):
    if len(l) == 0:
        return [l]
    subsets = get_subsets(l[1:])
    # final = subsets # I SEE IT. AHHH. This causes an infinite loop later.
    final = subsets[::]
    el = l[0]
    for subset in subsets:
        final.append([el] + subset)
    return final

print get_subsets(range(4))
