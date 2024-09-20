import time
from selenium import webdriver

def like_tweets(username, keyword):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/" + username)

    # Find all tweets that contain the keyword
    tweets = driver.find_elements_by_xpath("//p[@class='tweet-text']")
    for tweet in tweets:
        if keyword in tweet.text:
            # Click the "Like" button
            tweet.find_element_by_xpath("//div[@class='like-button']/span").click()

    # Wait 5 seconds before liking more tweets
    time.sleep(5)

if __name__ == "__main__":
    username = "example_username"
    keyword = "example_keyword"

    like_tweets(username, keyword)
