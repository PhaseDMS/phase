#!/bin/bash

set -e

echo "Project name?"
while [ -z ${project_name} ]; do
    read project_name
done

echo "LXC container name?"
while [ -z ${container_name} ]; do
    read container_name
done

echo "Local code repository?"
read repository_path
while [ ! -d ${repository_path} ]; do
    read repository_path
done

echo "Remote path for code repository mounting?"
read remote_path
while [ -z ${remote_path} ]; do
    read remote_path
done

echo "Select public ssh key"
echo ""
if [ $(ls -al ~/.ssh/ | grep -n .pub | wc -l) = "0" ]
then
    echo "No public ssh key found"
    echo "Use `ssh-keygen` and start over"
    exit
else
    echo ""
    ls -a ~/.ssh | grep .pub
    echo ""
    read ssh_key
    while [ ! -e "$HOME/.ssh/${ssh_key}" ]; do
        echo ""
        ls -a ~/.ssh | grep .pub
        echo ""
        read ssh_key
    done
fi

echo "Creating lxc container"
sudo lxc launch images:debian/buster $container_name -c security.privileged=true
echo ""

echo "Waiting for container to start"
echo ""
for i in {0..15}; do echo -ne "$i"'\r'; sleep 1; done; echo
echo ""

echo "apt Update / upgrade"
echo ""
sudo lxc exec $container_name -- sh -c "apt -y update"
sudo lxc exec $container_name -- sh -c "apt -y upgrade"
echo ""

echo "Installing ssh on container"
echo ""
sudo lxc exec $container_name -- sh -c "echo "y\n" | apt install ssh"
echo ""

echo "Sending public key to container"
echo ""
ip=$(lxc list $container_name -c 4 | awk '!/IPV4/{ if ( $2 != "" && $2 != "|" ) print $2}')
echo "Container ip is ${ip}"
ssh-keyscan -H $ip >> ~/.ssh/known_hosts
sudo lxc exec $container_name -- sh -c "mkdir /root/.ssh"
sudo lxc file push $HOME/.ssh/$ssh_key $container_name/root/.ssh/authorized_keys --uid=0 --gid=0
echo ""

echo "Mounting local repository to container"
echo ""
sudo lxc config device add $container_name $project_name disk source=$repository_path path=$remote_path
echo ""

echo "Installing python"
echo ""
sudo lxc exec $container_name -- sh -c "apt -y install python"
echo ""

echo "Container creation: done!"
echo ""


echo "There still is some work to be done."

echo "Add this in your '/etc/hosts' file:"
echo -e "\t$ip ${project_name}.local"
echo ""

echo "Setup your ssh config (in '~/.ssh/config')"
echo ""
echo "# The local instance on a LXC virtual machine and a public ip"
echo "Host ${project_name}.local"
echo -e "\tUser root"
echo -e "\tPort 22"
echo -e "\tHostName ${project_name}.local"
echo -e "\tForwardAgent yes"
echo ""
