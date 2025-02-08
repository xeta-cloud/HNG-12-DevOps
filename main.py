from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    n = abs(n)  
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    n = abs(n)
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    num_str = str(abs(n))
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == abs(n)

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Enter a number")):
    # **Strict Input Validation**
    try:
        parsed_number = float(number)
    except ValueError:
        # Invalid input, return 400 Bad Request with the invalid input
        raise HTTPException(
            status_code=400,
            detail={  
                "number": number,  # Ensure the invalid input is included in the response
                "error": True
            }
        )
    
    # Convert to int if it is a whole number
    is_integer = parsed_number.is_integer()
    parsed_number = int(parsed_number) if is_integer else parsed_number  

    properties = []
    
    if is_integer:
        properties.append("even" if parsed_number % 2 == 0 else "odd")
        if is_prime(parsed_number):
            properties.append("prime")
        if is_perfect(parsed_number):
            properties.append("perfect")
        if is_armstrong(parsed_number):
            properties.append("armstrong")

    # **Calculate digit_sum** (sum of absolute digits)
    digit_sum = sum(int(digit) for digit in str(abs(int(parsed_number))) if digit.isdigit())

    # Fetch fun fact
    try:
        fun_fact = requests.get(f"http://numbersapi.com/{abs(parsed_number)}/math").text
    except requests.RequestException:
        fun_fact = "Fun fact unavailable"

    return {
        "number": parsed_number,
        "is_prime": is_prime(parsed_number) if is_integer else False,
        "is_perfect": is_perfect(parsed_number) if is_integer else False,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
