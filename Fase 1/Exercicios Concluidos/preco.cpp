#include <iostream>
#include <math.h>

main() {
    double Tr, P, V, F;

    scanf("%lf", &Tr);
    scanf("%lf", &P);
    scanf("%lf", &V);

    if (Tr >= 0 && P >= Tr && V >= 0){
        P = P-Tr;
        F = P*V;

        printf("%.2lf\n", F);
    }

    
}
