# Where these files go

On the first execution of **vagrant up**, the Vagrant **bootstrap.sh** script copies my.minimal.conf to /etc/apache2/sites-available in the VM. The content of **hosts** is appended to the existing host file.