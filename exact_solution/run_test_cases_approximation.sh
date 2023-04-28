#!/bin/sh

printf "" > output_approx.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "10 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/10_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n10 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/10_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

printf "\n\n" >> output_approx.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "11 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/11_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n11 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/11_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "12 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/12_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n12 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/12_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

printf "\n\n" >> output_approx.txt

printf "\n\n" >> output_approx.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "13 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/13_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n13 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/13_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

printf "\n\n" >> output_approx.txt



for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "30 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/30_vertex.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n30 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/30_vertex.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

printf "\n\n" >> output_approx.txt

for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "3 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/provided_1.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n3 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/provided_1.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done


printf "\n\n" >> output_approx.txt


for i in 1 2 3 4 5 6 7 8 9 10
do
  printf "4 Vertex Approximation: test ${i}\n------------------------\n" >> output_approx.txt
  cat exact_solution/test_cases/provided_2.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
  printf "\n4 Vertex Lower Bound:\n" >> output_approx.txt
  cat exact_solution/test_cases/provided_2.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt
  printf "\n\n\n" >> output_approx.txt
done

#printf "\n\n" >> output_approx.txt

#printf "1060 Vertex Approximation:\n" >> output_approx.txt
#cat exact_solution/test_cases/u1060_tsp_t0.txt | python approximation_solution/travelling_sales_approx.py >> output_approx.txt
#printf "\n1060 Vertex Lower Bound:\n" >> output_approx.txt
#cat exact_solution/test_cases/u1060_tsp_t0.txt | python approximation_solution/tsp_lowerbound.py >> output_approx.txt