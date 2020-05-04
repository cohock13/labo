#include<stdio.h>

#define range 10 // 0 to range
#define dt 0.2
#define tau 3.0
#define a 2.0
#define x_0 0.0 //init

double f(double x,double t){
    return (a-x)/tau;
}

double euler(double x,double t){
    return x + dt*f(x,t);
}

FILE *fp;

int main(void){

	char filename[256];
    sprintf(filename, "data.txt");
	fp=fopen(filename,"w");

    double x = x_0,t = 0;
    long long i;
    long long step = range/dt+1;
    for(i = 0;i<step;++i){
        fprintf(fp,"%f	%f\n",t,x);
        t += dt;
        x = euler(x,t);
    }

	fclose(fp);
	return 0;

}

