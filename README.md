# Visited Cities

**CS178: Cloud and Database Systems — Project #1**
**Author:** Clayton Gustafson
**GitHub:** cpgus485

---

## Overview

With this project, I wanted to list out cities that the user has visited. The user can continue to update and view the list as they visit more cities, and they can look at all of the major cities in the database.

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **AWS DynamoDB** — non-relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page
│   ├── add_city.html     # Add city and visit number to database
│   ├── delete_city.html     # Delete a visited city
│   ├── display_visited_cities.html     # Display all visited cities
│   ├── update_city.html     # Update a visited city
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://ec2-3-215-73-35.compute-1.amazonaws.com:8080/
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->
My database consists of a table for cities and information related to the city, as well as a table for countries and information related to the country. The key relationship is between countrycode in the Cities table and code in the Countries table.

**Example:**

- `Cities` — stores City Name and City Population; primary key is `countrycode`
- `Country` — stores Country Name and Continent Name; foreign key links to `code`

The JOIN query used in this project: <!-- describe it in plain English -->
This project connects the Cities table to the Countries table based on the countrycode of the City.

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

My DynamoDB table keeps track of the cities that the user has visited, and how many times the user has visited it. The partition key is City, and it has the attribute of Visits. The user can create, update, or delete a city in this database, and it can read all of the cities they have visited.

- **Table name:** `Cities_Visited`
- **Partition key:** `Cities`
- **Used for:** Keeping track of the number of times the user has visited a city.

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/[add-city]` | Add a city to the database |
| Read      | `/[display-visited-cities]` | Display all of the visited cities |
| Update    | `/[update-city]` | Update the visit number of a city |
| Delete    | `/[delete-city]` | Delete a visited city |

---

## Challenges and Insights

<!-- What was the hardest part? What did you learn? Any interesting design decisions? -->
The hardest part of this project was getting my DynamoDB table to be output correctly. I had to make sure the html file was iterating through the dictionaries correctly, and not just outputting the whole dictionary in each cell. I had to play around with some different ways to iterate through, and was able to use ChatGPT to help me find the correct way to display the items.

---

## AI Assistance

<!-- List any AI tools you used (e.g., ChatGPT) and briefly describe what you used them for. Per course policy, AI use is allowed but must be cited in code comments and noted here. -->

When I ran into errors, I used ChatGPT to help me understand the error codes and locate the errors within my documents.
