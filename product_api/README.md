E-Commerce-Product API

```pip install -r requirements.txt```

{
    "swagger": "2.0",
    "info": {
        "title": "E-Commerce-Product API",
        "description": "API that allows the user to order products, track orders and check seamlessly",
        "contact": {
        "name": "Kenward Terhemba",
        "email": "codewithkenward@gmail.com",
        "projects": "https://github.com/Kenward-dev"
        },
        "version": "v1"
    },
    "host": "127.0.0.1:8000",
    "schemes": [
        "http"
    ],
    "basePath": "/api/v1",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "Token": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
        }
    },
    "security": [
        {
        "Token": []
        }
    ],
    "paths": {
        "/auth/login/": {
        "post": {
            "operationId": "auth_login_create",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "required": [
                    "email",
                    "password"
                ],
                "type": "object",
                "properties": {
                    "email": {
                    "description": "User email",
                    "type": "string"
                    },
                    "password": {
                    "description": "User password",
                    "type": "string"
                    }
                }
                }
            }
            ],
            "responses": {
            "200": {
                "description": "Successful Login",
                "schema": {
                "type": "object",
                "properties": {
                    "message": {
                    "type": "string"
                    },
                    "token": {
                    "type": "object",
                    "properties": {
                        "access": {
                        "type": "string"
                        },
                        "refresh": {
                        "type": "string"
                        }
                    }
                    }
                }
                }
            },
            "400": {
                "description": "Bad Request"
            },
            "401": {
                "description": "Unauthorized"
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/auth/register/": {
        "post": {
            "operationId": "auth_register_create",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/User"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/User"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/auth/token/": {
        "post": {
            "operationId": "auth_token_create",
            "description": "Takes a set of user credentials and returns an access and refresh JSON web\ntoken pair to prove the authentication of those credentials.",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/TokenObtainPair"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/TokenObtainPair"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/auth/token/refresh/": {
        "post": {
            "operationId": "auth_token_refresh_create",
            "description": "Takes a refresh type JSON web token and returns an access type JSON web\ntoken if the refresh token is valid.",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/TokenRefresh"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/TokenRefresh"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/auth/token/verify/": {
        "post": {
            "operationId": "auth_token_verify_create",
            "description": "Takes a token and indicates if it is valid.  This view provides no\ninformation about a token's fitness for a particular use.",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/TokenVerify"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/TokenVerify"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/auth/user/profile/": {
        "get": {
            "operationId": "auth_user_profile_read",
            "description": "",
            "parameters": [],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Profile"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "put": {
            "operationId": "auth_user_profile_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Profile"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Profile"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "patch": {
            "operationId": "auth_user_profile_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Profile"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Profile"
                }
            }
            },
            "tags": [
            "auth"
            ]
        },
        "parameters": []
        },
        "/cart/": {
        "get": {
            "operationId": "cart_read",
            "description": "",
            "parameters": [],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Cart"
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "parameters": []
        },
        "/cart/items/": {
        "get": {
            "operationId": "cart_items_list",
            "description": "",
            "parameters": [
            {
                "name": "page",
                "in": "query",
                "description": "A page number within the paginated result set.",
                "required": false,
                "type": "integer"
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "required": [
                    "count",
                    "results"
                ],
                "type": "object",
                "properties": {
                    "count": {
                    "type": "integer"
                    },
                    "next": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "previous": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "results": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/CartItem"
                    }
                    }
                }
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "post": {
            "operationId": "cart_items_create",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "parameters": []
        },
        "/cart/items/{id}/": {
        "get": {
            "operationId": "cart_items_read",
            "description": "",
            "parameters": [],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "put": {
            "operationId": "cart_items_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "patch": {
            "operationId": "cart_items_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/CartItem"
                }
            }
            },
            "tags": [
            "cart"
            ]
        },
        "delete": {
            "operationId": "cart_items_delete",
            "description": "",
            "parameters": [],
            "responses": {
            "204": {
                "description": ""
            }
            },
            "tags": [
            "cart"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "required": true,
            "type": "string"
            }
        ]
        },
        "/checkout/": {
        "post": {
            "operationId": "checkout_create",
            "description": "",
            "parameters": [],
            "responses": {
            "201": {
                "description": ""
            }
            },
            "tags": [
            "checkout"
            ]
        },
        "parameters": []
        },
        "/orders/": {
        "get": {
            "operationId": "orders_list",
            "description": "",
            "parameters": [
            {
                "name": "page",
                "in": "query",
                "description": "A page number within the paginated result set.",
                "required": false,
                "type": "integer"
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "required": [
                    "count",
                    "results"
                ],
                "type": "object",
                "properties": {
                    "count": {
                    "type": "integer"
                    },
                    "next": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "previous": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "results": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Order"
                    }
                    }
                }
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "parameters": []
        },
        "/orders/seller/": {
        "get": {
            "operationId": "orders_seller_list",
            "description": "",
            "parameters": [
            {
                "name": "page",
                "in": "query",
                "description": "A page number within the paginated result set.",
                "required": false,
                "type": "integer"
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "required": [
                    "count",
                    "results"
                ],
                "type": "object",
                "properties": {
                    "count": {
                    "type": "integer"
                    },
                    "next": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "previous": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "results": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Order"
                    }
                    }
                }
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "parameters": []
        },
        "/orders/update/{id}/": {
        "put": {
            "operationId": "orders_update_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Order"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Order"
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "patch": {
            "operationId": "orders_update_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Order"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Order"
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "description": "A unique integer value identifying this order.",
            "required": true,
            "type": "integer"
            }
        ]
        },
        "/orders/{id}/": {
        "get": {
            "operationId": "orders_read",
            "description": "",
            "parameters": [],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Order"
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "required": true,
            "type": "string"
            }
        ]
        },
        "/orders/{order_id}/items/{item_id}/return/": {
        "put": {
            "operationId": "orders_items_return_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/OrderItem"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/OrderItem"
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "patch": {
            "operationId": "orders_items_return_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/OrderItem"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/OrderItem"
                }
            }
            },
            "tags": [
            "orders"
            ]
        },
        "parameters": [
            {
            "name": "order_id",
            "in": "path",
            "required": true,
            "type": "string"
            },
            {
            "name": "item_id",
            "in": "path",
            "required": true,
            "type": "string"
            }
        ]
        },
        "/product/{product_id}/reviews/": {
        "get": {
            "operationId": "product_reviews_list",
            "description": "",
            "parameters": [
            {
                "name": "page",
                "in": "query",
                "description": "A page number within the paginated result set.",
                "required": false,
                "type": "integer"
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "required": [
                    "count",
                    "results"
                ],
                "type": "object",
                "properties": {
                    "count": {
                    "type": "integer"
                    },
                    "next": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "previous": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "results": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Review"
                    }
                    }
                }
                }
            }
            },
            "tags": [
            "product"
            ]
        },
        "post": {
            "operationId": "product_reviews_create",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            },
            "tags": [
            "product"
            ]
        },
        "parameters": [
            {
            "name": "product_id",
            "in": "path",
            "required": true,
            "type": "string"
            }
        ]
        },
        "/product/{product_id}/reviews/{id}/": {
        "get": {
            "operationId": "product_reviews_read",
            "description": "",
            "parameters": [],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            },
            "tags": [
            "product"
            ]
        },
        "put": {
            "operationId": "product_reviews_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            },
            "tags": [
            "product"
            ]
        },
        "patch": {
            "operationId": "product_reviews_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Review"
                }
            }
            },
            "tags": [
            "product"
            ]
        },
        "delete": {
            "operationId": "product_reviews_delete",
            "description": "",
            "parameters": [],
            "responses": {
            "204": {
                "description": ""
            }
            },
            "tags": [
            "product"
            ]
        },
        "parameters": [
            {
            "name": "product_id",
            "in": "path",
            "required": true,
            "type": "string"
            },
            {
            "name": "id",
            "in": "path",
            "required": true,
            "type": "string"
            }
        ]
        },
        "/products/": {
        "get": {
            "operationId": "products_list",
            "description": "",
            "parameters": [
            {
                "name": "search",
                "in": "query",
                "description": "A search term.",
                "required": false,
                "type": "string"
            },
            {
                "name": "ordering",
                "in": "query",
                "description": "Which field to use when ordering the results.",
                "required": false,
                "type": "string"
            },
            {
                "name": "page",
                "in": "query",
                "description": "A page number within the paginated result set.",
                "required": false,
                "type": "integer"
            },
            {
                "name": "page_size",
                "in": "query",
                "description": "Number of results to return per page.",
                "required": false,
                "type": "integer"
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "required": [
                    "count",
                    "results"
                ],
                "type": "object",
                "properties": {
                    "count": {
                    "type": "integer"
                    },
                    "next": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "previous": {
                    "type": "string",
                    "format": "uri",
                    "x-nullable": true
                    },
                    "results": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Product"
                    }
                    }
                }
                }
            }
            },
            "tags": [
            "products"
            ]
        },
        "parameters": []
        },
        "/products/create/": {
        "post": {
            "operationId": "products_create_create",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            ],
            "responses": {
            "201": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            },
            "tags": [
            "products"
            ]
        },
        "parameters": []
        },
        "/products/{id}/delete/": {
        "delete": {
            "operationId": "products_delete_delete",
            "description": "",
            "parameters": [],
            "responses": {
            "204": {
                "description": ""
            }
            },
            "tags": [
            "products"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "description": "A unique integer value identifying this product.",
            "required": true,
            "type": "integer"
            }
        ]
        },
        "/products/{id}/update/": {
        "put": {
            "operationId": "products_update_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            },
            "tags": [
            "products"
            ]
        },
        "patch": {
            "operationId": "products_update_partial_update",
            "description": "",
            "parameters": [
            {
                "name": "data",
                "in": "body",
                "required": true,
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            ],
            "responses": {
            "200": {
                "description": "",
                "schema": {
                "$ref": "#/definitions/Product"
                }
            }
            },
            "tags": [
            "products"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "description": "A unique integer value identifying this product.",
            "required": true,
            "type": "integer"
            }
        ]
        },
        "/reviews/{id}/delete/": {
        "delete": {
            "operationId": "reviews_delete_delete",
            "description": "",
            "parameters": [],
            "responses": {
            "204": {
                "description": ""
            }
            },
            "tags": [
            "reviews"
            ]
        },
        "parameters": [
            {
            "name": "id",
            "in": "path",
            "description": "A unique integer value identifying this review.",
            "required": true,
            "type": "integer"
            }
        ]
        }
    },
    "definitions": {
        "User": {
        "required": [
            "email",
            "password"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "email": {
            "title": "Email",
            "type": "string",
            "format": "email",
            "maxLength": 254,
            "minLength": 1
            },
            "username": {
            "title": "Username",
            "type": "string",
            "maxLength": 50,
            "x-nullable": true
            },
            "role": {
            "title": "Role",
            "type": "string",
            "enum": [
                "admin",
                "seller",
                "customer"
            ]
            },
            "password": {
            "title": "Password",
            "type": "string",
            "minLength": 1
            },
            "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            },
            "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            }
        }
        },
        "TokenObtainPair": {
        "required": [
            "email",
            "password"
        ],
        "type": "object",
        "properties": {
            "email": {
            "title": "Email",
            "type": "string",
            "minLength": 1
            },
            "password": {
            "title": "Password",
            "type": "string",
            "minLength": 1
            }
        }
        },
        "TokenRefresh": {
        "required": [
            "refresh"
        ],
        "type": "object",
        "properties": {
            "refresh": {
            "title": "Refresh",
            "type": "string",
            "minLength": 1
            },
            "access": {
            "title": "Access",
            "type": "string",
            "readOnly": true,
            "minLength": 1
            }
        }
        },
        "TokenVerify": {
        "required": [
            "token"
        ],
        "type": "object",
        "properties": {
            "token": {
            "title": "Token",
            "type": "string",
            "minLength": 1
            }
        }
        },
        "Profile": {
        "required": [
            "username"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "username": {
            "title": "Username",
            "type": "string",
            "minLength": 1
            },
            "user": {
            "title": "User",
            "type": "string",
            "readOnly": true
            },
            "role": {
            "title": "Role",
            "type": "string",
            "readOnly": true
            },
            "date_of_birth": {
            "title": "Date of birth",
            "type": "string",
            "format": "date",
            "x-nullable": true
            },
            "address": {
            "title": "Address",
            "type": "string",
            "x-nullable": true
            },
            "phone_number": {
            "title": "Phone number",
            "type": "string",
            "maxLength": 15,
            "x-nullable": true
            }
        }
        },
        "Product": {
        "required": [
            "name",
            "description",
            "price",
            "category"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 50,
            "minLength": 1
            },
            "description": {
            "title": "Description",
            "type": "string",
            "minLength": 1
            },
            "price": {
            "title": "Price",
            "type": "string",
            "format": "decimal"
            },
            "formatted_price": {
            "title": "Formatted price",
            "type": "string",
            "readOnly": true
            },
            "stock_quantity": {
            "title": "Stock quantity",
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
            },
            "image_url": {
            "title": "Image url",
            "type": "string",
            "format": "uri",
            "maxLength": 200,
            "x-nullable": true
            },
            "category": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 1
            }
            },
            "seller": {
            "title": "Seller",
            "type": "integer",
            "readOnly": true
            },
            "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            },
            "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            }
        }
        },
        "CartItem": {
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "product": {
            "$ref": "#/definitions/Product"
            },
            "quantity": {
            "title": "Quantity",
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
            },
            "total_price": {
            "title": "Total price",
            "type": "string",
            "format": "decimal",
            "readOnly": true
            }
        }
        },
        "Cart": {
        "required": [
            "user"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "user": {
            "title": "User",
            "type": "integer"
            },
            "items": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/CartItem"
            },
            "readOnly": true
            },
            "total_price": {
            "title": "Total price",
            "type": "string",
            "format": "decimal",
            "readOnly": true
            },
            "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            },
            "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            }
        }
        },
        "OrderItem": {
        "required": [
            "price"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "product": {
            "$ref": "#/definitions/Product"
            },
            "quantity": {
            "title": "Quantity",
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
            },
            "price": {
            "title": "Price",
            "type": "string",
            "format": "decimal"
            },
            "total_price": {
            "title": "Total price",
            "type": "string",
            "format": "decimal",
            "readOnly": true
            }
        }
        },
        "Order": {
        "required": [
            "user",
            "status"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "user": {
            "title": "User",
            "type": "integer"
            },
            "items": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/OrderItem"
            },
            "readOnly": true
            },
            "status": {
            "title": "Status",
            "type": "string",
            "enum": [
                "P",
                "C",
                "X",
                "R"
            ]
            },
            "total_price": {
            "title": "Total price",
            "type": "string",
            "format": "decimal",
            "readOnly": true
            },
            "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            }
        }
        },
        "Review": {
        "required": [
            "product",
            "rating"
        ],
        "type": "object",
        "properties": {
            "id": {
            "title": "ID",
            "type": "integer",
            "readOnly": true
            },
            "product": {
            "title": "Product",
            "type": "integer"
            },
            "user": {
            "title": "User",
            "type": "string",
            "readOnly": true
            },
            "rating": {
            "title": "Rating",
            "type": "integer",
            "maximum": 5,
            "minimum": 1
            },
            "comment": {
            "title": "Comment",
            "type": "string",
            "x-nullable": true
            },
            "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            },
            "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
            }
        }
        }
    }
}
