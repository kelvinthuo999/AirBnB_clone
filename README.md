# HBNB - ALX School AirBnB Clone

This repository contains the ALX School AirBnB Clone project, a simplified version of the popular AirBnB platform developed as part of the Holberton School curriculum.

## Description

The AirBnB Clone project allows users to interact with various types of objects, such as users, states, cities, places, reviews, and amenities. This project includes a command-line interpreter that allows you to interact with these classes and perform various operations.

## Getting Started

### Prerequisites

- You need to have `Python 3` installed on your system.
- cd into the repository.
- Run the console.py script to start the console.
- To use the console, you can create classes, list, or destroy the classes.
- Use the quit command to stop the console.

## Tests

- Tests have been put in place to make sure all the classes function as intended.
- All the test can be run using the inbuilt unit test in Python.

## Architecture

- The project follows a modular architecture, with various components working together to achieve its goals. Here's an overview of the architecture:

### Core Modules

1. Core Modules
The core of the project consists of the following modules:

BaseModel: This module defines the BaseModel class, which serves as the foundation for all other classes in the project. It contains common attributes and methods shared by all classes.

FileStorage: The FileStorage class is responsible for serializing and deserializing instances to/from a JSON file. It maintains a dictionary of objects in memory and handles storage operations.

2. Class Modules
The project defines several class modules that inherit from BaseModel. Each class module represents a specific entity, such as users, places, cities, states, amenities, and reviews. Here are the class modules:

User: Defines the User class, which includes attributes like email, password, first name, and last name.

Place: Represents the Place class, which includes attributes like city ID, user ID, name, description, and various other details about places.

City: Represents cities and includes attributes such as the state ID and the city's name.

State: Defines the State class, which primarily includes the state's name.

Amenity: Represents amenities and includes a single attribute, which is the amenity's name.

Review: Defines the Review class, which includes attributes like the place ID, user ID, and the review's text.

3. Console Module
The console.py module provides a command-line interface for users to interact with the project. It allows users to perform operations such as creating, displaying, updating, and deleting instances of the classes.

4. Storage and Serialization
Instances of the classes are stored in memory in a dictionary, managed by the FileStorage class. The FileStorage class also handles the serialization of objects to a JSON file and deserialization from the JSON file.
5. Command Interpreter
The command interpreter module, console.py, uses the cmd module to create a command-line interface. Users can interact with the project by running commands to manipulate instances and data.

This modular architecture allows for easy maintenance, scalability, and separation of concerns. Each module is responsible for specific functionality, making the project more organized and extensible.
