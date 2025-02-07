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
    n = abs(n)  # Work with absolute values
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
    try:
        # Validate input: Only numbers allowed (negative, decimal, and integer)
        if not number.lstrip('-').replace('.', '', 1).isdigit():
            raise ValueError

        number = float(number)
        is_integer = number.is_integer()
        number = int(number) if is_integer else number  

        properties = []
        
        if is_integer:
            # Check even/odd
            properties.append("even" if number % 2 == 0 else "odd")
            if is_prime(number):
                properties.append("prime")
            if is_perfect(number):
                properties.append("perfect")
            if is_armstrong(number):
                properties.append("armstrong")

        # Calculate class sum (sum of absolute value digits)
        class_sum = sum(int(digit) for digit in str(abs(int(number))) if digit.isdigit())

        # Fetch fun fact from Numbers API
        try:
            fun_fact = requests.get(f"http://numbersapi.com/{abs(number)}/math").text
        except requests.RequestException:
            fun_fact = "Fun fact unavailable"

        return {
            "number": number,
            "is_prime": is_prime(number) if is_integer else False,
            "is_perfect": is_perfect(number) if is_integer else False,
            "properties": properties,
            "class_sum": class_sum,
            "fun_fact": fun_fact
        }

    except ValueError:
        return HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True
            }
        )
