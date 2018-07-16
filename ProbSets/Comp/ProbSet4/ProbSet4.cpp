// PROBLEM SET 4

// EXERCISE 1
/*
S(p, N) = 1 / (f + (1 - f) / p)
S(100, N) = 1 / (0.04 + (1 - 0.04) / 100) = 2.5
*/

// EXERCISE 2
// #include <iostream>
// using namespace std;
// int main()
// {
// 	string name;
// 	cout << "Enter name: ";
// 	cin >> name;
// 	cout << "Hello, " << name << " from Sophie!" << endl;
// 	return 0;
// }

// EXERCISE 3 WHY DOESN'T THIS WORK AS;DOIJAO;EIJFAO;WJEF;AOWJEFO;AJWEO;FJAO;WEJFO;AJWEF
#include <iostream>
#include <math.h>
using namespace std;
// function that returns the solution to the quadratic equation
pair<double, double> sol(double a, double b, double c)
{
	double pos = (-b + sqrt(b * b - 4 * a * c)) / (2 * a);
	double neg = (-b - sqrt(b * b - 4 * a * c)) / (2 * a);
	return make_pair<double, double>(pos, neg);
}
int main()
{
	double a, b, c;
	cout << "Enter a value for a: ";
	cin >> a;
	cout << "Enter a value for b: ";
	cin >> b;
	cout << "Enter a value for c: ";
	cin >> c;
	pair<double,double> solution = sol(a, b, c);
	cout << "The solutions to the quadratic equation are " << solution.first << " and " << solution.second << endl;
	return 0;
}

// EXERCISE 4
// #include <iostream>
// using namespace std;
// static long num_steps = 1000000; double step;
// int main()
// {
// 	int i;
// 	double x, pi, sum = 0.0;
// 	step = 1.0 / (double) num_steps;
// 	for (i = 0; i < num_steps; i++)
// 	{
// 		x = (i + 0.5) * step;
// 		sum = sum + 4.0 / (1.0 + x * x);
// 	}
// 	pi = step * sum;
// 	cout << pi << endl;
// 	return 0;
// }

// EXERCISE 5
// #include <iostream>
// #include <random>
// using namespace std;
// // function that determines whether or not the dart lands in the circle
// bool circ(double x, double y)
// {
// 	double incirc;
// 	incirc = x * x + y * y;
// 	return incirc <= 1;
// }
// int main()
// {
// 	// create random generator
// 	unsigned seed = 3;
// 	default_random_engine randnum(seed);
// 	uniform_real_distribution<double> distr(0.0, 1.0);

// 	// random numbers
// 	double x, y;
// 	// number of darts in circle and total number of darts thrown
// 	int in = 0;
// 	int tot = 10000;
// 	// create experiment
// 	for (int i = 1; i < tot; i++)
// 	{
// 		x = distr(randnum);
// 		y = distr(randnum);
// 		if (circ(x, y))
// 		{
// 			in += 1;
// 		}
// 	}
// 	// estimate Pi according to the Monte Carlo method
// 	double pi = 4. * in / tot;
// 	cout << pi << endl;
// 	return 0;
// }