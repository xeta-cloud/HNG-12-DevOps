from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (can be restricted)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Enter a number")):
    """
    API endpoint to classify a number and return its mathematical properties along with a fun fact.
    """
    if not number.lstrip("-").isdigit():
        # ✅ Now correctly raises HTTPException with a 400 status
        raise HTTPException(
            status_code=400,
            detail={"number": number, "error": True}
        )

    number = int(number)

    properties = []
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    if is_prime(number):
        properties.append("prime")

    if is_perfect(number):
        properties.append("perfect")

    if is_armstrong(number):
        properties.append("armstrong")

    class_sum = sum(int(digit) for digit in str(abs(number)))

    # Fetch fun fact
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math")
    fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available."

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": class_sum,
        "fun_fact": fun_fact
    }

@app.get("/")
async def root():
    return {"message": "Number Classification API is running!"}
