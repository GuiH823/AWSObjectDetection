import boto3
import json
# import sys

# Configurations
BUCKET_NAME = 'rekognition-images-hansguillen'
REGION = 'us-east-1'
MAX_LABELS = 10
MIN_CONFIDENCE = 75

# initialize the aws clients
s3_client = boto3.client('s3', region_name = REGION)
rekognition_client = boto3.client('rekognition', region_name = REGION)


def list_images(bucket_name):
    """Lists all images in S3 bucket"""
    response = s3_client.list_objects_v2(Bucket = bucket_name)
    images = [obj['Key'] for obj in response.get('Contents', [])
              if obj['Key'].lower().endswith(('.jpg','.jpeg', '.png'))]
    return images

def detect_labels(bucket_name, image_key, max_labels=MAX_LABELS, min_confidence=MIN_CONFIDENCE):
    """
    Sends an image from S3 to Rekognition and returns detected labels.
    
    Args:
        bucket_name: name of S3 bucket
        image_key = File name/path of image in bucket
        max_labels: Maximum number of labels to return
        min_confidence: minimum confidence threshold
    """
    response = rekognition_client.detect_labels(
        Image = {
            'S3Object':{
                'Bucket': bucket_name,
                'Name': image_key
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence
    )
    return response['Labels']

def display_labels(image_key, labels):
    """Prints detected labels and confidence scores"""
    print(f"\n Image: {image_key}")
    print("-"*40)
    if not labels:
        print(" No labels detected above confidence threshold")
    for label in labels:
        confidence = label['Confidence']
        name = label['Name']
        # possible parent categories if they exist
        parents = ', '.join([p['Name'] for p in label.get('Parents', [])])
        parent_str = f"(Category: {parents})" if parents else ""
        print(f" {name}: {confidence: .1f}%{parent_str}")
    
def main():
    print(f" Scanning bucket: {BUCKET_NAME}\n")
    images = list_images(BUCKET_NAME)
    if not images:
        print("No images found in bucket")
        return

    print(f"Found {len(images)} image(s). Running Rekognition\n")

    all_results = {}

    for image_key in images:
        try:
            labels = detect_labels(BUCKET_NAME, image_key)
            display_labels(image_key, labels)
            all_results[image_key] = [{'Label': l['Name'], 'Confidence': round(l['Confidence'], 2)} for l in labels]
        except Exception as e:
            print(f" Error processing {image_key}: {e}")
    

    # save to json
    with open('rekognition_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print("\n Results saved to rekognition_results.json")

if __name__ == '__main__':
    main()