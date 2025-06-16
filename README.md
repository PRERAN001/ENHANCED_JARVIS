# Sasta Jarvis 🤖

A powerful AI assistant with a modern GUI interface that combines multiple functionalities including voice interaction, automation, content generation, and more.

![Sasta Jarvis](https://img.shields.io/badge/Sasta-Jarvis-blue)
![Python](https://img.shields.io/badge/Python-3.13.3-green)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-orange)

## 🌟 Features

### 🤖 AI Assistant
- Voice input and output capabilities
- Natural language processing
- Dynamic response generation
- Animated AI interface

### 🎯 Core Functionalities
- **General Queries**: Get answers to your questions
- **Automation**: Control and automate various applications
- **Web Search**: Quick access to Brave search
- **Content Generation**: 
  - PowerPoint presentations
  - Code generation
  - Custom content creation
- **Social Media Automation**:
  - WhatsApp messaging
  - YouTube automation

### 💻 Technical Features
- Modern PyQt5-based GUI
- Voice recognition and synthesis
- Multi-threaded operations
- Cross-platform compatibility

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sasta_jarvis.git
cd sasta_jarvis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python frontend/sasta_frontend.py
```

## 📋 Requirements

- Python 3.13.3 or higher
- PyQt5
- SpeechRecognition
- pyttsx3
- PyAudio
- requests
- beautifulsoup4
- Other dependencies listed in `requirements.txt`

## 🛠️ Usage

1. **Launch the Application**:
   - Run `sasta_jarvis.exe` from the `dist` folder
   - Or run `python frontend/sasta_frontend.py` from the project directory

2. **Using Voice Commands**:
   - Click the microphone button
   - Speak your command
   - Wait for the AI's response

3. **Using Text Input**:
   - Type your command in the input field
   - Press Enter or click the execute button

4. **Available Commands**:
   - General queries
   - Application automation
   - Web searches
   - Content generation
   - Social media automation

## 🏗️ Project Structure

```
sasta_jarvis/
├── frontend/
│   └── sasta_frontend.py    # GUI implementation
├── backend/
│   └── sasta_model.py       # Core functionality
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## 🔧 Backend Modules

The backend functionality is implemented in `backend/sasta_model.py`. Here's a breakdown of the available functions:

### Core Functions
- `general_quries()`: Handles general questions and queries
- `automation()`: Controls application automation
- `brave_search()`: Performs web searches using Brave
- `generate_content_for_ppt()`: Creates content for PowerPoint presentations
- `sasta_ppt_maker()`: Generates PowerPoint presentations
- `generate_code()`: Generates code based on requirements
- `whatsapp_sasta_automation()`: Handles WhatsApp automation
- `youtube_sasta_automation()`: Manages YouTube automation

To use these functions in your own projects, you can import them from the backend module:
```python
from backend.sasta_model import function_name
```

## 🔧 Building from Source

To create an executable:

```bash
python -m PyInstaller --onefile --name sasta_jarvis frontend/sasta_frontend.py
```

The executable will be created in the `dist` folder.

## ⚠️ Troubleshooting

1. **Voice Recognition Issues**:
   - Ensure microphone is properly connected
   - Check system audio settings
   - Verify PyAudio installation

2. **GUI Not Launching**:
   - Verify PyQt5 installation
   - Check for any running instances
   - Run as administrator if needed

3. **Automation Issues**:
   - Ensure target applications are installed
   - Check application paths
   - Verify permissions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PyQt5 for the GUI framework
- SpeechRecognition for voice capabilities
- All other open-source libraries used in this project

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

Made with ❤️ by PRERAN S 
