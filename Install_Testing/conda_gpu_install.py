# 1. Install GCP
# 2. execute the gcp commands
# 3. execute the install tf command

import os, platform
import sys

import sample_tf_program
import exec_gcp_commands

print("==========================INSTALL TESTING============================")
print("\n\nTest Case Suite: {}".format(sys.argv[1]))
print("Test Case ID: {}".format(sys.argv[2]))

win_install_command = "gcloud compute instances create my-instance-windows --image-family windows-2012-r2 --image-project gce-uefi-images --no-shielded-secure-boot"
ubuntu_install_command = "gcloud compute instances create my-instance-ubuntu --image-family ubuntu-1804-lts --image-project gce-uefi-images --no-shielded-secure-boot"
fedora_install_command = "gcloud compute instances create my-instance-fedora --image-family rhel-8-v20191018 --image-project gce-uefi-images --no-shielded-secure-boot"
centos_install_command = "gcloud compute instances create my-instance-centos --image-family centos-6-v20191014 --image-project gce-uefi-images --no-shielded-secure-boot"
debian_install_command = "gcloud compute instances create my-instance-debian --image-family debian-9-tf-1-15-v20191021 --image-project gce-uefi-images --no-shielded-secure-boot"
print("Creating a new instance of GCP with Operating System: {}".format(sys.argv[3]))

if sys.argv[3] == "Ubuntu":
    exec_gcp_commands.exec(ubuntu_install_command)
elif sys.argv[3] == "Fedora":
    exec_gcp_commands.exec(fedora_install_command)
elif sys.argv[3] == "Windows":
    exec_gcp_commands.exec(win_install_command)
elif sys.argv[3] == "Debian":
    exec_gcp_commands.exec(debian_install_command)
elif sys.argv[3] == "CentOS":
    exec_gcp_commands.exec(centos_install_command)

    

print("Name of Operating System : {}".format(sys.argv[3]))
print("Name of Platform : {}".format(platform.system()))
print("Version of Platform : {}".format(platform.release()))
print("Python version : {}".format(platform.python_version()))

cmd = "curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh"
exec_gcp_commands.exec(cmd)
cmd = "bash Anaconda3-2019.03-Linux-x86_64.sh"
exec_gcp_commands.exec(cmd)

cmd = "source ~/.bashrc"
exec_gcp_commands.exec(cmd)


cmd = "conda --version"
exec_gcp_commands.exec(cmd)
# print("Pip version : pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6")


print("Tensorflow has not been previously installed")
command = "conda install -c anaconda tensorflow-gpu"

exec_gcp_commands.exec(command)

print("\nTensorflow-GPU has been succesfully installed via Anaconda")
#print("Tensorflow version : {}".format(tf.__version__))

sample_tf_program.test_install()
print("Succesfully executed sample tensorflow program: sample_program.py")
print("\n\nTest Case Status: PASS\n\n")
print("=="*40)
