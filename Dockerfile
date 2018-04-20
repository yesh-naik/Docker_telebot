FROM python:2.7-slim

# Createa and Set the working directory to /twitter
RUN mkdir -p /twitter
WORKDIR /twitter


# Copy the required contents into the container at /twitter
ADD users.yml /twitter
ADD send_tweets_to_telegram.py /twitter
ADD config.py /twitter
ADD requirements.txt /twitter

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "./send_tweets_to_telegram.py"]
