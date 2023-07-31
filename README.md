# Reverse PI

A custom python interface for pi.ai


## 🚀 Getting Started

Follow these steps to set up and run the Pi.AI Voice Assistant on your machine:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command in your terminal:

   ```
   pip install -r requirements.txt
   ```

3. Register on the [Pi.AI website](https://pi.ai) to obtain your API key (cookie).

4. Set up your environment variable:
   - Create a `.env` file in the root of the project.
   - Add the following line to the `.env` file:
     ```
     PI_COOKIE=YOUR_API_KEY
     ```
   - Replace `YOUR_API_KEY` with the API key you obtained from Pi.AI.

5. Run the voice assistant:
   ```
   python convo.py
   ```

## 🎤 Features

- 🗣️ **Voice Interaction**: Communicate with the Unofficial Pi.AI Voice Assistant using your voice.
- 🤖 **Real-time Responses**: Get instant responses to your questions and queries.
- 📖 **Read Aloud**: Ask the assistant to read out information or messages for you.
- 🎶 **Play Audio**: Enjoy the audio output as the assistant reads messages in a natural voice.
- 🌐 **Web Connectivity**: Utilize web services to process your voice input.

## 🤖 How it Works

Reverse PI is a community reverse-engineered project built with Python. It uses the [speech_recognition](https://pypi.org/project/SpeechRecognition/) library for voice recognition. The received text response is then converted to speech and played using VLC media player.

## 📝 Usage

1. Start the Unofficial Pi.AI Voice Assistant by running `python convo.py`.
2. Wait for the prompt to say something.
3. Speak your command or question clearly.
4. The assistant will display the recognized text and respond with relevant information.
5. If the response includes an audio message, the assistant will play it for you.

## 📚 Dependencies

The following libraries are used in this project:

- [requests](https://pypi.org/project/requests/): For sending HTTP requests to the voice processing solution.
- [json](https://docs.python.org/3/library/json.html): For handling JSON data.
- [os](https://docs.python.org/3/library/os.html): For working with environment variables and file operations.
- [speech_recognition](https://pypi.org/project/SpeechRecognition/): For voice recognition.

## 📜 Disclaimer

This project is a community-driven endeavor and not affiliated with the official Pi.AI project. The use of any API or voice processing solution may be subject to terms and conditions set by the respective providers. Please ensure compliance with their policies and guidelines.

## 🤝 Contributing

Contributions are welcome! As this is a community project, your creative ideas and contributions can enhance the experience of the Unofficial Pi.AI Voice Assistant. Feel free to open an issue or submit a pull request with your improvements.
