all : problems.txt solutions.txt

problems.txt :
	./sight.py --fixed-seed --no-solutions > problems.txt

solutions.txt :
	./sight.py --fixed-seed > solutions.txt
