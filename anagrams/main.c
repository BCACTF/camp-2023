#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define FLAG_SIZE 37
#define SPACE 12

int isAnagramOfSize(char* word, int n) {
    if (strlen(word) != n) {
        return 0;
    }
    else {
        // check if word is an anagram by looping over it and checking if each character is at the end of the word
        for (int i = 0; i < n; i++) {
            if (!(word[i] == word[n - i - 1])) {
                return 0;
            }
        }
    }
    return 1;
}

int main(int argv, char **argc) {
    
    printf("Welcome to bofed!\n");
    printf("The game is simple: I'll tell you a number, and you have to tell me an anagram of that length.\n");
    printf("Let's see how far you can get!\n");
    
    int count = 0;
    char* flagCopy;

    while (count < 100000) {    
        srand(time(NULL));
        int n = rand() % 7 + 1;
        char word_flag[FLAG_SIZE+12+SPACE];
        
        FILE* f = fopen("flag.txt", "r");
        fgets(word_flag+n+1+SPACE, FLAG_SIZE, f);
        fclose(f);

        strcpy(flagCopy, word_flag+n+1+SPACE);
        // We already know where the string will end, so we can place a null terminator there
        *(word_flag + n+1) = '\0';
        
        printf("Give me an anagram of length %d: ", n);
        
        //load the input into the string word
        int c;
        int lettercount=0;
        while ((c = getchar()) != '\n' && c != EOF) {
            *(word_flag+(lettercount++)) = c;
        }

        printf("Checking the validity of the anagram... %s\n", word_flag);
        
        int correct = isAnagramOfSize(word_flag, n);

        if (correct) {
            printf("Correct!\n");
            count++;
        } else {
            printf("Incorrect!\n");
            printf("You got %d correct!\n", count);
            return 0;
        }
    }

    printf("You got 100000 correct! Here's your flag: %s\n", flagCopy);
    
    return 0;
}