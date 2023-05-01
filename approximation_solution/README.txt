THIS IS THE README FOR THE APPROXIMATION SOLUTION

Running run_test_cases_approximation.sh will run all available test cases, stored in the test_cases folder in the
exact solution directory. It will run each test case 10 times (excluding the provided
1060 vertex test case which only runs once), outputting results to the file named output_approx.txt. For our testing,
we used git bash to run this since we are both on windows and running shell scripts can be a pain on Windows. The script
also runs the lower bound program (located in this directory) and outputs the results of both lower bounds on
each run to compare the approximation result to.
**Timing code is commented out, to enable it uncomment the final print statement in main of cs412_tsp_approx.py

In bash, navigating to the approximation_solution directory and running $sh run_test_cases_approximation.sh
will run the test cases and output the results to a text file called output_approx.
