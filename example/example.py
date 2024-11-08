import logging
import shutil
import time
import os
from datetime import datetime
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, concatenate_videoclips, ColorClip, AudioFileClip
# from moviepy.video.fx.all import loop

from example.utilities.youtube_uploader import YouTubeUploader
from example.utilities.logic_pro import LogicProAutomation

class ExampleShell:
    def __init__(self, configs, debug=True, duration_hours=0.0083):
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
            # logging.info("Moving used music and video files to output directory for archival...")
            # self.cleanup_directories(music_file, video_file)

            # Step 4: Upload to YouTube
            # logging.info("Step 4: Uploading video to YouTube...")
            # self.upload_to_youtube(output_video_path)

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

    def create_video_with_black_screen(self, video_file, audio_path, output_video_path, duration_hours,
                                       buffer_duration=1):
        """
        Create a video with an intro, a slight buffer, an initial looped segment covering the audio duration,
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
            loop_duration = min(total_duration, audio_duration) - intro_clip.duration - buffer_duration
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

                # Create a buffer clip (black screen) between intro and main video
                # buffer_clip = ColorClip(size=video_clip.size, color=(0, 0, 0), duration=buffer_duration)

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
        """Upload the video to YouTube."""
        try:
            youtube_uploader = YouTubeUploader(credentials_file='client_secrets.json')
            title = "Relaxing Sleep Video with Soothing Sounds"
            description = (
                "This video features calming visuals and relaxing ambient music "
                "to help you unwind and fall asleep."
            )
            category_id = "22"  # YouTube category for People & Blogs
            privacy_status = "unlisted"
            logging.info("Initiating YouTube upload...")
            video_id = youtube_uploader.upload_video(video_path, title, description, category_id, privacy_status)
            if video_id:
                logging.info(f"Video uploaded successfully with ID: {video_id}")
            else:
                logging.error("Video upload failed.")
        except Exception as e:
            logging.error(f"An error occurred during YouTube upload: {e}")

    # def create_looped_audio_with_crossfade(self, audio_file, output_path, duration, crossfade_duration=2000,
    #                                        chunk_size_ms=60000):
    #     """
    #     Loop the audio file with crossfade until reaching or slightly exceeding the specified duration,
    #     and export in chunks with progress tracking.
    #     """
    #     try:
    #         audio = AudioSegment.from_file(audio_file)
    #         looped_audio = audio
    #         logging.info("Starting audio looping...")
    #
    #         # Repeat and crossfade until reaching or slightly exceeding target duration
    #         while len(looped_audio) < duration:
    #             looped_audio = looped_audio.append(audio, crossfade=crossfade_duration)
    #             progress_percentage = min(len(looped_audio) / duration * 100, 100)
    #             logging.info(f"Audio looping progress: {progress_percentage:.2f}% complete.")
    #
    #         # Directory for temporary chunk exports
    #         temp_dir = os.path.join(self.output_dir, "temp_audio_chunks")
    #         os.makedirs(temp_dir, exist_ok=True)
    #
    #         # Export each chunk with progress tracking
    #         logging.info("Starting export with chunked progress tracking...")
    #         total_length_ms = len(looped_audio)
    #         start = 0
    #         chunk_files = []
    #
    #         while start < total_length_ms:
    #             end = min(start + chunk_size_ms, total_length_ms)
    #             chunk = looped_audio[start:end]
    #             chunk_path = os.path.join(temp_dir, f"chunk_{start // chunk_size_ms + 1}.mp3")
    #             chunk.export(chunk_path, format="mp3")
    #             chunk_files.append(chunk_path)
    #             start += chunk_size_ms
    #
    #             # Log export progress and memory usage
    #             progress_percentage = min(start / total_length_ms * 100, 100)
    #             memory_info = psutil.virtual_memory()  # Get memory stats if psutil is available
    #             logging.info(f"Exporting audio chunk {start // chunk_size_ms}: {progress_percentage:.2f}% complete. "
    #                          f"Memory Usage: {memory_info.percent}%")
    #
    #         # Combining chunks into the final output
    #         logging.info("Combining chunks into the final audio file...")
    #         final_audio = AudioSegment.empty()
    #         for i, chunk_path in enumerate(chunk_files, start=1):
    #             logging.info(f"Adding chunk {i} to final audio...")
    #             final_audio += AudioSegment.from_file(chunk_path)
    #
    #         # Log before final export step to diagnose potential issues
    #         logging.info("Final audio assembled, starting final export to output file...")
    #         memory_info = psutil.virtual_memory()
    #         logging.info(f"Memory before final export: {memory_info.percent}%")
    #
    #         # Export the final combined audio
    #         final_audio.export(output_path, format="mp3")
    #         logging.info(f"Final looped audio with crossfade saved at: {output_path}")
    #
    #         # Clean up temporary chunk files
    #         shutil.rmtree(temp_dir)
    #         logging.info("Temporary chunk files cleaned up.")
    #
    #     except Exception as e:
    #         logging.error(f"Failed to create looped audio with crossfade: {e}")
    #         raise

