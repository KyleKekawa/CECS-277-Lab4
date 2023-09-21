import check_input

def read_maze(file):
  file = open("maze.txt")
  list2d = []
  for row in file:
    items = row.strip()
    list = []
    for item in items:
      list.append(item)
    list2d.append(list)
  return list2d

  for num in list2d:
    for num2 in num:
      print(num2, end = "")
    print()
  
def find_start(maze):
  for i, row in enumerate(maze):
    for j, column in enumerate(row):
      if column == 's':
        return [i, j]
  

def display_maze(maze, loc):
  for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if [i, j] == loc:
                print('X', end='')
            else:
                print(f'{char}', end='')
        print()

def main():
  print("- Maze Solver -")
  get_maze = read_maze("maze.txt")
  loc = find_start(get_maze)


  while True:
    display_maze(get_maze, loc)
    print("1.Go North")
    print("2.Go South")
    print("3.Go East")
    print("4.Go West")
    val = check_input.get_int_range("Enter Choice: ", 1, 4)

    if val == 1:
      new_loc = [loc[0] - 1, loc[1]]
    if val == 2:
      new_loc = [loc[0] + 1, loc[1]]
    if val == 3:
            new_loc = [loc[0], loc[1] + 1]
    if val == 4:
            new_loc = [loc[0], loc[1] - 1]

    if get_maze[new_loc[0]][new_loc[1]] == '*':
            print('You cannot move there. That is a wall.')
    else:
            loc = new_loc

    if get_maze[loc[0]][loc[1]] == 'f':
                loc = new_loc
                display_maze(get_maze, loc)
                print('Congratulations! You solved the maze.')

            
                break
    
    
if __name__ == '__main__':
      
  main()
