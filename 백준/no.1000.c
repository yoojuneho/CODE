#include <stdio.h>

int add(){
  int a, b; // scanf를 사용할 때 변수 초기화
  scanf("%d", &a);
  scanf("%d", &b);
  if(a > 0 && b < 10){
    int sum = a + b;
    return sum; // 반환해야 함
  } else {
    return 1;
  }
}

int main(void){
  int result = add(); // add함수의 리턴타입이 int
  printf("%d", result); 
  return 0;
  
}