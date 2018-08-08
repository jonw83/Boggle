def make_grid(width, height):
    """
    Make an empty boggle grid. For zero leave curly brackets empty. For a grid that will hold all the tiles in a boggle game
    """
    return {(row, column): ' ' for row in range(height)
        for column in range(width)}
    """
    We create a dictionary {} with row and column tuples as the key and a space as the value
    """