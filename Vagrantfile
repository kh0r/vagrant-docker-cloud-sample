require 'yaml'

nodes = YAML.load_file("nodes.yml")['nodes']

Vagrant.configure(2) do |config|
  config.vm.box = 'ubuntu/trusty64'

  nodes.each_with_index do |token, index|
    config.vm.define "node-#{index}" do |node|
      node.vm.provision 'shell', inline: "curl -Ls https://get.cloud.docker.com/ | sudo -H sh -s #{token}"
      node.vm.hostname = "node-#{index}.local"
      node.vm.network "private_network", ip: "192.168.77.#{20+index}"
    end
  end

# not used
  # config.vm.define 's3_backup' do |backup|
  #   backup.vm.provision 'shell', path: 'init_backup.sh'
  #   backup.vm.hostname = "s3_backup.local"
  #   backup.vm.network "private_network", ip: "192.168.77.10"
  # end
end
