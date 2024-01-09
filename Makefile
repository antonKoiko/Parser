IMAGE_NAME := framework 
CONTAINER_NAME := framework_container

.PHONY: build run interact background stop clean

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it $(IMAGE_NAME)

interact:
	docker run --rm -it $(IMAGE_NAME) /bin/bash

background:
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rmi $(IMAGE_NAME)
