------------------------------

# Social Media Sentiment Analysis Dashboard BERT Based Approach

This project provides a **web-based dashboard** to analyze sentiment and user satisfaction for Instagram posts and comments. It leverages a **BERT-based approach** for sentiment analysis, making it capable of understanding the context of comments more effectively than traditional methods. The dashboard also includes user satisfaction metrics based on likes, replies, and sentiment classification.

The application includes two main dashboards:

1. **Instagram QoS Dashboard**: Analyzes Instagram comments and displays average sentiment and user satisfaction statistics.
2. **Twitter QoS Dashboard** (planned for future implementation): Will display similar metrics for Twitter comments.

### **Tech Stack**

* **Flask**: A lightweight web framework for Python used to build the web application.
* **Pandas**: A powerful data analysis and manipulation library for Python.
* **TextBlob & BERT**: A combination of TextBlob and a BERT-based approach for sentiment analysis, with BERT enhancing the sentiment detection capabilities.
* **HTML, CSS**: Used for front-end development to create a responsive, user-friendly dashboard.

---

## Project Structure

The project is organized in the following folder structure:

```
/social_media_sentiment_analysis
│
├── /app.py                # Main Flask application file
├── /analysis.py           # Sentiment analysis and satisfaction classification logic
├── /templates/
│   ├── dashboard.html     # Instagram dashboard HTML template
│   └── twitter_dashboard.html  # Twitter dashboard HTML template (future implementation)
├── /static/
│   └── style.css          # Custom CSS for dashboard styling
└── /data/
    └── Instagram-datasets.csv  # Instagram dataset for analysis
```

---

## Requirements

To run the project, install the following dependencies:

* **Flask**: `pip install flask`
* **Pandas**: `pip install pandas`
* **TextBlob**: `pip install textblob`
* **transformers**: `pip install transformers` (for BERT-based sentiment analysis)
* **torch**: `pip install torch` (required for BERT)

---

## Setup

1. Clone or download the project files.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have the dataset file:

   * `Instagram-datasets.csv`: This file contains Instagram comments data, located in the `data/` folder.

   **Instagram Dataset Columns**:

   * **comment**: The comment text.
   * **likes\_number**: The number of likes on the comment.
   * **replies\_number**: The number of replies to the comment.
   * **comment\_user**: Username of the user who made the comment.
   * **comment\_date**: Date when the comment was posted.

---

## Running the Application

1. Open a terminal and navigate to the project directory.
2. Run the Flask application:

   ```bash
   python app.py
   ```
3. Open your browser and visit:

   ```
   http://localhost:5000/
   ```

   This will load the **Instagram QoS Dashboard**, displaying:

   * **Average Sentiment**: The average sentiment score calculated for all Instagram comments.
   * **Satisfaction Statistics**: A breakdown of comments classified as 'Positive', 'Neutral', or 'Negative' based on sentiment and engagement (likes and replies).

---

## Explanation of the Output

The Instagram dashboard provides an analysis of the comments based on the following metrics:

1. **Average Sentiment**:

   * This score reflects the overall sentiment of the comments. It is calculated using a **BERT-based approach** combined with **TextBlob**'s sentiment analysis, which allows for more accurate understanding of the context and nuances in the comments. The sentiment polarity score ranges from `-1` (negative) to `1` (positive), with `0` indicating neutral sentiment.
2. **Satisfaction Statistics**:

   * Comments are classified into three categories: **Positive**, **Neutral**, and **Negative**. The classification is based on a combination of sentiment score, the number of **likes**, and **replies**.

     * **Positive**: Comments with high sentiment scores and a relatively higher number of likes and replies.
     * **Neutral**: Comments with a sentiment score close to `0`, indicating neutral sentiment.
     * **Negative**: Comments with low sentiment scores and lower engagement.

   The dashboard shows the count of comments falling into each satisfaction category.

---

## Instagram CSV Implementation

The core functionality for Instagram sentiment analysis involves reading the dataset from the CSV file `Instagram-datasets.csv`. The steps involved are:

1. **Reading the CSV File**: The file is read using **Pandas** to load the dataset into a DataFrame.

2. **Data Cleaning**:

   * Renaming columns for consistency.
   * Dropping rows with missing comments to ensure accuracy in analysis.

3. **Sentiment Analysis**:

   * Using a **BERT-based approach** for sentiment analysis, which is more powerful and context-aware compared to traditional methods. We use the **Transformers** library to load a pre-trained BERT model, which is fine-tuned for sentiment classification.

   * Additionally, **TextBlob** can still be used for additional simplicity in combining the two techniques, but the BERT model enhances the overall sentiment analysis performance.

4. **Satisfaction Classification**:

   * Based on the sentiment score, number of likes, and replies, comments are classified into **Positive**, **Neutral**, or **Negative** categories.

5. **Displaying Results**:

   * The calculated **average sentiment** and **satisfaction statistics** are passed to the `dashboard.html` template, which renders the results in the web interface.

---

## Sample Instagram CSV Format

The `Instagram-datasets.csv` file should have the following columns:

| comment                  | likes\_number | replies\_number | comment\_user | comment\_date | ... |
| ------------------------ | ------------- | --------------- | ------------- | ------------- | --- |
| "Great post!"            | 120           | 10              | user1         | 2025-05-01    | ... |
| "This is amazing!"       | 200           | 15              | user2         | 2025-05-02    | ... |
| "Not bad, could improve" | 50            | 5               | user3         | 2025-05-03    | ... |

---

## Future Implementation

1. **Twitter QoS Dashboard**:

   * The logic for Twitter analysis will be similar to Instagram, but with Twitter-specific datasets (e.g., likes, retweets, and replies).
2. **Data Visualizations**:

   * Enhance the dashboard by adding **charts** and **graphs** (e.g., pie charts for satisfaction breakdown, bar charts for sentiment distribution).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---


![image](https://github.com/user-attachments/assets/dcac852a-a75e-41e6-8a39-96101c0d2d6b)


