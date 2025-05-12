#!/bin/bash

IMAGE=blanket77/flask-cicd-app:latest # Replace with your Docker image name

echo "Pulling image from DockerHub..."  
docker pull blanket77/flask-cicd-app:latest

echo "🧹 Cleaning up old container..."
docker stop flask-app || true # Stop the container if it's running
docker rm flask-app || true # Remove the container if it exists!

echo "🔥 Running new container..." 
docker run -d --name flask-app -p 8080:5000 blanket77/flask-cicd-app:latest

echo "🧽 Cleaning up dangling images..."
docker image prune -f  # Remove untagged (<none>) images without confirmation!!s