.PHONY: help train run predict clean test-client docker-build docker-run docker-stop

help:
    @echo "Available commands:"
    @echo "  train          Train the model"
    @echo "  run            Run the Flask app"
    @echo "  predict        Make a prediction"
    @echo "  test-client    Test the client script"
    @echo "  clean          Clean up temporary files"
    @echo "  docker-build   Build Docker image"
    @echo "  docker-run     Run Docker container"
    @echo "  docker-stop    Stop Docker container"

train:
    python trained_model.py

run:
    python app.py

predict:
    @echo "Sending POST request to Flask endpoint..."
    curl -X POST -H "Content-Type: application/json" -d "{\"feature1\": 1.5, \"feature2\": 2.0, \"feature3\": 0.5, \"feature4\": -1.0, \"feature5\": 3.2}" http://127.0.0.1:5000/predict

test-client:
    @echo "Running client script..."
    python client.py

clean:
    @echo "Cleaning up temporary files..."
    rm -rf __pycache__

docker-build:
    @echo "Building Docker image..."
    docker build -t mlops .

docker-run:
    @echo "Running Docker container..."
    docker run -d -p 5000:5000 --name your-container-name your-image-name

docker-stop:
    @echo "Stopping Docker container..."
    docker stop task4
    docker rm task4
