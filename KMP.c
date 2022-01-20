/*
	C program for implementation of KMP pattern searching algorithm

	Base Solution taken from GeeksForGeeks.
	Color addon by Shimon Aviram.
*/

#ifdef _WIN32 
	#include <windows.h>
	#ifndef ENABLE_VIRTUAL_TERMINAL_PROCESSING
		#define ENABLE_VIRTUAL_TERMINAL_PROCESSING 0x0004
	#endif
#endif

#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define TAB			50
#define RED			printf("\033[0;31m")
#define GREEN		printf("\033[0;32m")
#define CYAN		printf("\033[0;36m")
#define WHITE		printf("\033[0m")
#define SPACE(N)	for (int x = 0; x < (N); x++) printf(" ")

int EnableColor()
{
	//Enabling ANSI colors in older versions of Windows
	#ifdef _WIN32
		DWORD dwMode;
		HANDLE hInput = GetStdHandle(STD_INPUT_HANDLE), hOutput = GetStdHandle(STD_OUTPUT_HANDLE);
		GetConsoleMode(hOutput, &dwMode);
		dwMode |= ENABLE_PROCESSED_OUTPUT | ENABLE_VIRTUAL_TERMINAL_PROCESSING;
		if (!SetConsoleMode(hOutput, dwMode))
			return 0;
	#endif
	return 1;
}

void print_char(char c)
{
	GREEN;
	printf("%c", c);
	WHITE;
}

void print_suffix(char* str)
{
	RED;
	printf("%s\n", str);
	WHITE;
}

void print_prefix(char* str, int len)
{
	CYAN;
	for (int i = 0; i < len; i++) printf("%c", str[i]);
	WHITE;
}

// Fills lps[] for given patttern pat[0..M-1] 
int* computeLPSArray(char* pat, int M)
{
	int* lps = (int*)malloc(sizeof(int) * M);
	assert(lps != NULL);

	// length of the previous longest prefix suffix 
	int len = 0;

	lps[0] = 0; // lps[0] is always 0 

	// the loop calculates lps[i] for i = 1 to M-1 
	int i = 1;
	while (i < M) {
		if (pat[i] == pat[len]) {
			len++;
			lps[i] = len;
			i++;
		}
		else // (pat[i] != pat[len]) 
		{
			// This is tricky. Consider the example. 
			// AAACAAAA and i = 7. The idea is similar 
			// to search step. 
			if (len != 0) {
				len = lps[len - 1];

				// Also, note that we do not increment 
				// i here 
			}
			else // if (len == 0) 
			{
				lps[i] = 0;
				i++;
			}
		}
	}

	printf("LPS Array:\n");
	printf("----------\n");
	puts(pat);
	for (i = 0; i < M; i++)
		printf("%d", lps[i]);
	printf("\n\n");

	return lps;
}

// Prints occurrences of txt[] in pat[] 
void KMPSearch(char* pat, char* txt)
{
	int flag = 0;
	int i = 0; // index for txt[]
	int j = 0; // index for pat[] 

	int M = strlen(pat);
	int N = strlen(txt);

	// calculate lps[] array
	// that will hold the longest prefix suffix 
	// values for pattern  
	int* lps = computeLPSArray(pat, M);

	printf("KMP Search\n");
	printf("----------\n");

	puts(txt);

	while (i < N)
	{
		if (pat[j] == txt[i])
		{
			print_char(pat[j]);
			j++;
			i++;

			if (j == M)
			{
				flag = 1;
				SPACE(TAB - i - j);
				printf("Found pattern at index %d\n", i - j);
				j = lps[j - 1];
			}
		}
		else //mismatch after j matches
		{
			// Do not match lps[0..lps[j-1]] characters, 
			// they will match anyway 
			flag = 1;
			print_suffix(pat + j);
			if (j != 0)
				j = lps[j - 1];
			else
				i = i + 1;
		}

		if (flag == 1)
		{
			flag = 0;
			puts(txt);
			SPACE(i - j);
			print_prefix(pat, j);
		}
	}

	print_suffix(pat + j);
	free(lps);
}

// Driver program to test above function 
int main()
{
	char txt[] = "ABBABBABBABB";
	char pat[] = "A";

	EnableColor();
	KMPSearch(pat, txt);

	system("pause");
}