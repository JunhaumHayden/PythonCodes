import os

def main():
    children=[]
    # Create two child processes
    for _ in range(20):
        pid = os.fork()
        if pid == 0:
            # Child process
            print(f"Child process {os.getpid()} created.")
            os._exit(0) # Exit child process
        else:
            # Parent process
            children.append(pid)
            print(f"Parent process {os.getpid()} created child process {pid}.")

    for i in children:
        os.waitpid(i, 0) # Wait for child process to finish
        print(f"Child process {i} finished.")

    print("All child processes have finished.")


if __name__ == '__main__':
    main()
