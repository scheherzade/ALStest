#!/bin/bash

echo "This script is used to run als_csv_phylanx example"
module purge
module load gcc/8.2.0
module load boost/1.68.0-gcc8.2.0-release
module load cmake/3.9.0
module load pybind11/2.2.4
module load gperftools/2.7

phylanx_dir="/home/sshirzad/src/phylanx/build_release_gcc_no_hpxmp"
results_dir="/home/sshirzad/workspace/als/hpxmp-off-blas-indirect/results"
phylanx_log_file="/home/sshirzad/src/phylanx/build_release_gcc_no_hpxmp/phylanx_cmake_log.txt"

iteration_array=(1)
row_stop_array=(700)
num_factors_array=(40)
col_stop_array=(1000 10000 20000)
thr=(1 2 4 8 10 12 16) 

if [ ${results_dir} != '' ]
then
rm -rf ${results_dir}/*

mkdir ${results_dir}/info
date>> ${results_dir}/info/date.txt
cp ${phylanx_log_file} ${results_dir}/info/date.txt

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
		export OMP_NUM_THREADS=1
   	${phylanx_dir}/bin/als_csv_instrumented --hpx:threads=${th} --data_csv=/phylanx-data/CSV/MovieLens_20m.csv  --hpx:bind=balanced --hpx:numa-sensitive --iterations=${it} --f=${f} --row_stop=${rs} --col_stop=${cs} --hpx:print-counter=/threads{locality#*/total}/idle-rate >> ${results_dir}/alsphx_${th}th_itrscs_${it}_${f}_${rs}_${cs}
		echo "done ${th}_${it}_${f}_${rs}_${cs}_${th}"	
	    done
	done
    done
done
done

else
echo "errorrrrrrrrrrrrrr"
fi
