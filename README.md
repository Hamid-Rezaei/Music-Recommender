# Music Recommender System

## Overview


This project, developed using the Django-rest-framework, serves as a practical training ground for students enrolled in the Cloud Computing Course, offering hands-on experience and insights into the utilization of Platform as a Service (PaaS), Software as a Service (SaaS), and Infrastructure as a Service (IaaS) paradigms.

Implementation Details
----------------------
The project architecture comprises three distinct sections:

- `main`: The central component of the project is a Django application that acts as the primary service, orchestrating the entire system by managing API endpoints and coordinating the logic across all sections. This Django app serves as the main service, connecting and integrating the functionalities of other sections.
- `adapter`: Serving as the cornerstone for interacting with essential cloud services such as Amazon S3, RabbitMQ, and MailGun. 
- `schediler`: This  section functions as a dedicated scheduler within the project framework, executing tasks in response to specified job triggers. This segment operates autonomously, managing and overseeing the scheduling of various jobs based on predefined criteria.

How To Run
----------
1. **Clone the project**

2. **Set Up the Environment**: Fill this `.env` file with appropriate values. 
    
    ```
   # General
    FILES_FOLDER=
    
    # Postgres
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
       
    # Redis
    REDIS_HOST=
    REDIS_PORT=
    
    # RabbitMQ
    RABBITMQ_AUTO_ACK=
    RABBITMQ_USERNAME=
    RABBITMQ_PASSWORD=
    RABBITMQ_HOST=
    RABBITMQ_PORT=
    RABBITMQ_QUEUE=
    RABBITMQ_VHOST=
    
    # S3
    ENDPOINT_URL=
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_STORAGE_BUCKET_NAME=
    
    # Shazam
    SHAZAM_API_KEY=
    SHAZAM_URL=
    SHAZAM_HOST=
    
    # Spotify
    SPOTIFY_API_KEY=
    SPOTIFY_SEARCH_URL=
    SPOTIFY_RECOMMENDATION_URL=
    SPOTIFY_HOST=
    
    
    # Mail
    MAIL_URL=
    MAIL_API_KEY=
    MAIL_DOMAIN_NAME=

    ```

3. **Create project docker image**

    ```bash
    docker build . -t main_service
    ```

4. **Create docker network**

    ```bash
    docker network create musicnet 
    ```
   
5. **Start docker-compose.yml file**

    ```bash
    docker-compose up -d  
    ```