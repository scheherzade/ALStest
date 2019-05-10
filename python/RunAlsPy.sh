#!/bin/bash

echo "This script is used to run als_csv_python example"
results_dir="/home/sshirzad/workspace/als/python/results"

iteration_array=(1)
row_stop_array=(700)
num_factors_array=(40)
col_stop_array=(1000 10000 20000)
thr=(1 2 4 8 16)

if [ ${results_dir} != '' ]
then
rm -rf ${results_dir}/*

mkdir ${results_dir}/info

for it in "${iteration_array[@]}"
do
for f in "${num_factors_array[@]}"
    do
    for rs in "${row_stop_array[@]}"
	do
    	for cs in "${col_stop_array[@]}"
	do
	   for th in "${thr[@]}"
	    do
		export OMP_NUM_THREADS=${th}   
		export OMP_PLACES=cores
	    	python3 ./als_csv_python.py $rs $cs $f $it 0.1 40.0 >> ${results_dir}/alspy_${th}th_itrscs_${it}_${f}_${rs}_${cs}
		echo "done ${th}_${it}_${f}_${rs}_${cs}"	
	    done
	done
    done
done
done
fi
