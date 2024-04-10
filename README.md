
# Microservices-Based Reservation System

## Project Overview
This project develops a Microservices-Based Reservation System designed to streamline and manage reservations for restaurants and users. It breaks down the application into three main services: `user_service`, `restaurant_service`, and `reservation_service`, each with its dedicated functionalities and database interactions.

## Features
- **User Service:** Handles user registration, updates, retrieval, and deletion.
- **Restaurant Service:** Manages restaurant information including creation, updates, retrieval, and deletion of restaurant records.
- **Reservation Service:** Facilitates the creation, updating, retrieval, and cancellation of reservations.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Postman or any API testing tool

### Installation and Setup
Clone the repository:
```bash
git clone [repository URL]
```
Navigate to the project directory:
```bash
cd Microservices-Based-Reservation-System
```
Build and run the Docker containers:
```bash
docker-compose up --build
```
This command will start all the services along with the MySQL database.

### Accessing the Services
- User Service: http://localhost:8080/users
- Restaurant Service: http://localhost:8081/restaurants
- Reservation Service: http://localhost:8082/reservations

## API Reference
Detailed API endpoints and their descriptions are outlined below:

### User Service
- POST /users: Create a new user.
- GET /users/{user_id}: Retrieve user details.
- PUT /users/{user_id}: Update user information.
- DELETE /users/{user_id}: Delete a user.

### Restaurant Service
- POST /restaurants: Add a new restaurant.
- GET /restaurants/{restaurant_id}: Fetch restaurant details.
- PUT /restaurants/{restaurant_id}: Update restaurant information.
- DELETE /restaurants/{restaurant_id}: Remove a restaurant.

### Reservation Service
- POST /reservations: Create a new reservation.
- GET /reservations/{reservation_id}: Get reservation details.
- PUT /reservations/{reservation_id}: Update a reservation.
- DELETE /reservations/{reservation_id}: Cancel a reservation.

## Testing
Use Postman or a similar tool to test the API endpoints. Ensure to test all the CRUD operations for each service to verify the system's functionality.

## Development and Contributions
This project welcomes contributions. To contribute:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit changes and push them to your fork.
4. Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Flask for the backend service development.
- MySQL for database management.
- Docker for containerization and orchestration.
