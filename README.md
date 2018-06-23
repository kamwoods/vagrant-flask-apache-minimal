# Automatically deploy a simple Flask "Hello World" app in a VM using Vagrant. Serves content via Apache and mod_wsgi.

Minimal example for new users getting started with Vagrant, Flask, Apache, and mod_wsgi. To **keep** things simple, the Vagrant bootstrap is a single bash script (no Salt or Ansible here), the Flask app is a simple "Hello World", and it is **only** tested with the **bento/Ubuntu-18.04** base box.

See a problem, or something that could be improved? Submit a pull request!

## Getting started
To start, make sure you have VirtualBox and Vagrant installed on your Windows, Mac, or Linux host:

  * http://www.virtualbox.org/
  * https://vagrantup.com

To clone out this repository from git, you'll also need git installed. New to this stuff? See the **How to install git** section near the end for installing on Windows, Mac, and Debian/Ubuntu.

## Check out the source:

The following command should be sufficient on OS X or a Linux box. Using Windows? Check out the **Installing git on Windows, OS X, or Debian/Ubuntu** section further down - after installing a git client, you'll need to adjust line terminators with another command in order for everything to work as expected.

```shell
git clone https://github.com/kamwoods/vagrant-apache-flask-minimal
```

Once you have the source code (and you have unzipped it if you're using a release), change directory into vagrant-apache-flask-minimal, and make sure the associated Vagrant box (bentu/ubuntu-18.04) is added:

```shell
cd vagrant-apache-flask-minimal
vagrant box add bento/ubuntu-18.04
```

You will be prompted for a provider. Select **2) virtualbox** by typing '2' and hitting enter.

The first time you run **vagrant box add bento/ubuntu-18.04** may take some time. (Note: You only need to run "vagrant box add" for a specific box the **first** time after installing Vagrant. You may be promted to run the command **vagrant box update** in the future when attempting to run **vagrant up** in order to keep the box up to date).

## Once the base box is downloaded, you can start the service by running the command: 

```shell
vagrant up
```

from within the vagrant-apache-flask-minimal directory. This step can take a some time the first time you run the software. The installation script will provide feedback in the console as it installs each package. Once the virtual machine has been provisioned, open a web browser on your host and navigate to:

```shell
127.0.0.1:8080
```

to see the minimal app running.

## Terminating the service and virtual machine

If you need to stop the service, you can type:

```shell
vagrant halt
```

in the **vagrant-apache-flask-minimal** directory in the console or terminal on your host machine. The next time you issue the "vagrant up" command, the VM will restart in its previous state. 

If you need to delete the VM entirely, you can the the following command after halting the VM:

```shell
vagrant destroy
```

If you wish to build a new VM with updated sources, simply delete the vagrant-apache-flask-minimal directory after halting and destroying the previous VM, and clone or download the current sources from GitHub.

## Installing git on Windows, OS X, or Debian/Ubuntu

On **Windows**, download and install git from:

  * https://git-scm.com/downloads

On **MacOS**, run the following command in a terminal and click through the prompts:

```shell
xcode-select --install
```

On Debian-based variants of Linux (including Ubuntu), run the following from a terminal:

```shell
sudo apt-get install git
```

**IMPORTANT**: On Windows, you **must** make Git check out files with Unix-style line endings in order for the VM to run properly. After installing git, run the following in a console (cmd prompt):

```shell
git config --global core.autocrlf false
```

## License(s)

Unless otherwise indicated, software items in this repository are distributed under the terms of the GNU General Public License, Version 3. See the text file "COPYING" for further details about the terms of this license.

