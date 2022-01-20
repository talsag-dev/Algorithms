#include <iostream>
#include <bits/stdc++.h>
using namespace std;


bool hasRepeatedSubstring(string str)
{
    int i = 1, j = 0, n = str.size();
    
    /* dp[i+1] stores longest proper prefix 
    upto index i which also a suffix */ 
    vector <int> dp(n+1,0);
    
    /* Traverse the string */
    while(i < n)
    {
        /* if the current character (at index = i) is same as the last 
        character of longest common prefix obtained upto index i-1 */
        if(str[i] == str[j]) 
        dp[++i] = ++j;
        
        /* if characters don't match */
        else 
        {   
            /* when str[0] and str[i] don't match no proper 
            prefix which is also a suffix is possible 
            so length is 0, simply move on to next character*/
            if(j == 0) 
            i++;
            
            /* decrease the length (by 1) of longest proper 
            prefix (also suffix) possible upto index i-1 
            and then match the last character of longest 
            proper prefix to character at current index */ 
            else 
            j = dp[j];
        }
    }
    
    /* check if there is any such prefix of 
    input string that has length that 
    completely divides the input string length */
    return dp[n] && (dp[n]%(n-dp[n]) == 0);
}
int main()
{   
    /* input string */
    string str = "abcabcabc";
    
    if(hasRepeatedSubstring(str))
    cout<<"Formed by repeating substring";
    else
    cout<<"Cannot be formed by repeated substring";
    
    return 0;
}