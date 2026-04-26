# 🖼️ AWS Image Labels Generator
A fast Boto3 Python script that takes images out of a s3 bucket and lists all objects found within each image. Uses Amazon Rekognition.

---

## 📋 Prerequisites

- Python 3.7+
- AWS Account
- AWS CLI v2
- IAM User with the following permissions:
  - `AmazonS3ReadOnlyAccess`
  - `AmazonRekognitionReadOnlyAccess`

---

## ⚙️ AWS Setup

### 1. Create an S3 Bucket
1. Go to the [AWS S3 Console](https://console.aws.amazon.com/s3)
2. Note your preferred region for later (e.g. `us-east-1`)
3. Leave **Block all public access** enabled

---

### 2. Create an IAM User
1. Go to the [AWS IAM Console](https://console.aws.amazon.com/iam)
2. Attach the following policies:
   - `AmazonS3ReadOnlyAccess`
   - `AmazonRekognitionReadOnlyAccess`
3. Create Access Key ID and Secret Access Key

---

### 3. Install & Configure AWS CLI
```bash
# macOS
brew install awscli

# Windows / Linux
pip install awscli
```

```bash
aws configure
```

Enter the necessary information. For default output:
```
Default output format: json
```

---

## 🚀 Running the Project

### 1. Clone the Repository
```bash
git clone https://github.com/GuiH823/AWSObjectDetection.git
cd AWSObjectDetection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Example Output
```
🔍 Scanning bucket: rekognition-images-yourname

Found 3 image(s). Running Rekognition...

📷 Image: dog-in-park.jpg
----------------------------------------
  ✅ Dog: 98.7%  (Category: Animal, Pet)
  ✅ Park: 95.2%  (Category: Outdoors)
  ✅ Grass: 91.4%  (Category: Plant)

✅ Results saved to rekognition_results.json
```

---

## 🧹 Cleanup
To avoid any ongoing AWS charges, delete your resources after use.

---

## 🛠️ Built With
- [Amazon Rekognition](https://aws.amazon.com/rekognition/) — AI-powered image analysis
- [Amazon S3](https://aws.amazon.com/s3/) — Cloud object storage
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) — AWS SDK for Python
- [AWS CLI](https://aws.amazon.com/cli/) — Command line interface for AWS
