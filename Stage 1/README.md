# 🚀 Number Classification API
This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact.

## 📖 Features  

✅ **Check if the number is Prime**  
✅ **Perfect number check**  
✅ **Determines if the number is an Armstrong**  
✅ **Classifies as Odd or Even**  
✅ **Calculates the Sum of digits**  
✅ **Retrieves a Math fun fact** (from [Numbers API](http://numbersapi.com))  


## 🛠️ Tech Stack  

| Technology   | Description                                      |
|-------------|--------------------------------------------------|
| **FastAPI**  | Python-based web framework                      |
| **Python**   | Backend programming language                    |
| **Uvicorn**  | ASGI server for running FastAPI                 |
| **Nginx**    | Reverse proxy for HTTP request handling              |
| **AWS EC2**  | Cloud hosting for deployment                    |
| **Requests** | Fetching data from external APIs (Numbers API)  |

---

## 📌 API Endpoints  

 **1️⃣ Classify a Number**  
**Endpoint:**  
```http
GET /api/classify-number?number={your_number}
Example Request:
http://44.203.73.184/api/classify-number?number=371
Example Response (200 OK):
{
    "number": 371,
    "properties": {
        "is_prime": false,
        "is_perfect": false,
        "is_armstrong": true,
        "parity": "odd"
    },
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}

2️⃣ Invalid Input Handling
If a non-numeric input is provided, the API returns 400 Bad Request.
Example Request:
GET /api/classify-number?number=abc
Response (400 Bad Request):
json
{
    "error": true,
    "message": "Invalid input: 'abc' is not a valid number."
}
🖥️ Step-by-Step Setup

1️⃣ Clone Repository & Navigate
git clone https://github.com/xeta-cloud/HNG-12-DevOps.git
cd number-classification-api

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies
pip install fastapi unicorn requests

4️⃣ Run Locally
uvicorn main:app --reload --host 0.0.0.0 --port 8000

5️⃣ Test API Locally
Visit Swagger UI:
http://127.0.0.1:8000/docs

🌍 Step-by-Step Deployment on AWS EC2

1️⃣ Launch an EC2 Instance
Choose Ubuntu 22.04
Open ports 80, 443, 22 in the security group
SSH into the instance:
ssh -i your-key.pem ubuntu@your-ec2-ip

2️⃣ Install System Dependencies
#Clone this repository and install dependencies
sudo apt update && sudo apt install -y python3-pip nginx
pip install fastapi uvicorn requests

3️⃣ Deploy FastAPI with Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

4️⃣ Configure Nginx as Reverse Proxy
sudo nano /etc/nginx/sites-available/fastapi
- Paste the following:
server {
    listen 80;
    server_name your-ec2-ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Activate Nginx Configuration:
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled
sudo systemctl restart nginx

5️⃣ Keep API Running with screen
screen -S fastapi
uvicorn main:app --host 0.0.0.0 --port 8000
(Press Ctrl + A, then D to detach)

🛠️ Testing Live Deployment
Check if your API is running by visiting:

http://44.203.73.184/api/classify-number?number=371

