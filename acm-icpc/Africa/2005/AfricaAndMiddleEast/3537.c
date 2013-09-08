#include <stdio.h>
#include <stdlib.h>

static int matrix[10][10];
static int n;
static int cases;
static int i;
static int j, k;

int process() {
	int diff;
	for (j = 1; j < n; j++) {
		diff = matrix[0][0] - matrix[j][0];
		for (k = 1; k < n; k++) {
			if (matrix[0][k] - matrix[j][k] != diff)
				return 0;
		}
	}
	return 1;		
	
}
	

int main(int argc, char** argv)
{
	scanf("%d", &cases);
	for (i = 1; i <= cases; i++) {
		scanf("%d", &n);
		for (j = 0; j < n; j++) {
			for (k = 0; k < n; k++)
				scanf("%d", &matrix[j][k]);
		}
		if (process()) {
			printf("%d. YES\n", i);
		}
		else {
			printf("%d. NO\n", i);
		}
	}
		
	return 0;
}
