#include <iostream>
using namespace std;
void factorial()

 {  int a;
    int count=1;
    cin>>a;
   for(int i=a;i!=0;i--)
   {
       count=count*i;
   }
   cout<<count; 
 }
int main()
{
    factorial();
    return 0;       
}

