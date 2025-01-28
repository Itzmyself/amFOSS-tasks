def count_ways(X, N):
    def generate_powers(X, N):
        powers = []
        base = 1
        while base ** N <= X:
            powers.append(base ** N)
            base += 1
        return powers

    def find_ways(target, powers, index):
        if target == 0:
            return 1  
        if target < 0 or index == len(powers):
            return 0  

        include = find_ways(target - powers[index], powers, index + 1)
        exclude = find_ways(target, powers, index + 1)

        return include + exclude

    powers = generate_powers(X, N)

    return find_ways(X, powers, 0)

X=int(input())
N=int(input())
print(count_ways(X, N))  
