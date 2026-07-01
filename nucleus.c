#include <stdio.h>
#include <string.h>

int main() {
    char input[256];
    printf("KANDO-CORE: SYSTEM READY. ENTER COMMAND:\n");
    
    while(1) {
        printf("> ");
        if (fgets(input, sizeof(input), stdin) == NULL) break;
        
        // حذف کاراکتر خط جدید
        input[strcspn(input, "\n")] = 0;

        if (strcmp(input, "EXIT") == 0) {
            printf("KANDO-CORE: SHUTTING DOWN.\n");
            break;
        } else {
            printf("KANDO-CORE RECEIVED: %s | PROCESSED: ACKNOWLEDGED.\n", input);
        }
    }
    return 0;
}