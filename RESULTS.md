# Lab Results

## Step 0.1: A first request with curl
- Command: `curl.exe https://quickpizza.grafana.com/api/names`
- Result: Successfully retrieved the pizza names.
- Total pizza names: 18

## Step 0.2: The status code and the headers
- Command: `curl.exe -i https://quickpizza.grafana.com/api/names`
- Status Code: 200 OK
- Content-Type: application/json
- Result: Successfully retrieved the pizza names and response headers.

## Step 0.3: A request that needs a token
- Request without token: 401 Unauthorized
- Response: `{"error":"authentication failed"}`
- Request with token: Successfully retrieved tools
- Tools: Knife, Pizza cutter, Scissors

## Step 0.4: Sending data with POST
- Request Method: POST
- Endpoint: /api/pizza
- Request Body: {"mustBeVegetarian": true}
- Pizza Name: A Soft Quattro Formaggi
- Calories: 575
- Vegetarian: true
- Result: Successfully received a vegetarian pizza.

## Step 0.5: Using Python requests
- Imported the requests library successfully.
- Sent a GET request to /api/names.
- Status Code: 200
- Content-Type: application/json
- Result: Successfully retrieved 18 pizza names as JSON data.

## Step 0.7: Testing an authenticated endpoint
- Created test_tools.py.
- Sent a GET request to /api/tools with an Authorization token.
- Status Code: 200
- Expected Tools: Knife, Pizza cutter, Scissors
- Result: Test passed successfully.

## Step 0.8: Fields inside the answer, and a request that must be refused
- Tested a vegetarian pizza request with an Authorization token.
- Verified that the pizza has a name and all ingredients are vegetarian.
- Tested a pizza request without an Authorization token.
- Expected Status Code: 401
- Expected Response: {"error": "authentication failed"}
- Result: Both tests passed.

### Step 0.12: A test without a session
- Run 1: Failed
- Run 2: Failed
- Run 3: Failed
The test failed in all three runs. Without a session, cookies are not maintained between requests, so the load balancer may route requests to different servers.

### Step 0.16, blocks of "how many of the three tools are excluded":
  - B1: 0 tools excluded
  - B2: 1 tool excluded
  - B3: 2 tools excluded
  - B4: 3 tools excluded
  
## Defect report
- Title: QuickPizza returns 500 when all three tools are excluded
- Request: POST /api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: Status 400 Bad Request with a JSON error message.
- Actual result: Status 500 Internal Server Error with an empty response body (Content-Length: 0).
- Severity: High — The API returns an internal server error instead of a meaningful client error when no pizza can satisfy the request. This may prevent client applications from handling the situation correctly.