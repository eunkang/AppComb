import time

#DO NOT MODIFY THE FUNCTION BELOW
def memoize(f):
    memo = {}
    def helper(x):
        if x == "clear":
            memo.clear()
            return
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def configs(n):

    # initializing strings and numbers
    str = ""
    ans_set = set()

    #Base Cases
    if n is 0:
        return set(str)

    if n is 1:
        str = "M"
        return set(str)

    if n is 2:
        #return set_2
        ans_set.add("MM")
        ans_set.add("C")
        return ans_set

    #Recursive step
    else:

        new_set = configs(n-1)

        for i in new_set:
            i = i + "M"
            ans_set.add(i)

        new1_set = configs(n - 2)

        for i in new1_set:
            i = i + "C"
            ans_set.add(i)

        return ans_set


@memoize
def count(n):

    # Base Cases
    if n is 0:
        return 0
    if n is 1:
        return 1
    if n is 2:
        return 2
    else:
        return count(n - 1) + count(n - 2)


for n in range(11):
    start = time.time()
    configs(n)
    end = time.time()
    configs("clear")
    print(end - start)