def count_ways(X, N):
    # Generate all powers less than or equal to X
    def generate_powers(X, N):
        powers = []
        base = 1
        while base ** N <= X:
            powers.append(base ** N)
            base += 1
        return powers

    # Recursive function to count the ways
    def find_ways(target, powers, index):
        if target == 0:
            return 1  # Found a valid combination
        if target < 0 or index == len(powers):
            return 0  # No valid combination possible

        # Include or exclude the current power
        include = find_ways(target - powers[index], powers, index + 1)
        exclude = find_ways(target, powers, index + 1)

        return include + exclude

    # Generate the powers
    powers = generate_powers(X, N)

    # Start recursive search
    return find_ways(X, powers, 0)

# Example Usage:
X=int(input())
N=int(input())
print(count_ways(X, N))  
