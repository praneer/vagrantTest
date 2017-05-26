Vagrant.configure(2) do |config|
	config.vm.define "devops-box" do |devbox|
		devbox.vm.box = "ubuntu/trusty64"
    		#devbox.vm.network "private_network", ip: "192.168.199.9"
    		#devbox.vm.hostname = "devops-box"
      		config.vm.provision "ansible_local" do |ansible|
			  ansible.playbook = "playbook.yml"
			  ansible.install_mode = "pip"
			  ansible.version = "latest"
			end
    		devbox.vm.provider "virtualbox" do |v|
    		  v.memory = 1024
    		  v.cpus = 2
    		end
	end
end