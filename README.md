# Chatbot-Gemini

Chatbot-Gemini is a Flask-based web application that utilizes Google's Generative AI (Gemini) to create conversational chatbot responses. This repository provides a seamless integration of the Google Generative AI API into a web interface for interactive communication.

## Features

- **User Interaction**: Users can input messages via the web interface to engage with the chatbot.
- **AI Response**: The chatbot processes user inputs using Google's Generative AI model to generate contextually relevant responses.
- **Web Interface**: The Flask application provides a user-friendly web interface for a smooth chatting experience.
- **Markdown Support**: Markdown formatting is supported in both user inputs and chatbot responses for enhanced readability.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Chatbot-Gemini.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Chatbot-Gemini
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Obtain a Google API key and add it to the `.env` file:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Access the application in your web browser at `http://127.0.0.1:5000`.

## File Structure

- `app.py`: Contains the main Flask application code for routing and logic.
- `templates/`: Directory for HTML templates used in rendering the web interface.
  - `index.html`: Home page template with the user input form.
  - `bot.html`: Template to display chatbot responses.
- `requirements.txt`: List of Python dependencies required for the project.

## Contributing

Contributions to Chatbot-Gemini are welcome! Here's how you can contribute:
- Fork the repository.
- Create a new branch (`git checkout -b feature/my-feature`).
- Make your changes and commit them (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/my-feature`).
- Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, feel free to contact the project maintainers at [aakashsinha1606@gmail.com](mailto:aakashsinha1606@gmail.com).

---

Feel free to customize the README further by adding specific details about your project, such as deployment instructions, troubleshooting tips, additional features, or contact information.
