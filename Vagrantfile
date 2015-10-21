Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false

  config.vm.define "main" do |host|
    host.vm.network "private_network", ip: "172.16.100.10"

    host.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
  end

  ###########

  # config.vm.provision "ansible" do |ansible|
    # ansible.playbook = "provision/setup.yml"
  # end

end