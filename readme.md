# **Dockerhub-GitHubActions Dockerimage CI pipeline**

A simple CI pipeline to validate repository pushes and pull requests.  

After a repository update, a docker image is published and pulled from dockerhub.com.
Tests are run against the new images' container, the push or pull request become effective once the tests are successful.


## **A. Publish Docker image**
1. **Create a Dockerimage from a Dockerfile**
    - ex. `docker create -t fastapi-slim:base .`
2. **Tag the Dockerimage with dockerhub's username**
    - ex. `docker tag fastapi-slim:base username/fastapi-slim:base`
3. **Publish Dockerimage on a dockerhub.com repository**
    - ex. `docker push username/fastapi-slim:base`
4. **Add dockerhub.com secrets to the github repository**
    - ex. "Settings" > "Secrets and Variables" > "Repository secrets":
      - "New repository secret" > 
        - "Name *" > `DOCKER_USERNAME`
        - "Secret *" > `username`
      - "New repository secret" > 
        - "Name *" > `DOCKER_PASSWORD`
        - "Secret *" > `password`
5. **Modify `docker-publish.yml`**
    - Fields env / DOCKER_REPO, DOCKER_TAG, DOCKERFILE
6. **Move `docker-publish.yml` to `.github/workflows/`**

## **B. Trigger automated testing**

7. **Move `ci-workflow.yml` to `.github/workflows/`**
8. **Make changes to `main.py` and commit / push**



#### **Attempts logs**
- 240305:
  - 16h22 modified secrets
  - 16h30 fixed typo **docker-publish:SUCCESS, ci-workflow:FAILURE**
  - 17h15 fixed bugs in `ci-workflow.yml`:
    -  **docker-publish:SUCCESS, ci-workflow:FAILURE**
  - 17h32 docker image is published with both timestamp and `latest` tag, `ci-workflow` will use `latest` tag instead of timestamp 
    -  **docker-publish:SUCCESS, ci-workflow:FAILURE**
  - 17h41 small modif in `ci-workflow.yml`
    -  **docker-publish:SUCCESS, ci-workflow:FAILURE**
  - 17h51 test without artifacts