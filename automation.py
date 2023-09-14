from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Edge()

# Open the login page
# driver.get("file:///path_to_your_html_file/index.html")  # Replace with the actual path
driver.get("file:///C:/Users/Dell/Desktop/Python/Projects/Script/index.html")

# Find the username and password fields and submit button
username = driver.find_element("id", "username")
password = driver.find_element("id", "password")
login_button = driver.find_element("xpath", "//button[contains(text(),'Login')]")

# Replace 'your_username' and 'your_password' with your actual login credentials
username.send_keys("Satyajit")
password.send_keys("satya1")

# Click the login button
login_button.click()

# Wait for a moment to see the result
driver.implicitly_wait(100)

# Get the result element and print the text
result = driver.find_element("id", "result")
print(result.text)

# Close the browser
driver.quit()
