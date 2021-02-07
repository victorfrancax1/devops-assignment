# stack-io-assignment

## 📖 About 

This solution has two components:
- Database: a PostgreSQL database, which is created using a Kubernetes Statefulset
- Application: a simple Flask (Python) web app, which is deployed using Kubernetes Deployments

## 🤖 Quickstart
During the development of the solution, I used [Minikube](https://minikube.sigs.k8s.io/docs/). It allows us to quickly set up a local Kubernetes cluster for testing purposes.

To create a new cluster:
```bash
minikube start
```
To discard an existing cluster:
```bash
minikube delete
```

I used minikube `addons` feature in order to provision `metrics-server`, which will be necessary for Kubernetes' HPAs to work properly. With the cluster already online, run:
```bash
minikube addons enable metrics-server
```
It's also worth to mention that minikube ships its own Dynamic Provisioner, `k8s.io/minikube-hostpath`, which uses hostPath. I used it to create the StorageClass for the PersistentVolumes used in the solution. 

Finally, in order to interact with the cluster, [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl) is necessary. Its binary can be installed separately, or it can be used via minikube:
```bash
minikube kubectl
```

## 🤠 Usage
To deploy the database, run:
```bash
kubectl create -f database/
```
To deploy the app, run:
```bash
kubectl create -f app/
```
