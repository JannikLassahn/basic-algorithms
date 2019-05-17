import sorting

def k_selection(l, k):
    sorting.bubblesort(l)
    return l[len(l - k)]