import pytz
from datetime import datetime

def filter_reviews_by_date_ios(reviews, start_date, end_date):
    start_date1 = datetime.strptime(start_date, "%Y-%m-%d")
    end_date1 = datetime.strptime(end_date, "%Y-%m-%d")
    timezone_utc_plus_7 = pytz.timezone('Asia/Bangkok')
    start_date_7 = timezone_utc_plus_7.localize(start_date1)
    end_date_7 = timezone_utc_plus_7.localize(end_date1)
    
    filtered_reviews = []
    for review in reviews:
        date_format = "%Y-%m-%dT%H:%M:%S%z"
        review_date = datetime.strptime(review['attributes']['createdDate'], date_format)
        
        # Check if the review date is within the specified range
        if start_date_7 <= review_date <= end_date_7:
            filtered_review = {
                "Author": review['attributes']['reviewerNickname'],
                "Rating": review['attributes']['rating'],
                "Review": review['attributes']['body'],
                "Date": review['attributes']['createdDate'],
            }
            filtered_reviews.append(filtered_review)

    return filtered_reviews

def filter_reviews_by_date_andro(reviews, start_date, end_date):
    start_date1 = datetime.strptime(start_date, "%Y-%m-%d")
    end_date1 = datetime.strptime(end_date, "%Y-%m-%d")
    timezone_utc_plus_7 = pytz.timezone('Asia/Bangkok')
    start_date_7 = timezone_utc_plus_7.localize(start_date1)
    end_date_7 = timezone_utc_plus_7.localize(end_date1)
    
    filtered_reviews = []
    for review in reviews:
        date_format = "%Y-%m-%d %H:%M:%S"
        dateString = str(review['at'])
        review_date = datetime.strptime(dateString, date_format)
        review_date_7 = timezone_utc_plus_7.localize(review_date)
        
        # Check if the review date is within the specified range
        if start_date_7 <= review_date_7 <= end_date_7:
            filtered_review = {
                "Author": review['userName'],
                "Rating": review['score'],
                "Review": review['content'],
                "Date": review['at'],
            }
            filtered_reviews.append(filtered_review)

    return filtered_reviews