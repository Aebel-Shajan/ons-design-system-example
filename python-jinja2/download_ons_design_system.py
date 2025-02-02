"""
Script to download and extract the ONS design system nunjuck components for use with 
flask & jinja2.
"""
import requests
import zipfile
import io


def download_and_extract_latest_zip(repo, asset_name, output_folder):
    """
    Downloads and extracts the latest ZIP file from a GitHub repository release.
    
    Args:
        repo (str): GitHub repository in the format "owner/repo".
        asset_name (str): The name of the ZIP file in the release assets.
        output_folder (str): The folder to extract the contents into.
    Returns:
        None
    Raises:
        requests.exceptions.RequestException: If there is an issue with the network 
            request.
        zipfile.BadZipFile: If the downloaded file is not a valid ZIP file.
    """
    github_api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    
    response = requests.get(github_api_url)
    print(response)
    if response.status_code != 200:
        print(f"Error: Unable to fetch latest release details for {repo}")
        return
    
    release_data = response.json()
    release_tag = release_data.get("tag_name", "unknown")
    
    # Find the asset URL
    asset_url = None
    for asset in release_data.get("assets", []):
        if asset["name"] == asset_name:
            asset_url = asset["browser_download_url"]
            break
    
    if not asset_url:
        print(f"Error: Asset '{asset_name}' not found in latest release {release_tag}")
        return
    
    # Download the ZIP file
    print(f"Downloading {asset_name} from release {release_tag}...")
    zip_response = requests.get(asset_url, stream=True)
    if zip_response.status_code != 200:
        print("Error: Unable to download the ZIP file.")
        return
    
    # Extract the ZIP file
    with zipfile.ZipFile(io.BytesIO(zip_response.content)) as zip_ref:
        zip_ref.extractall(output_folder)
    
    print(f"Successfully extracted {asset_name} to {output_folder}")


if __name__ == '__main__':    
    download_and_extract_latest_zip(
        repo="ONSdigital/design-system",
        asset_name="templates.zip", 
        output_folder="./"
    )
