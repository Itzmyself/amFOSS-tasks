def crossword_puzzle(grid, words):
    def can_place_horizontally(grid, word, row, col):
        if col + len(word) > 10:  
            return False
        for i in range(len(word)):
            if grid[row][col + i] not in ('-', word[i]):
                return False
        return True

    def place_horizontally(grid, word, row, col):
        original = []
        for i in range(len(word)):
            original.append(grid[row][col + i])
            grid[row][col + i] = word[i]
        return original

    def undo_horizontally(grid, original, row, col):
        for i in range(len(original)):
            grid[row][col + i] = original[i]

    def can_place_vertically(grid, word, row, col):
        if row + len(word) > 10:  
            return False
        for i in range(len(word)):
            if grid[row + i][col] not in ('-', word[i]):
                return False
        return True

    def place_vertically(grid, word, row, col):
        original = []
        for i in range(len(word)):
            original.append(grid[row + i][col])
            grid[row + i][col] = word[i]
        return original

    def undo_vertically(grid, original, row, col):
        for i in range(len(original)):
            grid[row + i][col] = original[i]

    def solve(grid, words):
        if not words:
            return True  

        word = words[0]
        remaining_words = words[1:]

        for row in range(10):
            for col in range(10):
                if can_place_horizontally(grid, word, row, col):
                    original = place_horizontally(grid, word, row, col)
                    if solve(grid, remaining_words):
                        return True
                    undo_horizontally(grid, original, row, col)

                if can_place_vertically(grid, word, row, col):
                    original = place_vertically(grid, word, row, col)
                    if solve(grid, remaining_words):
                        return True
                    undo_vertically(grid, original, row, col)

        return False 

    if solve(grid, words):
        return [''.join(row) for row in grid]
    else:
        return None  


grid = [input().strip() for _ in range(10)]
words = input().strip().split(';')

result = crossword_puzzle([list(row) for row in grid], words)
if result:
    for row in result:
        print(row)
else:
    print("No solution exists.")
