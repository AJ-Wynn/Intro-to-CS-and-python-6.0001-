# Problem Set 4A
# Name: Andrew Wynn
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    

    if len(sequence) == 1:
        perm_list = [sequence]
        return perm_list
    
    else:
        
        # Returns a list of all possible permutations of the sequence minus the first character
        perm_list = get_permutations(sequence[1:])
        first_char = sequence[0]
        perm_list_new = []
        
        # Loop through each element, inserting first_char at each index in each element and appending that to perm_list_new
        for element in perm_list:
            for index in range(len(element) + 1):
                new_element = element[:index] + first_char + element[index:]
                perm_list_new.append(new_element)
            
        return perm_list_new
                
    
    
    
#print(get_permutations('abc'))

#1. Find the simplest case (base case)
#2. Play around with examples and visualize.
#3. Relate the harder cases to the simpler cases.
#4. Generalize pattern.  
#5. Combine recursive pattern with base case using code.

  

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

