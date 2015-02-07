#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>
#include<errno.h>

int main(int argc, char *argv[]) {
  pid_t pid;
  pid_t processID = getpid();
  printf("Current process ID = %d\n", processID);
  printf("Hello\n");
  printf("Fork occurs now:\n");
  printf("------------------------\n");
  pid = fork();
  printf("Return value of fork is: %d\n", pid);
  printf("Current Process is %d, Parent Process is: %d\n", getpid(), getppid());
  printf("world\n");
  return 0;
}

/* 
  Explination: 
  - Line 11 prints the current process ID, that is, the process ID of this program
  - Everything continues as normal until line 15, where a fork system call occurs
  - Each time you call fork it returns twice. Once in the parent, once in a new process.
  - You will see the print statement exectured in line 16 twice- one gives the PID of the child and is executed as part of the parent
    The other gives 0, and is executed as part of the child process.
  - In fact, everything after the for system call in line 15 is executed twice, once in the parent process and once in the child
  - This is because After a new child process is created, both processes will execute the next instruction following the fork() 
    system call.  
  - Normally, with each for system call you'd have something like this to handle it:
    
    switch (fork()) {
      case -1:
        break; an, error
      case 0:
        break; child process execution
      default:
        break; parent process execution
    }
 */
