import random

def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.

    # your code here
    path = [(0, 0)]
    x, y = 0, 0
    while (x, y) != (N - 1, M - 1):
        directions = []
        if x + 1 < N:
            directions.append((x + 1, y))
        if y + 1 < M:
            directions.append((x, y + 1))
        if not directions:
            break
        next_cell = random.choice(directions)
        path.append(next_cell)
        x, y = next_cell
    
    # Ensure the bottom-right cell is in the path
    if (N-1, M-1) not in path:
        path.append((N-1, M-1))
    
    return path

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    """Add a minimum number of obstacles randomly to the maze."""
    obstacles_added = 0
    while obstacles_added < min_obstacles:
        x, y = random.randint(0, N - 1), random.randint(0, M - 1)
        if maze[(x, y)] == 0:
            maze[(x, y)] = 1
            obstacles_added += 1

def set_obstacle(maze, path, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    """Set an obstacle at a given coordinate."""
    while True:
        try:
            x, y = map(int, input("Enter the coordinates to set an obstacle (i,j): ").split(","))
            if (x, y) not in maze:
                raise KeyError("Invalid coordinates. Please input coordinates within the range.")
            elif maze[(x, y)] == 2 or (x, y) in path:
                print("Cannot place an obstacle on the path.")
            elif maze[(x, y)] == 1:
                print("Obstacle already exists at this location.")
            else:
                maze[(x, y)] = 1
                print(f"Obstacle placed at {x,y}.")
                print_maze(maze, path, N, M)
                break
        except ValueError:
            print("ValueError in set_obstacle function. Need to be coordinates.")
        except KeyError as e:
            print(f"KeyError in set_obstacle function. {e}")

def remove_obstacle(maze, path, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    """Remove an obstacle at a given coordinate."""
    while True:
        try:
            x, y = map(int, input("Enter the coordinates to remove an obstacle (i,j): ").split(","))
            if (x, y) not in maze:
                raise KeyError("Invalid coordinates. Please input coordinates within the range.")
            elif maze[(x, y)] == 2 or (x, y) in path:
                print("Obstacle does not exist on the path.")
            elif maze[(x, y)] == 0:
                print("Obstacle does not exist at this location.")
            else:
                maze[(x, y)] = 0
                print(f"Obstacle removed at {x,y}.")
                print_maze(maze, path, N, M)
                break
        except ValueError:
            print("ValueError in remove_obstacle function. Need to be coordinates.")
        except KeyError as e:
            print(f"KeyError in remove_obstacle function. {e}")

def print_maze(maze, path, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.

    # your code here
    """Print the current state of the maze including the path."""
    print("+" +"---+"*(M-1))
    for i in range(N):
        for j in range(M-1):
            print("|",end = '')
            if (i, j) in path:
                print(' O ', end='')
            elif maze[(i, j)] == 0:
                print('   ', end='')
            elif maze[(i, j)] == 1:
                print(' X ', end='')
        print("|",end='')
        print()
        print("+" +"---+"*(M-1))

def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    # load grid
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line, end='')

                N = len(lines) // 2
                M = len(lines[0].strip().split('+')) - 1
                maze = {}
                for i in range(N):
                    for j in range(M):
                        maze[(i, j)] = 0
            break
        except IOError:
            print("IOError occurred in main function. File not found. Please enter a valid filename.")

    path = generate_path(N, M)
    for (x, y) in path:
        maze[(x, y)] = 2

    while True:
        try:
            min_obstacles = int(input(f"Enter the minimum number of obstacles (0-{N*M - len(path)}): "))
            if min_obstacles < 0 or min_obstacles > N*M - len(path):
                raise ValueError("Invalid number of obstacles.")
            break
        except ValueError:
            print("ValueError occurred in main function. Invalid number of obstacles.")

    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, path, N, M)

    while True:
        print("Option:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                set_obstacle(maze, path, N, M)
            elif option == 2:
                remove_obstacle(maze, path, N, M)
            elif option == 3:
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid option. Please choose a valid option.")

main()