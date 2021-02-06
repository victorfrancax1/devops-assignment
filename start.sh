kubectl create -f database/pgsql-storageclass.yaml
kubectl create -f database/pgsql-storage-resources.yaml
kubectl create -f database/pgsql-creds.yaml
kubectl create -f database/pgsql-statefulset.yaml
