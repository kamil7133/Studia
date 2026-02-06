#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_LENGTH 10000

long long int abs_sum(long long int *data, int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        int val = data[i];
        if (val < 0)
        {
            sum -= val;
        }
        else
        {
            sum += val;
        }
    }
    return sum;
}

int main(int argc, char *argv[])
{
    srand(time(NULL));
    long long int *data = malloc(sizeof(long long int) * ARRAY_LENGTH);
    for (int i = 0; i < ARRAY_LENGTH; i++)
    {
        data[i] = rand() % 100;

        int negative = 0;
        // negative = rand() % 2;
        // if (negative)
        // {
        //     data[i] = -data[i];
        // }
    }

    struct timespec start;
    timespec_get(&start, TIME_UTC);

    int ret = abs_sum(data, ARRAY_LENGTH);

    struct timespec end;
    timespec_get(&end, TIME_UTC);

    double elapsed =
        (end.tv_sec - start.tv_sec) + ((end.tv_nsec - start.tv_nsec) * 1e-9);

    printf("Result %d\n", ret);
    printf("Time elapsed: %f\n", elapsed);

    free(data);
}
