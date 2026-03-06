if __name__ == '__main__':

    print('Bootcamp')

    print('Hello World ')

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers[9])
    print(numbers[1:5]) #concept of slicing
    print(numbers[7:9])
    print(numbers[-4:-1]) #concept of reverse slicing
    numbers.append(11)
    print(numbers)
    numbers[9] = 100
    print(numbers)
    x = numbers[0]
    print(x)
    for i in numbers :
        print(i)
    
    a = 10
    b = 5
    if a>b:
        print("a is greater than b")
    elif a < b:
        print("a is less than b ")
    else:
        print("a = b ")

    if a%2 == 0:
        print("a is even")
    else:
        print("a is odd ")
    
    names = []
    print(names)
    names.append(1)
    print(names)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num = []
    for i in numbers:
        if i%2 == 0:
            num.append(i)
    print(num)
    for i in range(0 ,len(numbers),1): #skip one step at a time
        print(numbers[i])

    numbers = [10, 5, 3, 4, 5, 7, 2, 8, 9, 1]
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    print(max)

    min = numbers[0]
    for num in numbers:
        if num > min:
            min = num
    print(max)
#dictonary :keys are always string , dictionary maintains key value pair, we use square bracket to add the key , cannot have duplicate keys in dictionary

    d = { }
    d ["a"] =5
    d ["b"] =6
    print(d)
    d["a"] = d["a"]+1
    print(d)
    d["c"] = 10
    d["c"] = 11 #replaces the value of c as 11
    print(d)
    x ="b"
    if x in d:
        print(d[x]) # in operator to evalute the dictonary check
    else : print("key does not exist in a dictionary ")


    numbers = [10, 5, 3, 4, 5, 7, 2, 8, 9, 1,1,2,3]
    #count the number of 4
    target = 1
    # you will always have to define target in this ,
    # if someone wants the value of all the multiple values that's when dictionary comes in play
    count = 0
    for i in numbers:
        if i == target :
            count += 1
    print(count)

    numbers = [10, 20, 20, 30]
    d = {}
    for num in numbers:
        if num in d:
            d[num] = d[num]+1
        else :
            d[num] =1
    print(d)
    #d ={10:1,20:2,30:1} this is called dry run> execute in mind

    #if the user has to print number with max ocurrences

    max =0
    freq = 0
    for key in d.keys():
        value =d[key]
        if value > freq:
            max = key
            freq = value
    print(max)

    line = "Hello world hi world hi Nepal"
    words = line.split(' ')  #splitting this line on the basis of space called delimeter
    print(words)
    # word in the maximum occurrences
    word_counts= { }
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] +1
        else:
            word_counts[word] = 1
    print(word_counts)
    max = 0
    freq = 0
    for key in word_counts.keys():
        value = word_counts[key]
        if value > freq:
            max = key
            freq = value
    print(max)
# set
    list = [1, 2, 2, 3, 4, 4, 5]
    s = set (list)
    print(s)
    output = []
    set = set()
    for num in list:  # order of O(n)
        if num not in set:  # not in operator is o(n) but as we used set it is O(1)
            output.append(num)
            set.add(num)
    print(output)
    # this function will convert into set but the order is not granted as this is set
    output =[]
    # if asked to  maintain order
    list = [1, 2, 2, 3, 4, 4, 5]
    prev = list[0]    #1 # in this time complexity is o(n) and space complexity is O(n)
    output.append(prev)  #output(1)
    for num in list:  #order of O(n)
        if num != prev:
            output.append(num)
            prev = num
    print(output)
    



























