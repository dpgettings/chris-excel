import numpy as np

# Note: Since Python starts indexing at 0, the mapping is:
#   B2 --> Array[0]
#   B3 --> Array[1]
#   B4 --> Array[2]

"""
Set up a function to return the correct code depending on the condition
*Note*: Functions must be defined before they are used. You have to
        build the machinery before you run inputs through it.
"""
def return_argument_code(cond_vals):

    ### Sort the array from Large-->Small ###
    # In Python, you first sort from Small-->Large
    #    and then swap the order with the crazy construction [::-1]
    cond_vals_descending = np.copy(np.sort(cond_vals)[::-1])

    # A nice thing to do: group answers that return the same code using OR
    if (cond_vals[0] == cond_vals[1] == cond_vals[2] or cond_vals[0] == cond_vals[1] or cond_vals[1] == cond_vals[2]):
        return "DP_B"

    # "Second-largest value" is equivalent to "2nd element of Large-->Small sorted array"
    elif cond_vals[0] == cond_vals[2] or cond_vals_descending[1] == cond_vals[0]:
        return "GMO_B"

    elif cond_vals_descending[1] == cond_vals[2]:
        return "MJ_B"

    ### This is the "Failure to match anything" condition ###
    else:
        return None

"""
Set Values, and then test the return values of the function
"""
### An initial test ###
# The values of the B cells
B2=1
B3=1
B4=2
# Put these values into an array
B = np.array([B2, B3, B4])  
# Test the return value of the function
print return_argument_code(B)
# prints: DP_B


### Check another set of values ###
B_again = np.array([2, 4, 3])
print return_argument_code(B_again)
# prints: MJ_B


### Check yet another set of values ###
even_more_values = np.array([2, 8, 2])
print return_argument_code(even_more_values)
# prints: GMO_B


### Here's a fun special case that prints None ###
# [np.nan is NaN (Not A Number) which fails all equality tests, forever]
nan_values = np.array([np.nan, np.nan, np.nan])
print return_argument_code(nan_values)
# prints: None

