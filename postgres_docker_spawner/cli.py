import click
from .docker_utils import list_containers, create_postgres_container, remove_postgres_container

@click.group()
def cli():
    pass

@cli.command(name="list")
@click.option('--all', is_flag=True, default=False, help='Display all (running and stopped) containers')
def list(all):
    """
        List all containers
        Lists all the docker containers running postgres
    """
    
    filters = {"ancestor": "postgres"}
    list_containers(filters=filters, all=all)


@cli.command(name="up")
@click.option('--port', prompt='Port to expose', type=int, help="Port Number which docker will expose for the postgres instance")
@click.option('--name', prompt='Name of app/DB', type=str, help="Name of the docker container")
def up(port, name):
    """Create a new PostgreSQL container"""
    
    container = create_postgres_container(port, name)
    
    if not container:
        print("Could not create container")
        return
    
    click.echo(f"Container {name} started with ID: {container.id} on port : {port}")
    click.echo(f"Default user set to postgres, password = postgres")
    click.echo(f"You can connect to the DB @ localhost:{port}")
    click.echo(f"To connect using psql, use: psql -h localhost -p {port} -U postgres")
    

@cli.command(name="stop")
@click.argument('container_identifier', required=True)
@click.option('--hard', is_flag=True, default=False, help="Stop and DELETE the container")
def stop(container_identifier, hard):
    """Stop a running PostgreSQL container"""
    remove_postgres_container(container_identifier, hard)
    
    
if __name__ == '__main__':
    cli()