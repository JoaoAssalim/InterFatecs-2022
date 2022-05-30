#include <iostream>
#include <math.h>

main() {
    int cont;
    double I, A, T;
    bool p = true;

    scanf("%lf", &I);
    scanf("%lf", &A);
    scanf("%lf", &T);

    if (I >= A){
        printf("pode comprar agora");
    }
    else{
        while (p == true){
            I = I + I*T/100;
            cont ++;
            if (I >= A){
                p = false;
            }
        }
        if (cont > 1){
            printf("possivel em %d meses", cont);
        }
        else{
            printf("possivel em %d mes", cont);
        }

    }

    
}
