# GitHub Topics and Repositories Scraper

This Python script is designed to extract valuable information about GitHub topics and their top repositories. It provides a comprehensive overview of both the topics and the repositories within those topics.

## Overview

The script performs the following tasks:

1. **Scrape GitHub Topics:**
    - Extracts information about GitHub topics, including titles, descriptions, and URLs.
    - Utilizes BeautifulSoup and requests to parse the HTML content of the GitHub Topics page.

2. **Scrape Top Repositories within Topics:**
    - For each GitHub topic, the script navigates to the topic's page and extracts details about the top repositories.
    - The information includes the username, repository name, stars, and repository URL.

3. **Data Storage:**
    - Organizes the scraped data into a structured format.
    - Stores information about GitHub topics in a DataFrame, including titles, descriptions, and URLs.
    - For each topic, creates a CSV file in the `data` directory containing details of the top repositories.

