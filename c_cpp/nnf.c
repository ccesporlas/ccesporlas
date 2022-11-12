/***** Neural Network *****/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

# define N 10

void learn();
int s[N],s_in,mag,hits;
double j[N],h,games=0,qsum,kappa=1.,number;
int ch;

main(argc,argv)
int argc;
char *argv[];
{
   int i,file,garbage;
   FILE *fpr;

   if (argc<2) {printf("No argument given!\n");return;}
   for (file=1;file<argc;file++)
   {
      fpr=fopen(argv[file],"r");
      if (fpr==0L) {printf("Unable to open file!\n");return;}

      for (i=0;i<N;i++) s[i]=1; 
      for (i=0;i<N;i++) j[i]=1./N;
      hits=0;games=0;mag=0,garbage=0; 

      while((ch=getc(fpr))!=EOF)  if(ch=='1' || ch =='0')
	                                              {games ++;
                                                        if(ch=='1') mag++;}
      number=games; games=0;
      rewind(fpr);          

      while((ch=getc(fpr))!=EOF)
      {
	   switch (ch)
	   {
	      case '1': s_in=1;learn();break;
	      case '0': s_in=-1;learn();break; 
	      default: garbage++;
	   }
      }
      printf("File %s: hit percentage %6.2lf%%, %d characters, P(1)=%4.2lf, %d ignored\n"
                 ,argv[file],2.*hits/games*100,(int)games,mag/games,garbage);
   }
}

void learn()
{
  int i;
  h=0.; 
  games++;
/*   Calculate the field:  */
  for(i=0;i<N;i++)   h+=j[i]*s[i];
/*  Prediction: */
  if(games>number/2. && h*s_in>0 ) hits++; 
  qsum=0.;  
  for (i=0;i<N;i++) qsum+=j[i]*j[i]; 
  qsum=sqrt(qsum);
/* Learn: */
     if(h*s_in<=kappa*qsum)
         for (i=0;i<N;i++) j[i]+=s_in*s[i]/(double) N; 
/* Shift : */  
  for(i=N-1;i>0;i--) s[i]=s[i-1]; 
  s[0]=s_in;
}
