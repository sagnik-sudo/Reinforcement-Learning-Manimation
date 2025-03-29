#!/bin/bash

# Define the list of video files in order (adjust names if needed)
video_files=(
"media/videos/main/1080p60/IntroRLScene.mp4"
"media/videos/main/1080p60/MDPPolicyScene.mp4"
"media/videos/main/1080p60/DiscountedRewardsScene.mp4"
"media/videos/main/1080p60/ValueGuidesScene.mp4"
"media/videos/main/1080p60/TemporalDifferenceScene.mp4"
"media/videos/main/1080p60/SarsaVsQLearningScene.mp4"
"media/videos/main/1080p60/DeepQScene.mp4"
"media/videos/main/1080p60/PolicyGradientScene.mp4"
"media/videos/main/1080p60/OutroScene.mp4"
)

# Create a temporary file list for FFmpeg
file_list="file_list.txt"
rm -f "$file_list"
for video in "${video_files[@]}"; do
    echo "file '$video'" >> "$file_list"
done

# Concatenate the videos using FFmpeg
output_video="media/videos/main/1080p60/final_video.mp4"
ffmpeg -f concat -safe 0 -i "$file_list" -c copy "$output_video"

# Calculate total runtime of all scenes
total_duration=0
echo "Scene durations (in seconds):"
for video in "${video_files[@]}"; do
    duration=$(ffprobe -v error -show_entries format=duration \
              -of default=noprint_wrappers=1:nokey=1 "$video")
    echo "$video: $duration seconds"
    total_duration=$(echo "$total_duration + $duration" | bc)
done

echo "Total runtime (in seconds): $total_duration"

# Convert total duration to HH:MM:SS
total_seconds=$(printf "%.0f" "$total_duration")
hours=$(( total_seconds / 3600 ))
minutes=$(( (total_seconds % 3600) / 60 ))
seconds=$(( total_seconds % 60 ))

printf "Total runtime: %02d:%02d:%02d\n" "$hours" "$minutes" "$seconds"