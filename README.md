# Postgres Docker Spawner

Postgres Docker Spawner is a Python-based CLI tool designed to simplify the creation and management of PostgreSQL containers. If you find yourself working on multiple projects that require separate PostgreSQL databases or want to avoid conflicts with your local database setup, this utility is here to streamline the process.

> This is a very early verison of the project. There is plan to drastically improve UI using `rich` and add
> further monitoring utilities. Also there are plans to add more configurable options like choosing postgres image, mounting volumes etc.

## Why Postgres Docker Spawner?

Working on numerous projects simultaneously often demands isolated database environments. Managing multiple local PostgreSQL instances can become challenging and prone to interference. Containers offer a solution by allowing the creation of distinct PostgreSQL instances without conflicts. However, setting up and managing these containers can be complex and time-consuming.

Postgres Docker Spawner steps in to address these challenges. Its primary objective is to provide a straightforward and seamless process for managing PostgreSQL containers.

## Features

- Simple CLI: The utility offers a user-friendly command-line interface that simplifies the creation, listing, and stopping of PostgreSQL containers.

- Isolated Environments: With containerization, each project can have its own PostgreSQL database, ensuring isolation and preventing interference.

- Effortless Management: Postgres Docker Spawner automates the process of container creation, management, and removal, making it quick and hassle-free.

## Getting Started

### Installation

To use Postgres Docker Spawner, you'll need to install it. Open your terminal and run:

```bash
pip install <postgres-docker-spawner wheel>
```

You can get the wheel file from releases section of the repo

### Dev Setup

1. Clone the repo
2. Run `poetry install` to add all the necessary dependencies.
3. To create build, run: `poetry build`

## Usage

### Creating a PostgreSQL Container:

To create a new PostgreSQL container, use the following command:

```bash
dockerps up
OR
dockerps up --port <PORT NO> --name <Container Name>
```

You can either pass the vars using flags or follow the prompts to provide the port and name for the container.

### Listing Containers:

To list all running PostgreSQL containers, use the command:

```bash
dockerps list
```

You can also use the --all flag to list all containers, including stopped ones.

### Stopping Containers:

To stop a running PostgreSQL container, use the command:

```bash
dockerps stop <container_id>
```

Replace <container_id> with the ID of the container you want to stop.

## Contributing

Contributions are welcome! The current version is a very rudimentary utility. If you have any feature suggestions, quality of life improvements, bug reports etc. Please open an issue.

## Acknowledgements

Postgres Docker Spawner was inspired by the need for simplified PostgreSQL container management in development workflows.
