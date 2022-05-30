#include <iostream>
#include <math.h>

main() {
    int QInimigo, X, Y, I=0, II=0, III=0, IV=0;
	
    scanf("%d", &QInimigo);

    while (QInimigo > 0){
        scanf("%d %d", &X, &Y);

        if(X > 0 && Y > 0){
            I++;
        }
        else if(X > 0  && Y < 0){
            II++;
        }
        else if(X < 0 && Y > 0){
            IV++;
        }
        else if(X < 0 && Y < 0){
            III++;
        }

        QInimigo--;
    }

    printf("I = %d\n", I);
    printf("II = %d\n", II);
    printf("III = %d\n", III);
    printf("IV = %d\n", IV);

}