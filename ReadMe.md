###### 1. Install Required Tools:

- Python (preferably 3.9 or higher)
- pip (Python package manager)
- Docker
- Azure CLI
- kubectl (Kubernetes command-line tool)
- An Integrated Development Environment (IDE) like VSCode or PyCharm

###### 2. Quick Setup

```bash
cd ai-backend-service
```

```bash
pip install -r requirements.txt
```

###### 3. Run the Application (Without Docker)

```bash
cd ai-backend-service
```
```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
```
```bash
pip install fastapi uvicorn
```

```bash
uvicorn main:app --reload
```
Open your browser or use Postman to test endpoints like http://127.0.0.1:8000.

###### 4. Run the Application using Docker

```bash
docker build -t ai-backend-service .
```
```bash
docker run -p 8000:8000 ai-backend-service
```
Open your browser or use Postman to test endpoints at http://localhost:8000

