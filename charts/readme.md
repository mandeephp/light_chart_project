## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mandeephp/light_chart_project.git
    cd light_chart_project
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

- Open your browser and go to `http://127.0.0.1:8000/` to access the application.