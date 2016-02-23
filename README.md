# Vagrant Docker-Cloud sample

## Preparation

### Create a Docker-Cloud account
[https://cloud.docker.com/](https://cloud.docker.com/)

### Install docker-cloud CLI
- install docker-cloud python module: `pip install python-dockercloud`
- login: `docker login`
- generate a bunch of node-ids: `./generate_node_ids.py <<num_nodes>>` and copy the generated data to `nodes.yml`

## Start
```
vagrant up
```

The nodes should now be visible in [Docker Cloud's node dashboard](https://cloud.docker.com/node/cluster/list/)

## Further instructions
- [Setup Service (Apps/DB/etc...)](https://docs.docker.com/docker-cloud/getting-started/your_first_service/)
- [Setup loadbalancer](https://docs.docker.com/docker-cloud/tutorials/load-balance-hello-world/)
