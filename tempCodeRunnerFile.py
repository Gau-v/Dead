from selenium import webdriver
driver = webdriver.Chrome()

# Set the path to the webdriver executable
webdriver_path = '/path/to/webdriver'

# Create a new instance of the webdriver
driver = webdriver.Chrome(webdriver_path)

# Navigate to the desired webpage
driver.get('https://www.youtube.com')

# Perform web scraping operations using Selenium commands
# ...

# Close the webdriver
driver.quit() driver = webdriver.Chrome()