# Scheduling System

Appointment scheduler with automatic end-time and conflict prevention.

---

## Prerequisites

Make sure you have the following installed before setting up the project:

- [Python 3.10+](https://www.python.org/)
- [Node.js 16+](https://nodejs.org/)
- [Yarn](https://classic.yarnpkg.com/en/docs/install/)
- [MariaDB 10.6](https://mariadb.org/)
- [Redis](https://redis.io/)
- [Frappe Bench CLI](https://frappeframework.com/docs/v15/user/en/installation)
- [Pre-commit](https://pre-commit.com/) (for linting and formatting)

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app scheduling_system
```

---

## Usage

To create an appointment:

1. Open the **Appointment** doctype.
2. Enter the **start time**, **duration**, and **seller**.
3. The **end time** is automatically calculated.
4. The system prevents overlapping appointments and invalid datetimes.

---

## Validations

This app includes backend validations to ensure data integrity:

- **Start datetime cannot be in the past**

  ```
  Title: Invalid datetime  
  Message: Start datetime cannot be in the past.
  ```

- **Seller cannot have overlapping appointments**

  ```
  Title: Scheduling conflict  
  Message: This seller has an appointment from [start] to [end]. Please choose another time.
  ```

---

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/scheduling_system
pre-commit install
```

---

## License

MIT
