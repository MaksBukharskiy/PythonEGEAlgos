#include <stdio.h>
#include <math.h>
#include "stdlib.h"

#pragma warning(disable:4996)

FILE* open_file(const char* name, const char* mode) {
    FILE* f = fopen(name, mode);
    if (f == NULL) {
        printf("Не открыть файл %s\n", name);
    }
    return f;
}

int read_circle(FILE* f) {

    int kolvo_points = 0

    if(scanf(f, "%d", kolvo) == 1 && *kolvo > 0){
        kolvo_points = *kolvo

        point*
    }

}

int check_point(double r, double x, double y) {
    double dist = sqrt((x - CX) * (x - CX) + (y - CY) * (y - CY));
    if (dist <= r)
        return 1;
    else
        return 0;
}

void write_to_file(FILE* f, int ans) {
    if (ans == 1)
        fprintf(f, "YES\n");
    else
        fprintf(f, "NO\n");
}

int solver(point* arr, int kolvo_points, circle c){

    double x1x2, y1y2, sum;
    
    for(int i = 0; i < kolvo_points; i++){
        x1x2 = arr[i].x - c.x;
        y1y2 = arr[i].y - c.y;

        sum = (sqrt(sum) <= c.r) counter++;
    }

    return counter;
}


void main(){

    FILE*fin = open_file("input.txt", "r");


    if(fin){
        int kolvo_points_in_circle, kolvo_points;
        circle c = read_circle(fin);
        point* arr =read_points(fin, &kolvo_points);

        if(arr){
            kolvo_points_int_circle = solver(arr, kolvo_points, c)
        }
    }

    return 0;
}
