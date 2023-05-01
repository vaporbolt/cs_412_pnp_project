#!/bin/sh

printf "" > output.txt

printf "4 Vertex Exact:\n" >> output.txt
cat test_cases/provided_2.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt

printf "3 Vertex Exact:\n" >> output.txt
cat test_cases/provided_1.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt

printf "10 Vertex Exact:\n" >> output.txt
cat test_cases/10_vertex.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt

printf "11 Vertex Exact:\n" >> output.txt
cat test_cases/11_vertex.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt

printf "12 Vertex Exact:\n" >> output.txt
cat test_cases/12_vertex.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt

printf "13 Vertex Exact:\n" >> output.txt
cat test_cases/13_vertex.txt | python travelling_sales_exact.py >> output.txt
printf "\n\n" >> output.txt
