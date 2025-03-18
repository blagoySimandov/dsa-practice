.PHONY: setup test test1 test2 q3 q4 q5 q6 all_evaluations clean

setup:
	pip install -r requirements.txt

test: test1 test2

test1:
	python3 dijkstra_implementation_tests/test_dijkstra_simplegraph1.py

test2:
	python3 dijkstra_implementation_tests/test_dijkstra_simplegraph2.py

q3:
	python3 -c "from main import run_q3; run_q3()" #muhaha hack

q4:
	python3 -c "from main import run_q4; run_q4()"

q5:
	python3 -c "from main import run_q5; run_q5()"

q6:
	python3 -c "from main import run_q6; run_q6()"

all_evaluations: q3 q4 q5 q6

clean:
	rm -f *.png
