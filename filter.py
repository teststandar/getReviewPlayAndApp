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
        # date_format = "%Y-%m-%d %H:%M:%S"
        review_date = datetime.strptime(review['attributes']['createdDate'], date_format)
        
        # Check if the review date is within the specified range
        if start_date_7 <= review_date <= end_date_7:
            filtered_review = {
                "Author": review['attributes']['reviewerNickname'],
                "Rating": review['attributes']['rating'],
                "Title": review['attributes']['title'],
                "Review": review['attributes']['body'],
                "Territory": review['attributes']['territory'],
                "Date": review['attributes']['createdDate'],
                "Date": datetime.strptime(review['attributes']['createdDate'], date_format).strftime("%Y-%m-%d %H:%M:%S")
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
                "Reply Review": review['replyContent'],
                "Reply Date": review['repliedAt'],
                "App Version": review['appVersion'],
            }
            filtered_reviews.append(filtered_review)

    return filtered_reviews

def filter_reviews_by_date_andro2(reviews, start_date, end_date):
    start_date1 = datetime.strptime(start_date, "%Y-%m-%d")
    end_date1 = datetime.strptime(end_date, "%Y-%m-%d")
    timezone_utc_plus_7 = pytz.timezone('Asia/Bangkok')
    start_date_7 = timezone_utc_plus_7.localize(start_date1)
    end_date_7 = timezone_utc_plus_7.localize(end_date1)
    
    filtered_reviews = []
    for review in reviews:
        comments = review.get('comments', [0])
        comment = comments[0]
        user_comment = comment.get('userComment', {})
        text = user_comment.get('text', '')
        star_rating = user_comment.get('starRating', 'No rating')
        last_modified = user_comment.get('lastModified', {}).get('seconds', 'No date')
        # for comment in comments:
        #     user_comment = comment.get('userComment', {})
        #     text = user_comment.get('text', '')
        #     star_rating = user_comment.get('starRating', 'No rating')
        #     last_modified = user_comment.get('lastModified', {}).get('seconds', 'No date')
        # if review.get('comments', [1]) is not None:
        if len(comments) > 1:
            comment_2 = comments[1]
            developer_comment = comment_2.get('developerComment', {})
            replyContent = developer_comment.get('text', '')
            repliedAt = developer_comment.get('lastModified', {}).get('seconds', 'No date')
            dt_object_dev = datetime.fromtimestamp(int(repliedAt))
        else:
            replyContent = None
            dt_object_dev = None

        if last_modified == "No date":
            filtered_review = {
                "Author": review.get('authorName', 'Unknown'),
                "Rating": star_rating,
                "Review": text,
                "Date": last_modified,
                "Reply Review": replyContent,
                "Reply Date": dt_object_dev,
                "App Version" : user_comment.get('appVersionName', ''),
            }
            filtered_reviews.append(filtered_review)
        else:
            dt_object = datetime.fromtimestamp(int(last_modified))
            dateString = str(dt_object)
            date_format = "%Y-%m-%d %H:%M:%S"
            review_date = datetime.strptime(dateString, date_format)
            review_date_7 = timezone_utc_plus_7.localize(review_date)
            if start_date_7 <= review_date_7 <= end_date_7:
                filtered_review = {
                    "Author": review.get('authorName', 'Unknown'),
                    "Rating": star_rating,
                    "Review": text,
                    "Date": dt_object,
                    "Reply Review": replyContent,
                    "Reply Date": dt_object_dev,
                    "App Version" : user_comment.get('appVersionName', ''),
                }
                filtered_reviews.append(filtered_review)
                    

    return filtered_reviews

def filter_reviews_ios_pd(reviews):
    filtered_reviews = []
    for review in reviews:
        date_format = "%Y-%m-%dT%H:%M:%S%z"
        filtered_review = {
            "OS": "IOS",
            "APP": "PD",
            "Author": review['attributes']['reviewerNickname'],
            "Rating": review['attributes']['rating'],
            "Review": review['attributes']['body'],
            "Date": datetime.strptime(review['attributes']['createdDate'], date_format).strftime("%Y-%m-%d %H:%M:%S")
        }
        filtered_reviews.append(filtered_review)
    return filtered_reviews

def filter_reviews_ios_pds(reviews):
    filtered_reviews = []
    for review in reviews:
        date_format = "%Y-%m-%dT%H:%M:%S%z"
        filtered_review = {
            "OS": "IOS",
            "APP": "PDS",
            "Author": review['attributes']['reviewerNickname'],
            "Rating": review['attributes']['rating'],
            "Review": review['attributes']['body'],
            "Date": datetime.strptime(review['attributes']['createdDate'], date_format).strftime("%Y-%m-%d %H:%M:%S")
        }
        filtered_reviews.append(filtered_review)
    return filtered_reviews

def filter_reviews_andro_pd(reviews):
    filtered_reviews = []
    for review in reviews:
        filtered_review = {
            "OS": "ANDROID",
            "APP": "PD",
            "Author": review['userName'],
            "Rating": review['score'],
            "Review": review['content'],
            "Date": datetime.strptime(str(review['at']), "%Y-%m-%d %H:%M:%S")
           }
        filtered_reviews.append(filtered_review)
    return filtered_reviews

def filter_reviews_andro_pds(reviews):
    filtered_reviews = []
    for review in reviews:
        filtered_review = {
            "OS": "ANDROID",
            "APP": "PDS",
            "Author": review['userName'],
            "Rating": review['score'],
            "Review": review['content'],
            "Date": datetime.strptime(str(review['at']), "%Y-%m-%d %H:%M:%S")
           }
        filtered_reviews.append(filtered_review)
    return filtered_reviews