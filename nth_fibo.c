#include<stdio.h>
int nth_fibo(int num){
	int a=0,b=1,c,i;
	if(num==0){
	return a;
}for(i=2;i<=num;i++){
	c = a+b;
	a = b;
	b = c;
}
	return b;
	
}
int main(){
	int n;
	scanf("%d",n);
	printf("%d",nth_fibo(n));
	return 0;
}
