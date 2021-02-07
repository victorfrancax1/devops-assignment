## simple-app

`simple-app` is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) (Python) web application. It responds to requests only at `/`, which can be either `GET` or `POST`.

- GET: returns 10 entries of the `random` database table at random order.
- POST: adds a new random text to the `random` database table.

The docker image is available at vfrancax1/simple-app for convenience.

The application's deployment has the following components:

- Deployment: a K8S Deployment, that is responsible for the application itself. The containers will read the credentials for the database (username, password and database name) from the respective Secret. It also points to the `pgsql` service, which proxies to the database.
- Service: a K8S Service to expose the application. Since it's required that the application is reachable from outside the cluster, I chose the `nodePort` type.
- HorizontalPodAutoscaler: this will be used to scale the application based on CPU usage.
- PodDisruptionBuget: this will ensure that at least 1 pod is still available during voluntary disruptions.
