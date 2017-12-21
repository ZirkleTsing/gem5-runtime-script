#!/usr/bin/python

#
# A Python script to run all benchmarks.
#
# Copyright (C) Min Cai 2015
# Modified Xiaoting Hao 2016
#

import os


def run(cpu,cpubench, cpuoption, gpubench, l2_size, l2_assoc, num_threads):
    dir = 'results_1C1G_streamcluster/'  + str(cpu) + '/' +str(l2_size) + '/'  + str(l2_assoc)

    os.system('rm -fr ' + dir)
    os.system('mkdir -p ' + dir)

    cmd_run = 'build/X86_MESI_Two_Level_GPU/gem5.opt -d ' + dir + ' ../gem5-gpu/configs/se_fusion01.py --num-cpus=' \
              + str(num_threads) + ' --cmd=/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/' \
              +cpubench \
              + ' --options=' \
              + '"'+cpuoption +'"' \
              + ' --caches --l2cache --num-l2caches=1 --cpu-clock=3GHz  --cpu-type=detailed -I 100000000 --clusters=4 ' \
              + ' --l1d_size=32kB --l1i_size=32kB --l2_size=' + l2_size + ' --l2_assoc=' + str(l2_assoc) \
              + ' --gpu-benchmark=' + gpubench \
              + ' --gpu-option="2 5 4 512 512 10 none output.txt 1"' \
              + ' --gpu-stdout='+ dir+'/stdout.txt  --gpu-errout='+ dir+'/errout.txt'
             
    print cmd_run

    f=file("cmd.txt","w+")
    f.writelines(cmd_run)
    f.close()

    os.system('vim ' +dir+ '/cmd.txt')
    os.system('cp -r ./cmd.txt' + ' ' + dir +'/cmd.txt')
    os.system('rm -r cmd.txt')


    os.system(cmd_run)


def run_experiments(cpu,cpubench,cpuoption,gpubench):

     run(cpu,cpubench, cpuoption, gpubench, '256kB', 4, 2)


run_experiments('400','400.perlbench/exe/perlbench_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/400.perlbench/data/test/input/makerand.pl','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('401','401.bzip2/run/run_base_ref_amd64-m64-gcc42-nn.0000/bzip2_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/401.bzip2/run/run_base_ref_amd64-m64-gcc42-nn.0000/input.source  280','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('403','403.gcc/run/run_base_ref_amd64-m64-gcc42-nn.0000/gcc_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/403.gcc/run/run_base_ref_amd64-m64-gcc42-nn.0000/166.i','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('429','429.mcf/run/run_base_ref_amd64-m64-gcc42-nn.0000/mcf_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/429.mcf/run/run_base_ref_amd64-m64-gcc42-nn.0000/inp.in','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('435','435.gromacs/run/run_base_ref_amd64-m64-gcc42-nn.0000/gromacs_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/435.gromacs/run/run_base_ref_amd64-m64-gcc42-nn.0000/gromacs.tpr  -nice  0','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('436','436.cactusADM/run/run_base_ref_amd64-m64-gcc42-nn.0000/cactusADM_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/436.cactusADM/run/run_base_ref_amd64-m64-gcc42-nn.0000/benchADM.par','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('444','444.namd/run/run_base_ref_amd64-m64-gcc42-nn.0000/namd_base.amd64-m64-gcc42-nn','--input /home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/444.namd/run/run_base_ref_amd64-m64-gcc42-nn.0000/namd.input  --iterations 38  --output /home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/444.namd/run/run_base_ref_amd64-m64-gcc42-nn.0000/namd.out','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('450','450.soplex/run/run_base_ref_amd64-m64-gcc42-nn.0000/soplex_base.amd64-m64-gcc42-nn','-s1 -e -m45000 /home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/450.soplex/run/run_base_ref_amd64-m64-gcc42-nn.0000/pds-50.mps','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('454','454.calculix/run/run_base_ref_amd64-m64-gcc42-nn.0000/calculix_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/454.calculix/run/run_base_ref_amd64-m64-gcc42-nn.0000/hyperviscoplastic','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('456','456.hmmer/run/run_base_ref_amd64-m64-gcc42-nn.0000/hmmer_base.amd64-m64-gcc42-nn','--fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 /home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/456.hmmer/run/run_base_ref_amd64-m64-gcc42-nn.0000/retro.hmm','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('458','458.sjeng/run/run_base_ref_amd64-m64-gcc42-nn.0000/sjeng_base.amd64-m64-gcc42-nn','/home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/458.sjeng/run/run_base_ref_amd64-m64-gcc42-nn.0000/ref.txt','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('462','462.libquantum/run/run_base_ref_amd64-m64-gcc42-nn.0000/libquantum_base.amd64-m64-gcc42-nn','1397  8','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')
run_experiments('470','470.lbm/run/run_base_ref_amd64-m64-gcc42-nn.0000/lbm_base.amd64-m64-gcc42-nn','3000  reference.dat  0  0 /home/hao/SPEC2006/cpu2006_static_complier/benchspec/CPU2006/470.lbm/run/run_base_ref_amd64-m64-gcc42-nn.0000/100_100_130_ldc.of','../benchmarks/rodinia/streamcluster/gem5_fusion_streamcluster')

