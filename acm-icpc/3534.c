#include <stdlib.h>
#include <stdio.h>

#define MAX_VAL 999999

static int ar[10001];
static int ab[10001];

void process() {
	int i_ar = 0, i_ab = 0;
	int sum_ar = 0, sum_ab = 0;
	int res = 0;
	
	while ((!(ar[i_ar] == MAX_VAL) || !(ab[i_ab] == MAX_VAL))) {
		if (ar[i_ar] == ab[i_ab]) {
			res += ((sum_ar > sum_ab ? sum_ar : sum_ab) + ar[i_ar]);
			sum_ar = sum_ab = 0;
			i_ar++;
			i_ab++;
		}
		else if (ar[i_ar] < ab[i_ab]) {
			sum_ar += ar[i_ar++];
		}
		else {
			sum_ab += ab[i_ab++];
		}
	}
	res += (sum_ar > sum_ab ? sum_ar : sum_ab);
	printf("%d\n", res);
}

int main(int argc, char** argv)
{
	int aux;
	scanf("%d", &aux);
	while (aux != 0) {
		int i = 0;
		for (; i < aux; i++)
			scanf("%d", &ar[i]);
		ar[i] = MAX_VAL;
		scanf("%d", &aux);
		for (i = 0; i < aux; i++)
			scanf("%d", &ab[i]);
		ab[i] = MAX_VAL;
		process();
		scanf("%d", &aux);
	}
	return 0;
}
