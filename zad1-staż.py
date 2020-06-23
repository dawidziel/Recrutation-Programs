def in_between(str1,str2):
    list_in_between = []
    str1 = [int(s) for s in str1.split("-")]
    str2 = [int(s) for s in str2.split("-")]
    for x in range(str1[0],str2[0]+1):
        if x == str2[0]:
            for y in range(0,str2[1]):
                list_in_between.append(str(x) + "-" + str(y))
        else:
            for y in range(str1[1]+1,1000):
                list_in_between.append(str(x) + "-" + str(y))
            x += 1
    return list_in_between
def main():
    str1 = "79-900"
    str2 = "80-155"
    print(in_between(str1,str2))
if __name__ == "__main__":
    main()