#include "stdio.h"
#pragma warning(disable: 4996)

FILE* open_file(const char* name, const char* mode){
    return fopen(name, mode);
}

void write_to_file(FILE* f, int ans){
    fprint(f, "%d", ans);
}

int main(){
    



}