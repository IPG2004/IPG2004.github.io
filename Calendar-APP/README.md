# Authentication System

This project is an authentication system that uses facial recognition and password authentication to allow users to register and log in. It is built using the `customtkinter` library for the user interface and `OpenCV` for face capture and recognition.

## Features

- User registration with username and password.
- Capture user faces during registration.
- Login with username, password, and facial recognition.
- User interface adaptable to different screen resolutions.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/IPG2004/Authentication-System.git
    cd Authentication-System
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) Install the package using `setup.py`:
    ```sh
    pip install .
    ```

## Usage

1. Run the application:
    ```sh
    python src/app.py
    ```

2. Follow the on-screen instructions to register and log in.

## Project Structure

```plaintext
Authentication-System/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
    ├── authentication.py
│   ├── face_recognition.py
│   └── data/
│       ├── __init__.py
│       └── content.txt
└── tests/
    ├── __init__.py
    ├── test_app.py
    ├── test_authentication.py
    └── test_face_recognition.py
```

- `src/`: Contains the main application code.
    - `app.py`: Module for the user interface.
    - `authentication.py`: Module for login an register system
    - `face_recognition.py`: Module for face recognition functionality.
    - `data/`: Directory to store captured user faces and login information.
- `tests/`: Contains test files.
    - `test_app.py`: Test cases for the application.
    - `test_authentication.py`:
    - `test_face_recognition.py`:

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) for more details.

## Credits

Made by [@IPG2004](https://github.com/IPG2004)