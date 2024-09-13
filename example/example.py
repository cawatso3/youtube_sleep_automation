import logging
import time
import os
import replicate
import requests
from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
from pydub import AudioSegment



class ExampleShell:
    def __init__(self, configs):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        # Start timer
        start_time = time.time()
        logging.info("Starting ExampleShell...")

        # Create a new directory for this run
        # self.output_dir = self.create_output_directory()

        # authenticate replicate api
        # self.replicate_token = os.getenv('REPLICATE_API_TOKEN')

        # Initialize Replicate API client
        # self.replicate_client = replicate.Client(api_token=self.replicate_token)


        # MY CODE HERE

        # Generate music and video, download them, and store links
        # self.process_audio_and_video()

        # Define paths to your input and output files
        input_audio_path = "out.mp3"
        output_audio_path = "looped_audio.mp3"

        # Loop the input audio file
        loop_count = 2  # Number of loops
        crossfade_duration = 1000  # 2 seconds of crossfade

        # Call the function to loop the audio
        self.loop_audio_smoothly(input_audio_path, output_audio_path, loop_count, crossfade_duration)


        # End SHELL Timer
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"ExampleShell completed in {elapsed_time:.2f} seconds.")

    @staticmethod
    def combine_video_audio(video_path, audio_path, output_path):
        """
        Combine video and audio files into a single output file using moviepy.

        :param video_path: Path to the input video file (e.g., .mp4).
        :param audio_path: Path to the input audio file (e.g., .mp3).
        :param output_path: Path to the output file where the combined video/audio will be saved.
        """
        try:
            # Load video and audio files
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            # Set the audio to the video
            final_video = video_clip.set_audio(audio_clip)

            # Write the final video to the output file
            final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

            print(f"Video and audio combined successfully! Output saved at: {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def create_output_directory():
        # Create a unique folder name based on the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_dir = os.path.join(os.getcwd(), f"output_{timestamp}")

        # Create the directory
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Created directory: {output_dir}")
        return output_dir

    @staticmethod
    def download_audio_file(url, file_name):
        try:
            logging.info(f"Downloading audio file from {url}...")

            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Write the content to a local file
            with open(file_name, 'wb') as file:
                file.write(response.content)

            logging.info(f"File downloaded successfully and saved as {file_name}")
            print(f"File downloaded successfully and saved as {file_name}")

        except Exception as e:
            logging.error(f"An error occurred while downloading the audio file: {e}")

    @staticmethod
    def download_video_file(url, file_name):
        try:
            logging.info(f"Downloading video file from {url}...")

            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Write the content to a local file
            with open(file_name, 'wb') as file:
                file.write(response.content)

            logging.info(f"File downloaded successfully and saved as {file_name}")
            print(f"File downloaded successfully and saved as {file_name}")

        except Exception as e:
            logging.error(f"An error occurred while downloading the video file: {e}")

    @staticmethod
    def generate_music_from_text():
        try:
            logging.info("Generating music using Replicate API...")

            # Replace with your actual model ID and inputs
            output = replicate.run(
                "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
                input={
                    "top_k": 250,
                    "top_p": 0,
                    "prompt": "Calm and soothing ambient music with deep, resonant bass tones, soft ethereal synths, and gentle atmospheric pads. The music is slow-paced, with smooth transitions, no drums or percussion, ideal for relaxation, meditation, and sleep.",
                    "duration": 25,
                    "input_audio": "https://drive.google.com/uc?export=download&id=1FrahV--dilDQKSpcCrPg0k8EsSCuY9_i",
                    "temperature": 1,
                    "continuation": False,
                    "model_version": "stereo-melody-large",
                    "output_format": "mp3",
                    "continuation_start": 0,
                    "multi_band_diffusion": False,
                    "normalization_strategy": "peak",
                    "classifier_free_guidance": 3
                }
            )
            logging.info("audio url: ", output)
            return output

        except Exception as e:
            logging.error(f"An error occurred while generating music: {e}")
            return None


    @staticmethod
    def generate_video_from_text():
        logging.info("Generating music using Replicate API...")
        try:
            output = replicate.run(
                "deforum/deforum_stable_diffusion:e22e77495f2fb83c34d5fae2ad8ab63c0a87b6b573b6208e1535b23b89ea66d6",
                input={
                    "zoom": "0: (1.01)",  # Slight zoom to create a gentle sense of movement
                    "angle": "0:(0.1)",  # Minimal angle to maintain stability
                    "sampler": "klms",  # Sampler for high-quality output
                    "max_frames": 100,  # Length of the video, must be >= 100 and <= 1000
                    "translation_x": "0: (0)",  # No horizontal translation
                    "translation_y": "0: (0)",  # No vertical translation
                    "color_coherence": "Match Frame 0 LAB",  # Ensures color consistency
                    "animation_prompts": (
                         "0: masterpiece, best quality, atmospheric, futuristic, cosmos, night sky, stars, galaxies, calm "
                    )
                }
            )
            print(output)
            return output
        except Exception as e:
            logging.error(f"An error occurred while generating Video: {e}")
            return None

    @staticmethod
    def loop_audio_smoothly(audio_path, output_path, loop_count=3, crossfade_duration=2000):
        """
        Loop an audio file with smooth crossfade transitions between loops.

        :param audio_path: Path to the input audio file.
        :param output_path: Path where the looped audio will be saved.
        :param loop_count: Number of times to loop the audio.
        :param crossfade_duration: Duration (in milliseconds) of the crossfade between loops.
        """
        try:
            # Load the audio file
            audio = AudioSegment.from_file(audio_path)

            # Loop the audio smoothly with crossfade
            looped_audio = audio
            for _ in range(loop_count - 1):
                looped_audio = looped_audio.append(audio, crossfade=crossfade_duration)

            # Export the final looped audio to the output path
            looped_audio.export(output_path, format="mp3")

            print(f"Looped audio created successfully! Output saved at: {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def process_audio_and_video(self):
        # Generate music (audio)
        output_audio_url = self.generate_music_from_text()

        # Download the generated audio file
        if output_audio_url:
            audio_file_path = os.path.join(self.output_dir, "output_audio.mp3")
            self.download_audio_file(output_audio_url, audio_file_path)

        # Generate video
        output_video_url = self.generate_video_from_text()

        # Download the generated video file
        if output_video_url:
            video_file_path = os.path.join(self.output_dir, "output_video.mp4")
            self.download_video_file(output_video_url, video_file_path)

        # Combine video and audio into a single file
        output_combined_path = os.path.join(self.output_dir, "final_output_with_audio.mp4")
        self.combine_video_audio(video_file_path, audio_file_path, output_combined_path)

        # Store the output URLs in a file (if necessary)
        self.store_output_links(output_audio_url, output_video_url)

    def store_output_links(self, audio_url, video_url):
        try:
            logging.info("Storing output links...")

            # Define the file path
            links_file_path = os.path.join(self.output_dir, "output_links.txt")

            # Write the URLs to the file
            with open(links_file_path, 'w') as file:
                file.write(f"Audio URL: {audio_url}\n")
                file.write(f"Video URL: {video_url}\n")

            logging.info(f"Output links stored successfully in {links_file_path}")
            print(f"Output links stored successfully in {links_file_path}")

        except Exception as e:
            logging.error(f"An error occurred while storing the output links: {e}")







