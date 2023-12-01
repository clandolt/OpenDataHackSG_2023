docker build -t my_mongo_image .

docker run -d -p 27017:27017 --name my_mongo_container my_mongo_image
