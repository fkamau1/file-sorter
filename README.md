# File Sorter
This project is designed to automatically sort specific file types from a source folder to a destination folder using Python.
## Getting Started
To get a copy of this project up and running on your local machine, simply follow these steps.
### Prerequisites
Ensure that you have the following installed:
- Python 3
- Docker (if you want to run the project in a Docker container)
### Forking the Repository
To fork this repository on GitHub, simply click the "Fork" button at the top right of the repository page.
### Cloning the Repository
Clone the repository by running the following command in your terminal or command prompt:
```bash
git clone https://github.com/your-username/file-sorter.git
```
## Running the Project Locally
### Using Python
1. Navigate to the file-sorter directory.
2. Run the Python script with the following command:
```bash
python file-sorter.py
```
### Using Docker
Build the Docker image by running the following command in the project's root directory:
```bash
docker build -t file-sorter-app .
```
Once the image is built, run a Docker container using the following command:
```bash
docker run file-sorter-app
```
### Pulling from Docker Hub
To pull the Docker image from Docker Hub, use the following command:
```bash
docker pull fkamau1/file-sorter:1.0.2
```

