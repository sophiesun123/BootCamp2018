#######################################################################	

all: 	normalize_vec.exec \
	dot_prod.exec

#######################################################################	

normalize_vec.exec: normalize_vec.cpp
	g++ normalize_vec.cpp -fopenmp -o normalize_vec.exec	

dot_prod.exec: dot_prod.cpp
	g++ dot_prod.cpp -fopenmp -o dot_prod.exec
	

#######################################################################	
	
clean :
	rm -f *.exec