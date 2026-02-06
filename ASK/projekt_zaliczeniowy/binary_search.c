#include <stdio.h>

int binary_search(int* tab, int size, int target)
{
    int left = 0;
    int right = size;
	int mid;
	while(left <= right)
	{
		mid = (left + right) / 2;

		if(tab[mid] == target)
        {
			return mid;
        }

		if(tab[mid] > target)
        {
			right = mid - 1;
        }
		else
        {
			left = mid + 1;
        }
    }

	return -1;
}


int main(void)
{
    int tab[] = { 1, 2, 3, 4, 5, 6, 7};
    int target = 6;
    int index = binary_search(tab, sizeof(tab)/sizeof(tab[0]), target);
    printf("%d\n", index);
    return 0;
}