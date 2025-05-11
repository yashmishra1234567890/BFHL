import requests
import json
import os

def main():
    # User details
    name = "Yash Mishra"
    reg_no = "0827AL221150"
    email = "yashmishra221057@acropolis.in"  
    
    print("Bajaj Finserv Health API Challenge")
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Registration Number: {reg_no}")
    print(f"Email: {email}")
   
    
    gen_response = requests.post(
        "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
        json={
            "name": name,
            "regNo": reg_no,
            "email": email
        }
    )

    if gen_response.status_code != 200:
        print("Failed to generate webhook:", gen_response.text)
        return

    response_data = gen_response.json()
    access_token = response_data.get("accessToken")
    webhook_url = response_data.get("webhookUrl")  
    
    if not access_token or not webhook_url:
        print("Missing access token or webhook URL")
        return

    print("Webhook and AccessToken received successfully.")
    print(f"Access Token: {access_token}")
    print(f"Webhook URL: {webhook_url}")

   
    last_digit = int(reg_no[-1])
    if last_digit % 2 == 0:
        question = "Question 2"
        question_link = "https://drive.google.com/file/d/1pO1ZvmDqAZJv7TXRYsVben11Wp2HVb/view?usp=sharing"
    else:
        question = "Question 1"
        question_link = "https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing"

    print(f"\nYou are assigned: {question}")
    print("Question Link:", question_link)
    
    
    try:
        with open("solution.sql", "r") as file:
            final_sql_query = file.read().strip()
    except Exception as e:
        print(f"Error reading solution.sql: {e}")
        return
        
    print("SQL solution loaded successfully.")
    print("\nSQL Query:")
    print("-" * 50)
    print(final_sql_query)
    print("-" * 50)
    
    if not final_sql_query or "your_table" in final_sql_query:
        print("\nPlease update 'solution.sql' with your actual SQL solution.")
        return

    
    test_response = requests.post(
        "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON",
        headers={
            "Authorization": f"Bearer {access_token}",  
            "Content-Type": "application/json"
        },
        json={
            "finalQuery": final_sql_query
        }
    )

    if test_response.status_code == 200:
        print("✅ Submission successful!")
        print("\nAPI Response:")
        print("-" * 50)
        print(json.dumps(test_response.json(), indent=2))
        print("-" * 50)
    else:
        print(" Submission failed:")
        print(f"Status Code: {test_response.status_code}")
        print(f"Response: {test_response.text}")

if __name__ == "__main__": 
    main()
