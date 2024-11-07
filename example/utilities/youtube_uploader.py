import os
import time
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import pickle

class YouTubeUploader:
    def __init__(self, credentials_file='client_secrets.json', token_file='token.pickle'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.credentials = None  # Store credentials here
        self.youtube = self.authenticate_youtube()

    def authenticate_youtube(self):
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]

        # Load token if available
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                self.credentials = pickle.load(token)

        # If no valid token, initiate OAuth flow
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, scopes)
                self.credentials = flow.run_local_server(port=0)

            # Save the credentials for future use
            with open(self.token_file, 'wb') as token:
                pickle.dump(self.credentials, token)

        # Initialize the YouTube API client with the saved credentials
        return build('youtube', 'v3', credentials=self.credentials)

    def upload_video(self, video_file_path, title, description, category_id, privacy_status):
        try:
            logging.info("Initializing YouTube upload...")
            youtube = build("youtube", "v3", credentials=self.credentials)
            request_body = {
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": category_id,
                },
                "status": {"privacyStatus": privacy_status},
            }

            # Configure MediaFileUpload for resumable upload with a specified chunk size
            media_body = MediaFileUpload(video_file_path, chunksize=1024 * 1024, resumable=True)
            request = youtube.videos().insert(
                part="snippet,status", body=request_body, media_body=media_body
            )

            # Initialize variables for tracking upload progress
            response = None
            retry_count = 0
            max_retries = 5
            start_time = time.time()

            logging.info("Starting video upload in chunks...")
            while response is None:
                try:
                    status, response = request.next_chunk()
                    if status:
                        logging.info(f"Upload progress: {int(status.progress() * 100)}% complete")
                except Exception as e:
                    if retry_count < max_retries:
                        retry_count += 1
                        logging.warning(f"Upload interrupted: {e}. Retrying ({retry_count}/{max_retries})...")
                        time.sleep(5)  # wait before retrying
                    else:
                        logging.error("Maximum retries reached. Upload failed.")
                        return None

            end_time = time.time()
            elapsed_time = end_time - start_time
            logging.info(f"Video upload completed successfully in {elapsed_time:.2f} seconds. Video ID: {response.get('id')}")

            return response.get("id")
        except Exception as e:
            logging.error(f"Error uploading video: {e}")
            return None
# Example usage
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize uploader
    uploader = YouTubeUploader(credentials_file='client_secrets.json')

    # Upload video
    video_path = "path/to/final_output_video.mp4"
    title = "Relaxing Sleep Video"
    description = "This is a relaxing video to help you sleep, with calming visuals and ambient sounds."
    category_id = "22"  # "People & Blogs" category
    privacy_status = "unlisted"  # Keep it unlisted until ready

    video_id = uploader.upload_video(video_path, title, description, category_id, privacy_status)
    if video_id:
        logging.info(f"Video uploaded and staged successfully with ID: {video_id}")
