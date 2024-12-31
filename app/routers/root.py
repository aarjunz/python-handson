from fastapi import APIRouter

# Initialize the APIRouter instance
router = APIRouter()

@router.get("/")
def read_root():
    """
    Root endpoint that serves as a welcome or health check.
    """
    return {"message": "Welcome to ai-backend-service"}

@router.get("/health")
def health_check():
    """
    Health check endpoint to verify that the service is running.
    """
    return {"status": "healthy", "message": "ai-backend-service is up and running!"}
