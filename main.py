from algs import minmax

def main():

    l = [1000, 12, 390, 1, 9]

    low,high = minmax.minmax_2(l)

    print(low)
    print(high)

if __name__ == "__main__":
    main()