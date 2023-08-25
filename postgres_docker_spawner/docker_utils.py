import docker
from typing import List
from .errors import ERROR_MESSAGES
from .utils import to_kebab_case, display_container_information_panels

POSTGRES_IMAGE_NAME = "postgres"

def list_containers(filters:dict = {}, all: bool = True) -> List:
    """
        Returns a list of containers for the given filters
    """

    try:
        client = docker.from_env()
        containers = client.containers.list(all=all, filters=filters)
        display_container_information_panels(containers)
    except:
        print(ERROR_MESSAGES["DE404"])
        
        
def create_postgres_container(port: int, name:str) -> None:
    """ Creates a new postgres container based on the given port and name """
    
    try:
        client = docker.from_env()
        
        if not postgres_image_exists(client):
            print(f"'{POSTGRES_IMAGE_NAME}' image not found. The utility will pull the image from DockerHub. This might take some time")
            pull_docker_image(client)
        
        try:
            container = client.containers.run(
                POSTGRES_IMAGE_NAME,
                detach=True,
                name=to_kebab_case(name),
                ports={'5432/tcp': port},
                environment={'POSTGRES_PASSWORD': 'postgres'}
            )
            
            return container
        except docker.errors.APIError as e:
            print(f"Error creating container: {e}")
    except:
        print(ERROR_MESSAGES["DE404"])
        
        
def remove_postgres_container(search_query: str, hard : bool) -> None:
    """ Remove the docker container by name"""
    
    try:
        # Create connection with docker engine
        client = docker.from_env()
        
        # Get container either based on container ID or container name
        try:
            container = client.containers.get(search_query)
            print(f'Stopping Container with ID : {container.id}')
            
            try:
                container.stop()
            except docker.errors.APIError:
                print("Server Error. Unable to connect to docker server")
                return
            except:
                print("Something Went Wrong!")
                return
                
            if hard:
                try:
                    container.remove()
                except:
                    print("Unable to remove container")
            
        except docker.errors.NotFound:
            print("Could not delete container. Container not found")
        except docker.errors.APIError:
            print("Error Processing Request. Problem with the docker server.")
        except:
            print("Something Went Wrong!")
    except:
        print(ERROR_MESSAGES["DE404"])
        
        
def postgres_image_exists(client):
    """ Checks if the postgres image exists on the server and returns a bool """
    return len(client.images.list(name=POSTGRES_IMAGE_NAME)) > 0
    
    
def pull_docker_image(client) -> None:
    """ Pulls the docker image if not present """
    try:
        print(f"Pulling {POSTGRES_IMAGE_NAME} image... ")
        client.images.pull(POSTGRES_IMAGE_NAME)
        print("Pull Complete!")
    except:
        print("Unable to pull image!")