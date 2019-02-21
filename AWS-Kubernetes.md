Commands:

Set up an AWS account and a key.
```
pip install awscli
aws configure
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

More on `eksctl` here

Then we'll create a kubernetes cluster:

```
eksctl create cluster --name=cluster-1 --nodes=4 --region=us-east-1
```

We'll follow the instructions here:

http://docs.dask.org/en/latest/setup/kubernetes-helm.html



Kubernetes Stuff:

```
kubectl get nodes
kubectl --namespace kube-system create sa tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
kubectl get pods
kubectl get services
kubectl get pod agile-newt-dask-jupyter-54f86bfdd7-jdb5p
kubectl exec -it agile-newt-dask-jupyter-54f86bfdd7-jdb5p -- /bin/bash
```

Once in, clone this github and watch dask go!

