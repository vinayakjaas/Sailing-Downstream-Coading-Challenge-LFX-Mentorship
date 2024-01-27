from typing import Iterable

def reduce(x : Iterable, skipevery : list[int] | int = None) -> Iterable:
    """Reduces the list / iterable size by skipping every `nth` index, as provided.

    Args:
        x (Iterable): list | Iterable to reduce. Must be a length of some multiple of 10.
        
        
        skipevery (list[int] | int, optional): Which indices to skip. If a single value is provided, all indices which are a multiple of this value is skipped. If a list of indices are provided, then all indices which are a multiple of any of these values is skipped. Defaults to [2, 3].

    Returns:
        Iterable: Reduced list.
    """
    
    
    #Checks if the iterable is of a size of multiple of 10.
    assert (len(x) % 10 == 0), f"Length of list must be a multiple of 10; found {len(x)} instead."
    
    
    #Sets default value of skipevery to [2, 3]. If it is a single value, it is turned into a list.
    if skipevery is None:
        skipevery = [2, 3]
    if type(skipevery) != list:
        skipevery = [skipevery]
    
    
    # newlist containing all the correct indiced elements.
    newlist = []
    
    #main for loop of the function.
    for i, each in enumerate(x):
        #assume value must not be skipped by default.
        skip = False
        
        #assume 0 is not a multiple of any positive integer.
        if i == 0:
            newlist.append(each)
            continue
        
        # if this index is a multiple of any value in skipevery, then it must be skipped.
        for ind in skipevery:
            if i % ind == 0:
                skip = True
                break
        
        #if not to be skipped, append to newlist and move on.
        if skip: continue
        
        newlist.append(each)
    
    return newlist

if __name__ == '__main__':
    test1 = list(range(1, 21))
    test2 = list(range(1, 11))
    
    c1 = [1, 2, 6, 8, 12, 14, 18, 20]
    c2 = [1, 2, 6, 8]
    
    cases = [
        ((test1,), c1),
        ((test2,), c2),
    ]
    
    success = 0
    for i, (t, c) in enumerate(cases):
        try:
            assert reduce(*t) == c
            success += 1
        except AssertionError:
            print(f"Failed testcase {i} t = {t}; c = {c}")
            print(f"Got {reduce(*t)}...")
    
    print(f"Passed {success}/{len(cases)} test cases...")