cdef int cython_difference(str str1, str str2):
    """
    Compare two strings split by '_', counting different elements at the same index.
    """
    cdef list list1 = str1.split('_')
    cdef list list2 = str2.split('_')
    cdef int count = 0
    cdef int i
    
    for i in range(6): #todo: remove hardcode number
        if list1[i] != list2[i]:
            count += 1
    
    return count

def attribute_diff_count(str str1, str str2):
    """Python-accessible wrapper for cython_difference"""
    return cython_difference(str1, str2)