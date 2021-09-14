n = 8
def triangle(n):
    print(f"call triangle({n})")
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n-1)
        foo = list(range(len(last_row) - 1))
        for i in foo:
            last_n_sum = last_row[i] + last_row[i + 1]
            new_row.append(last_n_sum)
        new_row += [1]
    return new_row
print(triangle(n))
