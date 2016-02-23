# Vagrant Docker-Cloud sample

## Preparation

### Create a Docker-Cloud account
[https://cloud.docker.com/](https://cloud.docker.com/)

### Install docker-cloud CLI
- install docker-cloud python module: `pip install python-dockercloud`
- login: `docker login`
- generate a bunch of node-ids: `./generate_node_ids.py <<num_nodes>>` and copy the generated data to `nodes.yml`

## Config
copy `init_node_sample.sh` to `init_node.sh` and copy the link from `Bring your own node` in [https://cloud.docker.com/node/cluster/list/](https://cloud.docker.com/node/cluster/list/).
See [https://docs.docker.com/docker-cloud/getting-started/use-byon/](https://docs.docker.com/docker-cloud/getting-started/use-byon/) for more info.

## Start
```
vagrant up
```

## Further instructions
- [Setup Service (Apps/DB/etc...)](https://docs.docker.com/docker-cloud/getting-started/your_first_service/)
- [Setup loadbalancer](https://docs.docker.com/docker-cloud/tutorials/load-balance-hello-world/)
