import logging
import shutil
import time
import os
from datetime import datetime
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, concatenate_videoclips, ColorClip, AudioFileClip
# from moviepy.video.fx.all import loop
import random

from example.utilities.youtube_uploader import YouTubeUploader
from example.utilities.logic_pro import LogicProAutomation

class ExampleShell:
    def __init__(self, configs, debug=True, duration_hours=0.5):
        #30 min = 0.5
        # 1 min duration = 0.0166
        # 30-sec duration = 0.0083

        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.debug = debug
        self.output_dir = os.path.abspath(self.create_output_directory())
        self.music_dir = "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/music"

        self.video_dir = "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/videos"
        self.duration_hours = duration_hours  # Customizable duration in hours
        self.logic_pro_automation = LogicProAutomation("example/utilities/logic_pro_loop_and_bounce.scpt")  # Path to Logic Pro script

        self.main()

    def main(self):
        start_time = time.time()
        logging.info("Starting YouTube Shell...")

        try:
            # Step 1: Prepare music file
            music_file = self.get_music_file()
            looped_audio_path = os.path.join(self.output_dir, "looped_audio.mp3")
            logging.info("LogicPro: Looping audio with crossfade...")

            # Run Logic Pro automation, passing the music file and dynamic output directory
            self.logic_pro_automation.run_automation(target_folder=self.music_dir, save_to_folder=self.output_dir)

            logging.info(f"Looped audio saved at: {looped_audio_path}")

            # Step 2: Prepare video file
            video_file = self.get_video_file()
            output_video_path = os.path.join(self.output_dir, "final_output_video.mp4")
            logging.info(f"Creating video for {self.duration_hours} hours...")
            self.create_video_with_black_screen(video_file, looped_audio_path, output_video_path, duration_hours=self.duration_hours)
            logging.info(f"Video created and saved at: {output_video_path}")

            # Step 3: Archive used files
            logging.info("Moving used music and video files to output directory for archival...")
            self.cleanup_directories(music_file, video_file)

            # Step 4: Upload to YouTube
            logging.info("Step 4: Uploading video to YouTube...")
            self.upload_to_youtube(output_video_path)

        except Exception as e:
            logging.error(f"An error occurred in the pipeline: {e}")
        finally:
            elapsed_time = time.time() - start_time
            logging.info(f"ExampleShell completed in {elapsed_time:.2f} seconds.")

    def create_output_directory(self):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_dir = os.path.join(os.getcwd(), f"output_{timestamp}")
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Created output directory: {output_dir}")
        return output_dir

    def get_music_file(self):
        try:
            music_files = [f for f in os.listdir(self.music_dir) if f.endswith(('.mp3', '.wav'))]
            if not music_files:
                raise FileNotFoundError(f"No supported music files found in {self.music_dir}.")
            selected_file = os.path.join(self.music_dir, music_files[0])
            logging.info(f"Selected music file: {selected_file}")
            return selected_file
        except Exception as e:
            logging.error(f"Failed to retrieve music file: {e}")
            raise

    def get_video_file(self):
        try:
            files = os.listdir(self.video_dir)
            if not files:
                raise FileNotFoundError("No video files found in the video directory.")
            selected_file = os.path.join(self.video_dir, files[0])
            logging.info(f"Selected video file: {selected_file}")
            return selected_file
        except Exception as e:
            logging.error(f"Failed to retrieve video file: {e}")
            raise

    def create_video_with_black_screen(self, video_file, audio_path, output_video_path, duration_hours):
        """
        Create a video with an intro, an initial looped segment covering the audio duration,
        followed by a black screen if necessary.

        Parameters:
        - video_file (str): Path to the main video file to loop.
        - audio_path (str): Path to the audio file.
        - output_video_path (str): Path where the final video will be saved.
        - duration_hours (float): Desired total duration of the video in hours.
        - buffer_duration (float): Duration of the buffer in seconds between intro and main video.
        """
        try:
            # Load intro video
            intro_path = "/Users/mac/PycharmProjects/staging_files/intro_video/Welcome.mp4"
            intro_clip = VideoFileClip(intro_path)

            # Load the main video and check dimensions without resizing
            video_clip = VideoFileClip(video_file)

            # Calculate the total desired duration in seconds
            total_duration = duration_hours * 60 * 60

            # Load audio and determine its duration
            audio_clip = AudioFileClip(audio_path)
            audio_duration = audio_clip.duration

            # Calculate loop duration to cover audio duration, minus intro and buffer
            loop_duration = min(total_duration, audio_duration) - intro_clip.duration
            if loop_duration <= 0:
                logging.warning("Intro and buffer duration exceed or match the specified total duration.")
                # Use only the intro clip trimmed to total_duration
                main_video_with_intro = intro_clip.subclip(0, total_duration).set_audio(audio_clip)
                black_screen_duration = 0
            else:
                # Loop the main video to cover the audio duration
                num_loops = int(loop_duration / video_clip.duration) + 1
                logging.info("Creating looped video segment to match audio duration...")
                looped_video = concatenate_videoclips([video_clip] * num_loops).subclip(0, loop_duration)

                # Concatenate intro, buffer, and looped main video, then set audio
                main_video_with_intro = concatenate_videoclips([intro_clip, looped_video]).set_audio(
                    audio_clip)

                # Calculate any remaining time to fill with a black screen
                black_screen_duration = total_duration - main_video_with_intro.duration

            # Create a black screen for any remaining duration
            if black_screen_duration > 0:
                black_screen = ColorClip(size=video_clip.size, color=(0, 0, 0), duration=black_screen_duration)
                final_video = concatenate_videoclips([main_video_with_intro, black_screen])
            else:
                final_video = main_video_with_intro

            # Export the final video with high-quality settings to avoid artifacts
            logging.info("Exporting final video with intro, buffer, looped segment, and black screen as needed...")
            final_video.write_videofile(
                output_video_path,
                codec="libx264",
                audio_codec="aac",
                fps=24,
                preset="medium",  # Adjust preset for balance between quality and speed
                threads=4  # Use multithreading if possible
            )
            logging.info(f"Final video saved at: {output_video_path}")

        except Exception as e:
            logging.error(f"Failed to create video with black screen: {e}")
            raise


    def cleanup_directories(self, music_file, video_file):
        """Move used music and video files to the output directory after each run."""
        try:
            shutil.move(music_file, os.path.join(self.output_dir, os.path.basename(music_file)))
            logging.info(f"Moved used music file to {self.output_dir}")
        except Exception as e:
            logging.error(f"Failed to move {music_file}. Reason: {e}")

        try:
            shutil.move(video_file, os.path.join(self.output_dir, os.path.basename(video_file)))
            logging.info(f"Moved used video file to {self.output_dir}")
        except Exception as e:
            logging.error(f"Failed to move {video_file}. Reason: {e}")

    def upload_to_youtube(self, video_path):
        """Upload the video to YouTube with optimized settings for gaining subscribers."""
        try:
            youtube_uploader = YouTubeUploader(credentials_file='client_secrets.json')

            # Generate an optimized title with engaging elements
            title_options = [
                "Relaxing Ambient Music for Deep Sleep & Relaxation 🌌 | 10 Hours of Soothing Sounds",
                "10 Hours of Binaural Beats for Deep Sleep & Relaxation 🎶",
                "Ultimate 10-Hour Binaural Beats for Sleep & Meditation 🛌 | Deep Relaxation",
                "10 Hours of Pure Binaural Beats 🌙 | Achieve Deep Sleep & Relaxation",
                "Soothing Binaural Beats for Restful Sleep 🌌 | 10 Hours of Calm",
                "Peaceful Binaural Meditation Music 🧘 | 10 Hours for Sleep & Relaxation",
                "10 Hours of Calming Binaural Waves 🌊 | Ultimate Sleep & Meditation Sounds",
                "Deep Sleep with Binaural Beats 🌙 | 10 Hours of Soothing Meditation Music",
                "Binaural Soundscape for Deep Relaxation 🌌 | 10 Hours for Sleep",
                "10-Hour Relaxing Binaural Beats | Meditative Music for Deep Sleep 🎶",
                "Tranquil Binaural Ambience 🌠 | 10 Hours of Deep Sleep Music",
                "Ultimate Deep Sleep with Binaural Beats 🔊 | 10 Hours of Healing Sounds",
                "10 Hours of Peaceful Binaural Tones 🌙 | Perfect for Meditation & Sleep",
                "Calming Binaural Meditation Music 🌌 | 10 Hours for Sleep and Relaxation",
                "Binaural Beats & Soothing Ambience 🌙 | 10 Hours for Restful Sleep",
                "10 Hours of Gentle Binaural Beats for Sleep 🎶 | Deep Relaxation",
                "Ultimate Calm Binaural Ambience 🌌 | 10 Hours of Sleep-Inducing Sounds",
                "10-Hour Binaural Sound Therapy 🎶 | Fall Asleep Fast with Relaxing Music",
                "Healing Binaural Tones 🌙 | 10 Hours of Relaxation for Sleep & Meditation",
                "Deep Sleep Music with Binaural Beats 🌌 | 10 Hours of Calming Sounds"
            ]

            title = random.choice(title_options)

            # Create an optimized description to engage viewers and encourage subscribing
            description = (
                f"{title}\n\n"
                "Immerse yourself in 10 hours of soothing, relaxing ambient sounds designed to help you "
                "unwind, meditate, and drift into deep, restful sleep. Ideal for background ambiance, relaxation, "
                "and creating a calming environment.\n\n"
                "📌 Like, Share, and Subscribe for more relaxing sounds and sleep music.\n"
                "🔔 Don't forget to hit the notification bell to stay updated with new uploads!\n\n"
                "Follow us on our journey to peace and relaxation.\n\n"
                "#RelaxingMusic #DeepSleep #AmbientSounds #Meditation #Calm #SleepMusic"
            )

            # Use an optimal YouTube category for relaxation and music content
            # 10: Music, 22: People & Blogs, 24: Entertainment
            category_id = "10"  # Music category tends to work well for ambient and sleep videos

            # Set video privacy status to public to reach a larger audience
            privacy_status = "unlisted"

            # Set an optimized thumbnail (replace 'thumbnail_path' with actual path to the file)
            # thumbnail_path = "/path/to/optimized_thumbnail.jpg"  # Update this path with the actual thumbnail location

            logging.info("Initiating YouTube upload...")
            video_id = youtube_uploader.upload_video(
                video_path,
                title=title,
                description=description,
                category_id=category_id,
                privacy_status=privacy_status,
                # thumbnail=thumbnail_path  # Optional: Add thumbnail
            )

            if video_id:
                logging.info(f"Video uploaded successfully with ID: {video_id}")
                logging.info(f"Video Title: {title}")
            else:
                logging.error("Video upload failed.")

        except Exception as e:
            logging.error(f"An error occurred during YouTube upload: {e}")



