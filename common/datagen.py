
def generate_n_lined_file_randomly(filename, n):
    with open(filename, "w") as file:
        for i in range(1, n+1):
            file.write(f'This is line {i}\n')

    print("done")


generate_n_lined_file_randomly("wk1-input.txt", 69)
