def lacking_values(n_list,n):
    full_list = []
    list_lacking_values = []
    for x in range(1,n+1):
        full_list.append(x)
    for x in range(1,len(full_list)):
        if full_list[x] not in n_list:
            list_lacking_values.append(full_list[x])
    return list_lacking_values
def main():
    n_list = [1,3,5,7,9]
    n = 11
    print(lacking_values(n_list,n))
if __name__ == "__main__":
    main()