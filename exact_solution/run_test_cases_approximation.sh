#!/bin/sh

printf "" > output.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "13 Vertex Approximation: test ${i}\n------------------------\n" >> output.txt
  cat exact_solution/test_cases/13_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output.txt
  printf "\n13 Vertex Lower Bound:\n" >> output.txt
  cat exact_solution/test_cases/13_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output.txt
  printf "\n\n\n" >> output.txt
done

printf "\n\n" >> output.txt


for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "30 Vertex Approximation: test ${i}\n------------------------\n" >> output.txt
  cat exact_solution/test_cases/30_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output.txt
  printf "\n30 Vertex Lower Bound:\n" >> output.txt
  cat exact_solution/test_cases/30_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output.txt
  printf "\n\n\n" >> output.txt
done

printf "\n\n" >> output.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "3 Vertex Approximation: test ${i}\n------------------------\n" >> output.txt
  cat exact_solution/test_cases/provided_1.txt | python approximation_solution/travelling_sales_approx.py >> output.txt
  printf "\n3 Vertex Lower Bound:\n" >> output.txt
  cat exact_solution/test_cases/provided_1.txt | python approximation_solution/tsp_lowerbound.py >> output.txt
  printf "\n\n\n" >> output.txt
done


printf "\n\n" >> output.txt


for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "4 Vertex Approximation: test ${i}\n------------------------\n" >> output.txt
  cat exact_solution/test_cases/provided_2.txt | python approximation_solution/travelling_sales_approx.py >> output.txt
  printf "\n4 Vertex Lower Bound:\n" >> output.txt
  cat exact_solution/test_cases/provided_2.txt | python approximation_solution/tsp_lowerbound.py >> output.txt
  printf "\n\n\n" >> output.txt
done

printf "\n\n" >> output.txt

printf "1060 Vertex Approximation:\n" >> output.txt
cat exact_solution/test_cases/u1060_tsp_t0.txt | python approximation_solution/travelling_sales_approx.py >> output.txt
printf "\n1060 Vertex Lower Bound:\n" >> output.txt
cat exact_solution/test_cases/u1060_tsp_t0.txt | python approximation_solution/tsp_lowerbound.py >> output.txt