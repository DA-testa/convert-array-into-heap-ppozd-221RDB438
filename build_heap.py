# python3
from pathlib import Path

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    s = len(data)
    for i in range(s//2, -1, -1):
        heap(data, i, swaps)
    return swaps

def heap(data, i, swaps):
    s = len(data)
    m_index = i
    l_ch = 2*i + 1
    r_ch = 2*i + 2
    if l_ch < s and data[m_index] > data[l_ch]:
        m_index = l_ch
    if r_ch < s and data[m_index] > data[r_ch]:
        m_index = r_ch
    if m_index != i:
        swaps.append((i, m_index))
        data[i], data[m_index] = data[m_index], data[i]
        heap(data, m_index, swaps)


def main():
    
    type = input()
    if "I" in type:
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    # checks if lenght of data is the same as the said lenght
        assert len(data) == n
    elif "F" in type:
        name = input()
        p = Path('./tests') / name
        with p.open() as fl:
            n = int(fl.readline())
            data = list(map(int, fl.readline().split()))
    else:
        print("Wrong input")
        return 0
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
