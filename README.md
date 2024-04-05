---

# Speech Recognition Game

This repository contains a Python script for a simple speech recognition game where two players take turns speaking into a microphone, and the script transcribes their speech using the Google Cloud Speech API. The game also estimates the speaker's gender based on their pitch contour.

## Usage

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/wazupsteve/speech-recognition-game.git
   ```

2. **Navigate to the Directory:** Change your current directory to the cloned repository:
   ```
   cd speech-recognition-game
   ```

3. **Install Dependencies:** Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. **Obtain Google Cloud Speech API Key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing project.
   - Enable the Google Cloud Speech-to-Text API for your project.
   - Create a service account and download the JSON key file.
   - Rename the JSON key file to `YOUR_API_KEY.json` and place it in the root directory of the repository.

5. **Run the Script:** Run the Python script to start the speech recognition game:
   ```
   python speech_recognition_game.py
   ```

6. **Follow On-Screen Instructions:** Follow the on-screen instructions to play the game. Players take turns speaking into the microphone, and their speech is transcribed by the script using the Google Cloud Speech API. The estimated gender of the speaker is also displayed based on pitch contour analysis.

## Dependencies

- `speech_recognition`: Library for performing speech recognition with support for several engines and APIs, including Google Cloud Speech API.
- `google-cloud-speech`: Official Google Cloud Speech API client library.
- `numpy`: Library for numerical computing in Python.
- `librosa`: Library for audio and music analysis.

## Contribution

Contributions to this project are welcome. Feel free to fork this repository and submit pull requests with your enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

