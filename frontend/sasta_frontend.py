import sys
import os
import traceback
import time
import pyautogui

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                QHBoxLayout, QLabel, QPushButton, QTextEdit,
                                QLineEdit, QMessageBox, QGridLayout, QFrame)
    from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
    from PyQt5.QtGui import QPainter, QColor, QPen, QFont
    import speech_recognition as sr
    from PyQt5.QtMultimedia import QMediaPlayer, QAudioOutput
    import threading
    print("Successfully imported PyQt5 and other dependencies")
except Exception as e:
    print(f"Error importing dependencies: {str(e)}")
    print("Traceback:")
    traceback.print_exc()
    sys.exit(1)

try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from backend.sasta_model import (
        listen_and_convert, ask_groq, txt_to_speak, automation,
        general_quries, brave_search, generate_content_for_ppt,
        sasta_ppt_maker, generate_code,
        whatsapp_sasta_automation, youtube_sasta_automation
    )
    print("Successfully imported backend modules")
except Exception as e:
    print(f"Error importing backend modules: {str(e)}")
    print("Traceback:")
    traceback.print_exc()
    sys.exit(1)

def send_whatsapp_message(contact_name, message):
    try:
        # Open WhatsApp desktop app using automation function
        automation("open whatsapp")
        time.sleep(5)  # Wait longer for the desktop app to open
        
        # Click on search bar
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        
        # Type contact name
        pyautogui.write(contact_name)
        time.sleep(2)
        
        # Press enter to select the contact
        pyautogui.press('enter')
        time.sleep(1)
        
        # Click on the chat at specific coordinates
        pyautogui.click(x=200, y=200)
        time.sleep(1)
        
        # Type the message
        pyautogui.write(message)
        time.sleep(1)
        
        # Send the message
        pyautogui.press('enter')
        
        return True
    except Exception as e:
        print(f"Error in WhatsApp automation: {str(e)}")
        return False

class AnimatedAI(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)
        
    def update_animation(self):
        self.angle = (self.angle + 5) % 360
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(QColor(0, 255, 255))
        pen.setWidth(2)
        painter.setPen(pen)
        
        center = self.rect().center()
        radius = min(self.width(), self.height()) // 3
        painter.drawArc(center.x() - radius, center.y() - radius,
                       radius * 2, radius * 2, self.angle * 16, 270 * 16)
        
        font = QFont('Arial', 20)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, "AI Assistant")

class FeatureCard(QFrame):
    def __init__(self, title, function_name, main_window_ref):
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.main_window = main_window_ref
        self.function_name = function_name

        layout = QVBoxLayout()
        label = QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #00ff00; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)
        self.setLayout(layout)

        self.setStyleSheet("""
            FeatureCard {
                background-color: #1a1a1a;
                border: 2px solid #333;
                border-radius: 10px;
                padding: 15px;
            }
            FeatureCard:hover {
                background-color: #333333;
                border: 2px solid #00ff00;
            }
        """)

    def mousePressEvent(self, event):
        self.main_window.set_active_function(self.function_name)
        super().mousePressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sasta AI Assistant")
        self.setStyleSheet("background-color: black; color: white;")
        self.setMinimumSize(1200, 800)
        
        # Define features and their placeholder texts
        self.features = {
            "General Query": {"title": "General Query", "placeholder": "Ask me anything!"},
            "Open Website/App": {"title": "Open Website/App", "placeholder": "e.g., open youtube, open chrome"},
            "Search Web": {"title": "Search Web", "placeholder": "e.g., search for latest news"},
            "Create PowerPoint": {"title": "Create PowerPoint", "placeholder": "e.g., generate a ppt on topic AI and save it as MyAI"},
            "Generate Code": {"title": "Generate Code", "placeholder": "e.g., write python function for fibonacci series"},
            "WhatsApp Message": {"title": "WhatsApp Message", "placeholder": "e.g., jhon send message hi there"},
            "YouTube Automation": {"title": "YouTube Automation", "placeholder": "e.g., type the channel name"}
        }
        self.active_function = "General Query" # Default active function

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Left side - Feature cards, Input field, and Output display
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        # Feature Cards Grid Layout
        self.cards_layout = QGridLayout()
        self.card_widgets = {}
        row, col = 0, 0
        for name, data in self.features.items():
            card = FeatureCard(data["title"], name, self)
            self.cards_layout.addWidget(card, row, col)
            self.card_widgets[name] = card
            col += 1
            if col >= 2: # 2 cards per row
                col = 0
                row += 1
        left_layout.addLayout(self.cards_layout)

        # Input field for commands
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText(self.features[self.active_function]["placeholder"])
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: #00ff00;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        left_layout.addWidget(self.input_field)
        
        # Output display
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                color: #00ff00;
                border: 2px solid #333;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        left_layout.addWidget(self.output_display)
        
        # Right side - AI Animation and Voice Input
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # Add AI Animation
        self.ai_animation = AnimatedAI()
        self.ai_animation.setMinimumSize(300, 300)
        right_layout.addWidget(self.ai_animation)
        
        # Add Voice Input Button
        self.voice_button = QPushButton("Click to Speak")
        self.voice_button.setStyleSheet("""
            QPushButton {
                background-color: #00ff00;
                color: black;
                border: none;
                border-radius: 20px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00cc00;
            }
        """)
        self.voice_button.clicked.connect(self.start_voice_input)
        right_layout.addWidget(self.voice_button)
        
        # Add Execute Button
        self.execute_button = QPushButton("Execute Command")
        self.execute_button.setStyleSheet("""
            QPushButton {
                background-color: #0066ff;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0052cc;
            }
        """)
        self.execute_button.clicked.connect(self.execute_command)
        right_layout.addWidget(self.execute_button)
        
        # Add widgets to main layout
        layout.addWidget(left_widget, 2)
        layout.addWidget(right_widget, 1)

        self.set_active_function("General Query") # Set initial state for input field

    def set_active_function(self, function_name):
        self.active_function = function_name
        self.input_field.setPlaceholderText(self.features[function_name]["placeholder"])
        # Optionally, add visual feedback for the selected card
        for name, card in self.card_widgets.items():
            if name == function_name:
                card.setStyleSheet("""
                    FeatureCard {
                        background-color: #333333;
                        border: 2px solid #00ff00;
                        border-radius: 10px;
                        padding: 15px;
                    }
                """)
            else:
                card.setStyleSheet("""
                    FeatureCard {
                        background-color: #1a1a1a;
                        border: 2px solid #333;
                        border-radius: 10px;
                        padding: 15px;
                    }
                    FeatureCard:hover {
                        background-color: #333333;
                        border: 2px solid #00ff00;
                    }
                """)
        
    def start_voice_input(self):
        self.voice_button.setEnabled(False)
        self.voice_button.setText("Listening...")
        
        threading.Thread(target=self.process_voice_input, daemon=True).start()
    
    def process_voice_input(self):
        try:
            user_input = listen_and_convert()
            self.input_field.setText(user_input)
            self.execute_command()
        except Exception as e:
            self.output_display.append(f"Error: {str(e)}\n")
        finally:
            self.voice_button.setEnabled(True)
            self.voice_button.setText("Click to Speak")
    
    def execute_command(self):
        command = self.input_field.text().strip()
        if not command:
            return
            
        function = self.active_function # Use active_function from card selection
        try:
            if function == "General Query":
                response = general_quries(command)
                self.output_display.append(f"Response: {response}\n")
                txt_to_speak(response)
                
            elif function == "Open Website/App":
                automation(command)
                self.output_display.append(f"Attempting to open: {command}\n")
                txt_to_speak(f"Attempting to open {command}")
                
            elif function == "Search Web":
                results = brave_search(command)
                if results:
                    response_text = "Search results:\n" + "\n".join(results)
                    self.output_display.append(response_text)
                    txt_to_speak("Here are the top search results.")
                else:
                    self.output_display.append("No search results found.\n")
                    txt_to_speak("No search results found.")
                    
            elif function == "Create PowerPoint":
                titles, contents, images = generate_content_for_ppt(command)
                if titles and contents:
                    sasta_ppt_maker(f"{command.replace(' ', '_')}.pptx", titles, contents)
                    self.output_display.append("PowerPoint created successfully!\n")
                    txt_to_speak("PowerPoint created successfully.")
                else:
                    self.output_display.append("Failed to create PowerPoint.\n")
                    txt_to_speak("Failed to create PowerPoint.")

                    
            elif function == "Generate Code":
                code = generate_code(command)
                self.output_display.append(f"Generated Code:\n{code}\n")
                txt_to_speak("Code generation complete.")

            elif function == "WhatsApp Message":
                # Parse the command to separate contact name and message
                try:
                    # Split the command into contact name and message
                    parts = command.split(" send message ", 1)
                    if len(parts) == 2:
                        contact_name = parts[0].replace("search for ", "").strip()
                        message = parts[1].strip()
                        
                        self.output_display.append(f"Searching for contact: {contact_name}\n")
                        self.output_display.append(f"Message to send: {message}\n")
                        
                        if send_whatsapp_message(contact_name, message):
                            self.output_display.append("Message sent successfully!\n")
                            txt_to_speak("Message sent successfully.")
                        else:
                            self.output_display.append("Failed to send message. Please try again.\n")
                            txt_to_speak("Failed to send message. Please try again.")

                    else:
                        self.output_display.append("Invalid format. Please use: 'search for [contact name] send message [message]'\n")
                        txt_to_speak("Invalid format for WhatsApp message. Please use: 'search for [contact name] send message [message]'")
                except Exception as e:
                    self.output_display.append(f"Error in WhatsApp automation: {str(e)}\n")
                    txt_to_speak(f"Error in WhatsApp automation: {str(e)}")

            elif function == "YouTube Automation":
                youtube_sasta_automation(command)
                self.output_display.append("YouTube automation completed!\n")
                txt_to_speak("YouTube automation completed.")

        except Exception as e:
            self.output_display.append(f"Error: {str(e)}\n")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            txt_to_speak(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    try:
        print("Starting application...")
        app = QApplication(sys.argv)
        print("Created QApplication instance")
        window = MainWindow()
        print("Created MainWindow instance")
        window.show()
        print("Showing window")
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error in main: {str(e)}")
        print("Traceback:")
        traceback.print_exc()
        sys.exit(1) 
