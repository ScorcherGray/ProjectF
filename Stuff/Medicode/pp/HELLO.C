/* hello.c: Greet the either the user or the world */ 
#include <stdio.h>

main(int argc, char *argv[])
{
    if (argc > 1 && argv[0] != NULL)
        printf("Hello, %s!\n",argv[1]);
    else
        printf("Hello, world!\n");
    return 0;
}
