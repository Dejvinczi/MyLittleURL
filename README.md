# Recipe

REST application for shortening long urls. The idea for the app was https://tinyurl.com/app

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [API Documentation](#api-documentation)

## Features
- **User registration**: API for creating new system users for authentication purposes. 
- **URLs management**: Authorised users of the system can manage its links. 

## Requirements

- **Python**: This application requires **Python 3.11** or later. You can download and install Python from the [official Python website](https://www.python.org/).

- **Docker**: Ensure that Docker is installed on your system. You can download and install Docker Desktop from the [official Docker website](https://www.docker.com/).

- **Docker Compose**: Docker Compose is used for orchestrating multi-container Docker applications. It should be included with Docker Desktop installation on most platforms. If not, make sure to install Docker Compose separately following the instructions provided on the [Docker Compose documentation](https://docs.docker.com/compose/install/).

## Getting Started

### Installation

1. **Clone the repository**: Clone the repository to your local machine using Git:
    ```bash
    git clone https://github.com/Dejvinczi/MyLittleUrl.git
    ```
2. **Build Docker containers**: Use Docker Compose to build the Docker containers defined in the composition file `docker-compose.yaml`:
    ```bash
    docker-compose build
    ```

### Usage
- **Start Docker containers**: Start the Docker containers using Docker Compose:
    ```bash
    docker-compose up
    ```

## API Documentation
The API documentation is available at:<br /> 
**http://127.0.0.1:8000/api/**<br />