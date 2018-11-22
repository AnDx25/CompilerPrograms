def common_prefix(strings):

    if len(strings) == 1:#rule out trivial case
        return strings[0]

    prefix = strings[0]

    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break

    return prefix


#if __name__=='__main__':
def left_factor(str):
    list=[]
    list1=[]
    arr1=str.split("->")
    list=arr1[1].split("|")
    factor = common_prefix(list)
    for w in list:
        list1.append(w.replace(factor,''))
    print("Required Output :")
    print(arr1[0],"->",factor+arr1[0]+'\'')
    for i in range(1,len(list1)+2,2):
        list1.insert(i,'|')
    print(arr1[0]+'\'->',*list1)

if __name__=='__main__':
    str=[]
    n=int(input('Enter the number of Non-Terminals(for which productions are present):'))# number of times run this program
    print("Enter the productions :")
    for i in range(n):
        str.append(input())
    for item in str:
        left_factor(item)
