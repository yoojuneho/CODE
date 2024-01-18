#include <stdio.h>

int main(){
  int a,b;
  printf("정수를 입력하세요");
  scanf("%d %d", &a, &b);

  if(a < -10000 || a > 10000 || b < -10000 || b > 10000){
    return 1;
  }

  if(a<b){
    printf("<");
  } else if(a>b){
    printf(">");
  } else {
    printf("==");
  }

  return 0;
}