# Numb App - Mathematical Number Classifier

Numb App is a Django-based web application that takes a number as input and returns interesting mathematical properties about it, along with a fun fact. It is designed to provide quick insights into the properties of numbers in a fun and educational way.

---

## Features

- **Number Classification**: Classifies a number based on its mathematical properties.
- **Mathematical Properties**:
  - Checks if the number is **prime**.
  - Checks if the number is **perfect**.
  - Determines if the number is an **Armstrong number**.
  - Identifies if the number is **even** or **odd**.
  - Calculates the **sum of its digits**.
- **Fun Fact**: Provides a fun fact about the number.
- **Error Handling**: Handles invalid inputs gracefully.

---

## API Endpoint

### Request

Make a **GET** request to the following endpoint:

- /api/classify-number?number=any positive whole number

### Response

- **Success (200 OK)**:
  ```json
  {
    "number": 8,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "even"],
    "digit_sum": 8,
    "fun_fact": "8 is the base of the octal number system, which is mostly used with computers."
  }
  ```

---

- **Error (400 BAD REQUEST)**:
  ```json
  {
    "number": 8,
    "error": true
  }
  ```

---

### Installation

- **Clone the Repo**: - git clone https://github.com/your-username/numb-app.git
- cd numb-app
- **Install Dependencies**:
- Install the required packages from **requirements.txt**:
  - pip install -r requirements.txt
- **Start the Development Server**:
  - python manage.py runserver

---

### Contributing

- **Contributions are welcome! If you'd like to contribute to this project, please follow these steps**:
  - Fork the repository.
  - Create a new branch for your feature or bugfix.
  - Commit your changes.
  - Submit a pull request.

---

## Hire Python Developers

Looking for skilled Python developers? Check out [HNG Hire](https://hng.tech/hire/python-developers) to find top talent for your projects.
