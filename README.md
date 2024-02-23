 This is a url-shortening service written in Python with the Django Rest Framework
 
 # API Documentation

## Shorten URL Endpoint

**Endpoint:** `/shorten`

**Method:** `POST`

**Description:** This endpoint is used to shorten a URL.

### Request Body:

| Parameter | Type   | Description              |
|-----------|--------|--------------------------|
| url       | string | The URL to be shortened. |

### Response:

- **200 OK:** If the URL is successfully shortened.
    ```json
    {
        "originalUrl": "Original URL",
        "shortUrl": "Shortened URL"
    }
    ```

- **400 Bad Request:** If the request body is missing the URL.
    ```json
    "Error: No URL entered."
    ```

## Resolve Shortened URL Endpoint

**Endpoint:** `/resolve`

**Method:** `POST`

**Description:** This endpoint is used to resolve a shortened URL.

### Request Body:

| Parameter  | Type   | Description                    |
|------------|--------|--------------------------------|
| shortUrl   | string | The shortened URL to resolve.  |

### Response:

- **200 OK:** If the shortened URL is successfully resolved.
    ```json
    {
        "originalUrl": "Original URL",
        "shortUrl": "Shortened URL"
    }
    ```

- **400 Bad Request:** If the request body is missing the shortened URL or if the shortened URL is not found in the service.
    ```json
    "Error: No URL entered."   // If URL is missing
    "This URL did not originate from this service."   // If URL is not found
    ```