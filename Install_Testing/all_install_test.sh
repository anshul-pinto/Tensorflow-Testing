test_case_id=1

for os in Ubuntu CentOS Fedora Debian Windows 
do
    echo $os
    python3 pip_cpu_install.py 1 $test_case_id $os
    ((test_case_id=test_case_id+1))

    python3 pip_gpu_install.py 1 $test_case_id $os
    ((test_case_id=test_case_id+1))

    python3 conda_cpu_install.py 1 $test_case_id $os
    ((test_case_id=test_case_id+1))

    python3 conda_gpu_install.py 1 $test_case_id $os
    ((test_case_id=test_case_id+1))
done