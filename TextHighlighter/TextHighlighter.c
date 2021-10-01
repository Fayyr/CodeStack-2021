#include <stdio.h>
#include <string.h>
 
void main()
{
    int i,l,arr[100],max,h[26];
    char word[10];
    
    for(i=0;i<26;i++)
               scanf("%d",&h[i]);
    
    scanf("%s", word);
    
    l=strlen(word);
    
    for(i=0;i<l;i++)
               arr[i]= 25 - (word[i]-97);
    
    max=h[arr[0]];
    
    for(i=0;i<l;i++)
               if(h[arr[i]]>max)
                              max=h[arr[i]];
    
    printf("%d",max*l);
}
