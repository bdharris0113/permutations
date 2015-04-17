#returns all permutations of any length [0,n]
def perm(word):

    if len(word) < 1:
        return ['']

    else:
        first = word[0]
        rest = word[1:]
        rest_list = perm(rest)
        answer = rest_list[:]

        for char in rest_list:
            for index in range(len(char)+1):
                answer.append(char[index:] + first + char[:index])

        return answer


#returns permutations of length n    
def perm2(word):

    if len(word) == 1:
        return [word]

    else:
        first = word[0]
        rest = word[1:]
        rest_list = perm2(rest)
        answer = []

        for char in rest_list:
            for index in range(len(char)+1):
                answer.append(char[index:] + first + char[:index])
        return answer                

def qsort(l):
    if len(l) == 0:
        return []
    else:
        pivot = len(l) / 2
        smaller = []
        bigger = []

        for index in l[:pivot] + l[pivot+1:]:
            if index <= l[pivot]:
                smaller.append(index)
            else:
                bigger.append(index)

        smaller = qsort(smaller)
        bigger = qsort(bigger)
        return smaller + [l[pivot]] + bigger
            
