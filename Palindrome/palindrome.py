def generatePalindromes(A,n):
    
    result = [] #new list
    init_array = []
    subarray = []
    new_string = ""
    added_string = ""
    half_string = ""
    rev_string = ""
    palindrome_string = ""
    array_size = len(A) #size of list A
    half = int(n/2)
    mid = 0
    global count

    if n is 0 or array_size is 0: #if A is empty, return empty
        return {''}

    else:

        for i in range (0, array_size) : # ex) ['a','b','c']
            if n == 1:
                result.append(A[i]) # ex)['a','b','c']
            else:
                for j in range(0, array_size):

                    added_string = (A[i] + A[j]) #ex) aa, ab, ac, ba, bb,...

                    if n == 2 and (added_string[0] == added_string[1]):
                        result.append(added_string)

                    subarray.append(added_string)

                    for k in range(0, len(subarray)):

                        if (n % 2) != 0:
                            half_string = added_string[half:len(added_string)]  # length 2
                            rev_string = half_string[::-1]
                            new_string = subarray[k] + rev_string  # length 4

                            if (new_string == new_string[::-1]):
                                result.append(new_string)

                        else :

                            for z in range(0, len(subarray)):

                                if (n % 2) == 0 and n != 2: #length 4
                                    added_string = subarray[k] + subarray[z]

                                    if (added_string == added_string[::-1]):
                                        result.append(added_string)

                                    if (n > 4):
                                        added_string = added_string * 2
                                        ten_rev = added_string[0:half]
                                        ten_string = ten_rev + ten_rev[::-1]

                                        if (added_string == added_string[::-1]):
                                            result.append(ten_string)


        return (set(result))

def countPalindromes(A, n):

    # call A[i] and see if they are palindrome and count

    array_size = len(A)
    element_string = ""

    if n is 0 or len(A) is 0:
        return 1

    else:
        if (n % 2) is 0:
            count = (n / 2)
            return (array_size**count)
        else:
            count = (n + 1) / 2
            return (array_size**(count))
