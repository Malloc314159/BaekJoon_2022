#include <bits/stdc++.h>

using namespace std;

int main()
{
   int n,k,cnt=0;
   long long int a[300005],l;
   
   scanf("%lld %d %d",&l,&n,&k);
   
   a[0]=0; a[n+1]=l;
   for(int i=1;i<=n;i++)
   {
      scanf("%lld",&a[i]);
   }
   while(k>0)
   {
      if(cnt==0)
      {
         for(int i=0;i<n;i++)
         {
            printf("0\n");
            k--;
            if(k==0) break;
         }
         if(k==0) break;
      }
      else
      {
         for(int i=1;i<=n;i++)
         {
            if(a[i]-cnt>=0 && a[i]-cnt>a[i-1]+cnt)
            {
               printf("%d\n",cnt);
               k--;
               if(k==0) break;
            }
            if(a[i]+cnt<=l && a[i]+cnt<a[i+1]-cnt)
            {
               printf("%d\n",cnt);
               k--;
               if(k==0) break;
            }
            if(a[i]+cnt<l && a[i]+cnt==a[i+1]-cnt)
            {
               printf("%d\n",cnt);
               k--;
               if(k==0) break;
            }
         }
      }
      cnt++;
   }
   
   return 0;
}
    