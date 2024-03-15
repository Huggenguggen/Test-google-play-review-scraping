import csv
import json

def convert_to_csv(json_data, csv_filename):
    results = json_data['results']['data']
    fieldnames = ['id', 'userName', 'userImage', 'date', 'score', 'scoreText', 'url', 'title', 'text', 'replyDate', 'replyText', 'version', 'thumbsUp', 'criterias']

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for review in results:
            writer.writerow({
                'id': review.get('id', ''),
                'userName': review.get('userName', ''),
                'userImage': review.get('userImage', ''),
                'date': review.get('date', ''),
                'score': review.get('score', ''),
                'scoreText': review.get('scoreText', ''),
                'url': review.get('url', ''),
                'title': review.get('title', ''),
                'text': review.get('text', ''),
                'replyDate': review.get('replyDate', ''),
                'replyText': review.get('replyText', ''),
                'version': review.get('version', ''),
                'thumbsUp': review.get('thumbsUp', ''),
                'criterias': review.get('criterias', '')
            })


def convert_to_csv_2(json_data, csv_filename):
    results = json_data['data']
    fieldnames = ['id', 'userName', 'userImage', 'date', 'score', 'scoreText', 'url', 'title', 'text', 'replyDate', 'replyText', 'version', 'thumbsUp', 'criterias']

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for review in results:
            writer.writerow({
                'id': review.get('id', ''),
                'userName': review.get('userName', ''),
                'userImage': review.get('userImage', ''),
                'date': review.get('date', ''),
                'score': review.get('score', ''),
                'scoreText': review.get('scoreText', ''),
                'url': review.get('url', ''),
                'title': review.get('title', ''),
                'text': review.get('text', ''),
                'replyDate': review.get('replyDate', ''),
                'replyText': review.get('replyText', ''),
                'version': review.get('version', ''),
                'thumbsUp': review.get('thumbsUp', ''),
                'criterias': review.get('criterias', '')
            })

def load_json_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    json_data = load_json_from_file('./data/google_reviews.json')
    convert_to_csv(json_data, './data/google_reviews.csv')
    json_data = load_json_from_file('./data/api_reviews.json')
    convert_to_csv_2(json_data, './data/api_reviews.csv')