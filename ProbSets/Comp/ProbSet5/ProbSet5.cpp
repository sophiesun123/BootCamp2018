// PROBLEM SET 5

// EXERCISE 1
// makefile: 
// all: normalize_vec.exec 
// normalize_vec.exec: normalize_vec.cpp
// 	g++ normalize_vec.cpp -fopenmp -o normalize_vec.exec	
// clean:
// 	rm -f *.exec

// parallel code is in normalize_vec.cpp

// EXERCISE 2
#include <iostream>
#include <vector>
#include <omp.h>

int main(void){
    const int N = 100000000;
    std::vector<double> a(N);
    std::vector<double> b(N);

    int num_threads = omp_get_max_threads();
    std::cout << "dot of vectors with length " << N  << " with " << num_threads << " threads" << std::endl;

    // initialize the vectors
    for(int i=0; i<N; i++) {
        a[i] = 1./2.;
        b[i] = double(i+1);
    }

    double time = -omp_get_wtime();
    double dot=0.;
	#pragma omp parallel for reduction(+:dot)
    for(int i=0; i<N; i++) {
        dot += a[i] * b[i];
    }
    time += omp_get_wtime();

    // use formula for sum of arithmetic sequence: sum(1:n) = (n+1)*n/2
    double expected = double(N+1)*double(N)/4.;
    std::cout << "dot product " << dot
              << (dot==expected ? " which matches the expected value "
                                : " which does not match the expected value ")
              << expected << std::endl;
    std::cout << "that took " << time << " seconds" << std::endl;
    return 0;
}

// EXERCISE 3 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
 
int main()
{
    const int iter = 10000;
    double x, y, pi;
    int count = 0;
    int threadID;
 
    //main loop
    #pragma omp parallel private(x, y, z, threadID)
    {
      threadID = omp_get_thread_num();
      srand(threadID);
    #pragma omp for reduction(+:count)
    for (int i = 0; i < iter; i++) 
	{   
        x = (double)random() / RAND_MAX;
        y = (double)random() / RAND_MAX;
        if (sqrt((x * x) + (y * y)) <= 1)
        {
            count++;
        }
    }
    }
    printf(((double)count/(double)niter)*4.0);
    return 0;
}