## Database

This database application is deployed using a Statefulet, which is backed by a Persistent volume. That way, if the pod provisioned by the Statefulset would restart, the database would keep all the data, and the new pod would read from there. For the StorageClass, I used minikube's own Provisioner, `k8s.io/minikube-hostpath`.

I chose PostgreSQL for the database, and used Bitnami's Docker image as base (bitnami/postgresql), and added `init.sql` to `/docker-entrypoint-initdb.d/`, in order to create the `random` table, that will be used by our web app. I built and pushed the image to my dockerhub repository (vfrancax1/postgresql) for convenience.

I also decised to upload the username, password and database name to a Secret, as well as passing them to the `POSTGRESQL_USERNAME`, `POSTGRESQL_PASSWORD` and `POSTGRESQL_DATABASE` env vars of the container.

The database is also exposed to other applications in the cluster via a Headless Service. 
