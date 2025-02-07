# 🚀 Number Classification API

## 📖 Overview  
The **Number Classification API** is a RESTful API that analyzes a given number and returns its mathematical properties, along with a fun fact. The API provides insights such as:  
✅ **Prime check**  
✅ **Perfect number check**  
✅ **Armstrong (Narcissistic) number check**  
✅ **Even/Odd classification**  
✅ **Digit sum calculation**  
✅ **Math fun fact** from the Numbers API  

This API is built using **FastAPI**, deployed on **AWS EC2**, and supports **CORS** for cross-origin access.

---

## ⚡ API Features  
✅ Accepts **GET** requests with a query parameter (`number`)  
✅ Returns responses in **JSON format**  
✅ Handles **CORS** (Cross-Origin Resource Sharing)  
✅ Includes **error handling** for invalid inputs  
✅ Fetches **math fun facts** from [Numbers API](http://numbersapi.com)  
✅ Hosted on a **publicly accessible endpoint**  

---

## 🛠️ Tech Stack  

| Technology       | Description                                  |
|-----------------|----------------------------------------------|
| **FastAPI**     | High-performance Python web framework       |
| **Python**      | Backend programming language                |
| **AWS EC2**     | Cloud hosting for deployment                |
| **CORS**        | Handles cross-origin requests               |
| **GitHub**      | Version control for codebase                |


---

## 📌 API Endpoints  

### **1️⃣ Classify a Number**  
**Endpoint:**  
```http
GET /api/classify-number?number={your_number}

## 📌 API Endpoints  

### **1️⃣ Classify a Number**  
**Endpoint:**  
```http
GET /api/classify-number?number={your_number}
Example Request:

http
Copy
Edit
GET /api/classify-number?number=371
Example Response (200 OK):

json
Copy
Edit
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

http
Copy
Edit
GET /api/classify-number?number=abc
Response (400 Bad Request):

json
Copy
Edit
{
    "error": true,
    "message": "Invalid input: 'abc' is not a valid number."
}
🖥️ Local Setup & Testing
1️⃣ Clone Repository
sh
Copy
Edit
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
2️⃣ Create Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run Locally
sh
Copy
Edit
uvicorn main:app --reload --host 0.0.0.0 --port 8000
5️⃣ Test API Locally
Open your browser or Postman and visit:
http://127.0.0.1:8000/docs

🌍 Deployment to AWS EC2
1️⃣ Launch an EC2 Instance
Choose Ubuntu 22.04
Configure Security Group to allow port 8000 (or 80 if using Nginx)
SSH into your instance:
sh
Copy
Edit
ssh -i your-key.pem ubuntu@your-ec2-ip
2️⃣ Install Python & Dependencies
sh
Copy
Edit
sudo apt update && sudo apt install -y python3-pip
pip install fastapi uvicorn requests
3️⃣ Deploy the API on EC2
sh
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000
4️⃣ Keep the API Running (Using screen or nohup)
sh
Copy
Edit
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > output.log 2>&1 &
5️⃣ Test Your Live API
Visit:

sh
Copy
Edit
http://your-ec2-ip:8000/api/classify-number?number=371


