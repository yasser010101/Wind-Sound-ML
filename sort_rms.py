import os
import librosa

# Define the directory where the .wav files are located
directory = r"C:\Wind\Converted_to_1_sec\file_name.wav"  # Replace with your actual directory path


# Function to calculate the RMS of a .wav file
def calculate_rms(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)
    # Calculate the RMS value
    rms = librosa.feature.rms(y=y).mean()
    return rms


# Get a list of .wav files in the directory
files = [file for file in os.listdir(directory) if file.endswith('.wav')]

# Calculate RMS values and store them in a list of tuples (filename, rms)
rms_values = [(filename, calculate_rms(os.path.join(directory, filename))) for filename in files]

# Sort the list of tuples based on the RMS value in ascending order
sorted_rms_values = sorted(rms_values, key=lambda x: x[1])

# Rename the files in ascending order based on RMS value
for i, (filename, _) in enumerate(sorted_rms_values):
    # Define the new file name with a leading zero for proper sorting
    new_name = f"file_{str(i).zfill(len(str(len(files))))}.wav"

    # Define the old and new file paths
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(directory, new_name)

    # Rename the file
    os.rename(old_file, new_file)

# Print a success message
print(f"All .wav files in {directory} have been renamed in ascending order based on RMS value.")
