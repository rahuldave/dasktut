Commands:

Set up an AWS account and a key.

Alternatively you might want to set up minikube on your machine. Both will take some time.

```
pip install awscli
aws configure
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

More on `eksctl` here: https://eksctl.io/

Then we'll create a kubernetes cluster:

```
eksctl create cluster --name=cluster-1 --nodes=4 --region=us-east-1
```

We'll follow the instructions here:

http://docs.dask.org/en/latest/setup/kubernetes-helm.html

First:


Kubernetes Stuff:

```
kubectl get nodes
kubectl --namespace kube-system create sa tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller

```

Install helm. See the dask link above for how.

Helm Stuff:

```
helm init --service-account tiller
```

Give it 2 minutes

```
helm version
helm repo update
helm install stable/dask
helm status agile-newt
helm list
helm upgrade agile-newt stable/dask -f config.yaml
helm status agile-newt
```

Kubernetes Stuff:

```
kubectl get pods
kubectl get services

```

For more details and a shell you will need a command like this. Your exact pod names will be different..

```
kubectl get pod agile-newt-dask-jupyter-54f86bfdd7-jdb5p
kubectl exec -it agile-newt-dask-jupyter-54f86bfdd7-jdb5p -- /bin/bash
```

Once in, clone this github and watch dask go!

**DELETE CLUSTER**:

`eksctl delete cluster --name=<name> [--region=<region>]`
