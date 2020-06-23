def float_nums(x,y):
    nums = []
    while x <= y:
        nums.append(x)
        x += 0.5
    return nums
def main():
    print(float_nums(2,5.5))
if __name__ == '__main__':
    main()