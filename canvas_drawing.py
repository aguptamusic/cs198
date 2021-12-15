### Canvas Drawing ###

def draw(canvas, left, top, width, height, n):
    """
    Draw a series of lines starting at points across the top edge of the figure, all ending at the lower-right corner. 
    The first line should start at the upper left corner, the last line should start at the upper right corner, 
    with the other lines distributed evenly in between.
    """
    canvas.draw_rect(left, top, width, height, color='lightblue')
    
    # Question to ask: 
    # Among starting coordinates of each line:
    #   How (if at all) is x changing?
    #   How (if at all) is y changing?
    # Repeat for ending coordinates of each line.

    # First, find a formula in terms of given parameters for the non-changing coordinates.
    # Then, use a loop over the number of lines to calculate the changing coordinates.

    # Here: starting x coordinate changes. All else is constant.
    
    for i in range(n):
        x_add = (i / (n - 1)) * (width - 1)
        canvas.draw_line(left + x_add, top, left + width - 1, top + height - 1)

    """
    If n = 3 lines, each one is some fraction of the width.
    
    First line starts at x = (0 / (2)) * (4) = 0
    Second line starts at x = (1 / (2)) * (4) = 2
    Third line starts at x = (2 / (2)) * (4) = 4
    """

    """
    -1 Logic.
    Example: Draw a line across the top of the canvas, with

    Left = 0
    Width = 5
    | 0 | 1 | 2 | 3  | 4 |
    
    canvas.draw_line(left, top, ___, top)
    __ is width - 1. You do not want to draw to pixel 5.
    """