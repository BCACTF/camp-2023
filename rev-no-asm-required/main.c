#include <stdio.h>
#include <stdlib.h>

static int NO_ONE_WILL_EVER_FIND_THIS_mwahahahahaha = 0x6FED;

int main(int argv, char **argc) {
    int lol = 0xf00d;

    puts("Hey.");
    sleep(1);
    printf("Password? ");
    int password = 0;
    scanf("%d", &password);

    int actual_password = lol | (NO_ONE_WILL_EVER_FIND_THIS_mwahahahahaha << 16);

    if (actual_password == password) {
        system("/bin/sh");
    } else {
        puts("Cool");
        sleep(1);
        puts("Yeah thats wrong!");
    }

    return 0;
}

// 
// Hello people who solved this
// How does it feel to have shell haha
// 