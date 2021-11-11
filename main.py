from utils import *
from utils.button import Button 


def get_row_col_from_pos(pos):
    x, y = pos 
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row,col


def init_grid(rows,cols,color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid

def draw_grid(win,grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j * PIXEL_SIZE,i * PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win,LIGHT_GREY,(0,i * PIXEL_SIZE),(WIDTH,i * PIXEL_SIZE))
        for j in range(COLS + 1):
            pygame.draw.line(win,LIGHT_GREY,(j * PIXEL_SIZE,0),(j * PIXEL_SIZE,HEIGHT - TOOLBAR_HEIGHT))



def draw(win,grid,buttons):
    win.fill(BG_COLOR)
    draw_grid(win,grid)

    for button in buttons:
        button.draw(win)
    pygame.display.update()

def floodFill(grid,x,y,color):
    if x < 0 or x >= len(grid) or y < 0 or y >=  len(grid[0]) or grid[x][y] == BLACK or grid[x][y] == color:
        return

    grid[x][y] = color
    floodFill(grid,x + 1, y ,color)   
    floodFill(grid,x - 1, y ,color) 
    floodFill(grid,x,y + 1,color)  
    floodFill(grid,x,y - 1 ,color)



WIN  = pygame.display.set_mode((WIDTH,HEIGHT))
draw_mode = True
fill_mode = False
pygame.display.set_caption("pypaint")
run = True
grid = init_grid(ROWS,COLS,BG_COLOR)
clock = pygame.time.Clock()
drawing_color = BLACK
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10,button_y,50,50,BLACK),
    Button(70,button_y,50,50,RED),
    Button(130,button_y,50,50,GREEN),
    Button(190,button_y,50,50,BLUE),
    Button(250,button_y,50,50,WHITE,"Erase",BLACK),
    Button(310,button_y,50,50,WHITE,"Clear",BLACK),
    Button(370,button_y,50,50,WHITE,"Fill",BLACK),
    ]

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row,col = get_row_col_from_pos(pos)
                if fill_mode:
                    floodFill(grid,row,col,drawing_color)
                else:
                    grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    else:
                        if button.text == "Fill":
                            # row,col = get_row_col_from_pos(pos)
                            # floodFill(grid,row,col,drawing_color)
                            fill_mode = True
                            draw_mode = False
                        elif button.text == "Clear":
                            draw_mode = True
                            fill_mode = False
                            grid = grid = init_grid(ROWS,COLS,BG_COLOR)
                            drawing_color = BLACK
                        else:
                            drawing_color = button.color
                            draw_mode = True
                            fill_mode = False

    draw(WIN,grid,buttons)
pygame.quit()

