#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char* getString() {
    int bufferSize = 1;
    int length = 0;
    char* input = (char*) malloc(bufferSize * sizeof(char));

    if (input == NULL) {
        printf("Memory allocation failed.\n");
        return "";
    }

    char c = getchar();
    while (c != '\n' && c != EOF) {
        input[length++] = c;

        if (length >= bufferSize) {
            bufferSize *= 2;
            input = (char*)realloc(input, bufferSize * sizeof(char));
            if (input == NULL) {
                printf("Memory reallocation failed.\n");
                return "";
            }
        }

        c = getchar();
    }

    input[length] = '\0';
    return input;
}

int getNumber(x) {
    return x/2;
}

int indexOf(char* password, char thing) {
    for (int i = 0; password[i] != '\0'; i++) {
        if (password[i] == thing) {
            return i;
        }
    }

    return -1;
}

int checkLength(char* password) {
    int x=0,y=0;

    for (int i = 0; i <= getNumber(89); i+=2) x++;
    for (int i = 0; password[i] != '\0'; i++) y++;

    return x==y;
}

int checkDigits(char* password) {
    int x=0, y=0;

    for (int i = 0; password[i] != '\0'; i++) {
        if (isdigit(password[i])) {
            x += password[i] - '0';
            y++;
        }
    }

    return getNumber(19)==x && getNumber(13)==y;
}

int checkUnderscore(char* password) {
    int underscoreIndex = indexOf(password, '_');
    int x = 0;

    for (int i = 0; password[i] != '\0'; i++) {
        if (password[i] == '_') {
            x++;
        }
    }

    return underscoreIndex == 13 && getNumber(3) == x;
}

int checkLetters(char* password) {
    int firstWordIndex = indexOf(password, '{')+1;
    int secondWordIndex = indexOf(password, '_')+1;
    int firstWordLastIndex = indexOf(password, '_')-1;
    int secondWordLastIndex = indexOf(password, '}')-1;

    if (!(password[firstWordIndex] == 'C' && password[++firstWordIndex] == '0')) {
        return 0;
    }

    if (!(password[firstWordLastIndex] == 'R' && password[--firstWordLastIndex] == '3')) {
        return 0;
    }

    if (!(password[secondWordIndex] == 'c' && password[++secondWordIndex] == 'H')) {
        return 0;
    }

    if (!(password[secondWordLastIndex] == 'n' && password[--secondWordLastIndex] == '0')) {
        return 0;
    }

    return 1;
}

int checkASCII(char* password) {
    int x = 0;

    for (int i = 0; password[i] != '\0'; i++) {
        x += password[i];
    }

    return x == getNumber(3947);
}

int checkIndexOf(char* password) {
    char* passwordMinusCamp = password+getNumber(11);
    return indexOf(passwordMinusCamp, 'p') == -1;
}

int checkFlag(char* password, char* flag) {
    for (int i = 0; password[i] != '\0'; i++) {
        if (password[i] != flag[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char* flag = "camp{C0mP1l3R_cH4mP10n}";

    printf("Enter your password: ");
    char* password = getString(); 

    if (checkLength(password) && checkDigits(password) && checkUnderscore(password) && checkLetters(password) && checkASCII(password) && checkIndexOf(password) && checkFlag(password, flag)) {
        printf("Correct");
    }
    else {
        printf("Incorrect");
    }
    
}