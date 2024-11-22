import requests
import zipfile
import os
import sys

# URL of the zip file
url = "https://www.accessdata.fda.gov/cder/ndctext.zip"

# Directory to save the unzipped files
output_dir = "ndctext_files"

# Expected manifest based on the uploaded sample
expected_manifest = {"package.txt", "product.txt"}

# Fetching the zip file from the URL
response = requests.get(url)

# Saving the zip file to a temporary location
downloaded_zip_path = "downloaded_ndctext.zip"
with open(downloaded_zip_path, "wb") as f:
    f.write(response.content)


# Get the manifest of the downloaded zip file
def get_zip_manifest(zip_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        return set(zip_ref.namelist())


# Get the manifest of the downloaded zip file
downloaded_manifest = get_zip_manifest(downloaded_zip_path)

# Verify that the manifests match
if downloaded_manifest == expected_manifest:
    # Unzipping the downloaded file silently
    with zipfile.ZipFile(downloaded_zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)
else:
    print("The manifests do not match.")
    print("Downloaded manifest:", downloaded_manifest)
    print("Expected manifest:", expected_manifest)
    sys.exit(1)

# Move the files to the root directory
os.replace(f"{output_dir}/package.txt", "package.txt")
os.replace(f"{output_dir}/product.txt", "product.txt")
