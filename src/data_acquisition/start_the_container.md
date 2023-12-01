docker build -t open_data_hack_2023_image .

docker run -d -p 27017:27017 --name open_data_hack_2023_container open_data_hack_2023_image
