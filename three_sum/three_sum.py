def threeSum(nums):
    # Initialize a set to store unique triplets that sum to zero
    res = set()

    # Initialize sets for positive numbers, negative numbers, and count of zeros
    N, P, z = set(), set(), 0

    # Initialize sets to keep track of duplicates in positive and negative numbers
    p_dub, n_dub = set(), set()

    # Iterate over the numbers to categorize them into positive, negative, or zero
    for num in nums:
        if num > 0:  # Positive numbers
            if num in P:  # Check for duplicates
                p_dub.add(num)
            else:
                P.add(num)
        elif num < 0:  # Negative numbers
            if num in N:  # Check for duplicates
                n_dub.add(num)
            else:
                N.add(num)
        else:  # Zero
            z += 1

    # If there is at least one zero, find pairs of positive and negative numbers that are negations of each other
    if z:
        for num in P:
            if -num in N:
                res.add((-num, 0, num))

    # If there are three or more zeros, add the triplet (0,0,0) to the result set
    if z >= 3:
        res.add((0, 0, 0))

    # Convert sets of positive and negative numbers to lists for iteration
    n, p = list(N), list(P)

    # Find two negative numbers that sum up to the negation of a positive number
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # Find two positive numbers that sum up to the negation of a negative number
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    # For duplicates among positive numbers, check if their double negation is in negative numbers
    for i in p_dub:
        if -2 * i in N:
            res.add(tuple([i, i, -2 * i]))

    # For duplicates among negative numbers, check if their double negation is in positive numbers
    for i in n_dub:
        if -2 * i in P:
            res.add(tuple([i, i, -2 * i]))

    # Return the set of unique triplets
    return res