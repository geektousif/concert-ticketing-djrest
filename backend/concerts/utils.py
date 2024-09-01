import string


def generate_row_alphabets(num_rows):
    rows = []
    alpahabet = string.ascii_uppercase

    for i in range(1, num_rows + 1):
        label = ""
        n = i

        while n > 0:
            n, remainder = divmod(n - 1, 26)
            label = alpahabet[remainder] + label

        rows.append(label)

    return rows
