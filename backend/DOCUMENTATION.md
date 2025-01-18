
# Token-Based Authentication Flow

This document outlines the token-based authentication flow and the related functions implemented in the Django application using a custom user model.

## 1. User Registration (Signup)
- **Endpoint**: `/api/signup/`
- **Method**: `POST`
- **Description**: This endpoint allows new users to sign up. Upon successful registration, an authentication token is generated and returned.

### Example Request
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "password123",
  "role": "CLERK"
}
```

### Example Response
```json
{
  "user": {
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com",
    "role": "CLERK"
  },
  "token": "f2afca0567cd22a156f3791b7374ea774fd4b529"
}
```

## 2. User Login (Token Generation)
- **Endpoint**: `/api/api-token-auth/`
- **Method**: `POST`
- **Description**: This endpoint authenticates users and provides them with a token for subsequent requests.

### Example Request
```json
{
  "username": "newuser",
  "password": "password123"
}
```

### Example Response
```json
{
  "token": "f2afca0567cd22a156f3791b7374ea774fd4b529"
}
```

## 3. Accessing Protected Resource (Role-Based Dashboard)
- **Endpoint**: `/api/dashboard/`
- **Method**: `GET`
- **Description**: This endpoint allows authenticated users to access a dashboard based on their role. The user must provide a valid token in the request header.

### Example Request
```http
GET /api/dashboard/ HTTP/1.1
Authorization: Token f2afca0567cd22a156f3791b7374ea774fd4b529
```

### Example Response
```json
{
  "message": "Welcome to the Clerk Dashboard!"
}
```

## 4. Refreshing the Token
- **Endpoint**: `/api/refresh-token/`
- **Method**: `POST`
- **Description**: This endpoint allows users to refresh their authentication token when it expires. A valid token must be provided in the request header.

### Example Request
```http
POST /api/refresh-token/ HTTP/1.1
Authorization: Token f2afca0567cd22a156f3791b7374ea774fd4b529
```

### Example Response
```json
{
  "token": "d3f627a3cc840774077dc3a3dea69d5fbd43fe26"
}
```

## 5. Logging Out (Token Invalidations)
- **Endpoint**: `/api/logout/`
- **Method**: `POST`
- **Description**: This endpoint logs out the user by deleting their authentication token, rendering it invalid for future requests.

### Example Request
```http
POST /api/logout/ HTTP/1.1
Authorization: Token d3f627a3cc840774077dc3a3dea69d5fbd43fe26
```

### Example Response
```json
{
  "message": "Successfully logged out."
}
```

## 6. Error Handling for Invalid Tokens
- When a user attempts to access protected resources with an invalid or expired token, they receive an error message.

### Example Response for Invalid Token
```json
{
  "detail": "Invalid token."
}
```

## Complete Flow Summary
1. **Signup**: User registers, receives a token.
2. **Login**: User logs in, retrieves a token.
3. **Access Dashboard**: User accesses role-based resources using the token.
4. **Refresh Token**: User can refresh their token when it is about to expire.
5. **Logout**: User logs out, invalidating their current token.
6. **Error Handling**: If a token is invalid, an error response is returned.

This document provides a clear overview of how token-based authentication works within the application. For any further clarification or additional functionality, please reach out!
