def reverse_string(s):
    # INTENTIONAL BUG: Sorting the string alphabetically instead of reversing it.
    return "".join(sorted(list(s)))
