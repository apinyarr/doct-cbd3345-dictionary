# doct-cbd3324-backend
Containerization and Container Delivery - Backend Application

## Structure

```
doct-cbd3324-backend/           
├── app/                        # Python Flask application path
│   ├── main.py                 # Python Web Application code
│   └── ...
├── k8s/                        # K8s folder
│   ├── helm/                   # Helm structure path
│   │   ├── dictionary/         # Dictionary chart
│   │   ├── mongodb/            # MongoDB chart
│   │   ├── rbac/               # RBAC chart
│   │   ├── values.yaml         # Charts share value file
|   |   └── ...
│   └── manifests/
|       ├── dictionary/         # Dictionary manifest files
|       ├── mongodb/            # MongoDB manifest files
|       ├── rback/              # RBAC manifest files
|       ├── configmaps-prd.yml  # ConfigMap config for PRD
|       ├── configmaps.yml      # ConfigMap config for UAT
|       ├── namespace-prd.yml   # Namespace config for PRD
|       ├── namespace.yml       # Namespace config for UAT
|       ├── secrets.yml         # Secret config file
|       └── ...
├── tests/
│   ├── __init__.py             # Module structure file
│   ├── test_app_json.py        # Python unit test file
├── .gitignore                  # Excluded Files List for Git
├── docker-compose.yml          # Docker Compose file for multi-container
├── Dockerfile                  # Dockerfile to build an image
├── README.md                   # This readme file
├── requirements.txt            # Python dependencies requirement
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
