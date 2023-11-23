# doct-cbd3324-backend
Containerization and Container Delivery - Backend Application

## Structure

```
doct-cbd3324-backend/
├── app/
│   ├── main.py
│   ├── ...
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── helm/
│   │   ├── backend/
│   │   │   ├── charts/
│   │   │   │   ├── backend/
│   │   │   │   ├── ...
│   │   ├── values.yaml
│   ├── manifests/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── ...
├── requirements.txt
├── tests/
│   ├── __init__.py
├── .gitignore
└── ...
```

## Dependencies Installation
```pip install -r requirements.txt```

## Run the application
```python3 app/main.py```

## Build and Run Docker Container
To build an image, use the command

```docker build -t apinyarr/dic-backend:test .```

To run a container, use the command

```docker run -d --rm --name dic-backend -p 8088:8088 -e MONGODB_HOST=host.docker.internal apinyarr/dic-backend:test```

## Run using Docker Compose
To run using Docker Compose (explicit the compose file name)

```docker compose -f docker-compose.yaml up -d```

## Run using Kubernetes
Starting order

*Remark* Skip step 1 if dictionary-namespace is created
1. Create namespace dictionary-namespace

```kubectl apply -f namespace.yaml```

*Remark* Skip step 2 if dic-config is created
2. Create configMap dic-config

```kubectl apply -f configmaps.yaml```

3. Create deployment dic-mongodb-deployment

```kubectl apply -f mongodb/mongodb-deployment.yaml```

4. Create service dic-mongodb-service

```kubectl apply -f mongodb/mongodb-service.yaml```

5. Create deployment dic-backend-deployment

```kubectl apply -f backend/backend-deployment.yaml```

6. Create service dic-backend-service

```kubectl apply -f backend/backend-service.yaml```