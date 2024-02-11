def threeSum(nums):
    # Create a set to hold the unique triplets that add up to zero.
    res = set()

    # Create sets to separate the numbers into positive, negative, and keep track of zeros.
    N, P, z = set(), set(), 0  # N for negatives, P for positives, z for zero count.

    # Sets to remember which positive and negative numbers appear more than once.
    p_dub, n_dub = set(), set()

    # Go through each number in the input list.
    for num in nums:
        if num > 0:  # For positive numbers
            if num in P:  # If we've seen it before, remember it has a duplicate.
                p_dub.add(num)
            else:  # Otherwise, just add it to the set of positives.
                P.add(num)
        elif num < 0:  # For negative numbers
            if num in N:  # If we've seen this one before, remember the duplicate.
                n_dub.add(num)
            else:  # Add new negatives to the set of negatives.
                N.add(num)
        else:  # For zeros
            z += 1  # Just count how many zeros we have.

    # If we have any zeros, look for pairs of numbers that are negatives of each other.
    if z:
        for num in P:
            if -num in N:
                res.add((-num, 0, num))

    # If we have 3 or more zeros, then (0, 0, 0) is a valid triplet.
    if z >= 3:
        res.add((0, 0, 0))

    # Convert the sets of positives and negatives to lists so we can iterate over them.
    n, p = list(N), list(P)

    # Look for pairs of negatives that, when added, are the negation of a positive number.
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # Do the same for pairs of positives, looking for a corresponding negative number.
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    # Check if the double of a positive number's duplicate is a negative number.
    for i in p_dub:
        if -2 * i in N:
            res.add((i, i, -2 * i))

    # Similarly, check if the double of a negative number's duplicate is a positive.
    for i in n_dub:
        if -2 * i in P:
            res.add((i, i, -2 * i))

    # Return the unique triplets that sum up to zero.
    return res
