# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=""
ENV MONGO_INITDB_ROOT_PASSWORD=""
ENV MONGO_INITDB_DATABASE="open_data_hack_2023"

# Expose MongoDB default port
EXPOSE 27017

# Start MongoDB when the container launches
CMD ["mongod"]