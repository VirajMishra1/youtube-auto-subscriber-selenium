# YouTube Auto-Subscriber Bot - Selenium 🎥

## Project Description

The **YouTube Auto-Subscriber Bot** is a Python-based tool that automates subscribing to YouTube channels and helps transfer subscriptions from one account to another. By utilizing Selenium, the script logs into a Gmail account, navigates to the specified YouTube channels, and subscribes to them if not already subscribed. The tool is designed for efficient and hands-free channel subscription management.

## 🚀 Features

1. **Automated Gmail Login**: The bot securely logs into a Gmail account using Selenium.
2. **Channel Subscription**: Automatically subscribes to channels listed in a text file.
3. **Smart Detection**: Detects if the user is already subscribed to a channel and skips unnecessary actions.
4. **Headless Browser Mode**: Runs the browser in headless mode for faster execution and reduced resource usage.
5. **System Awake Functionality**: Prevents the system from sleeping during script execution using `caffeinate`.
6. **Error Handling**: Handles exceptions during login and subscription to ensure smooth operation.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Selenium**: For browser automation.
- **caffeinate**: Keeps the system awake on macOS.
- **ChromeDriver**: Interface for controlling Google Chrome.

## 📦 Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd youtube-auto-subscriber
    ```
3. **Install Required Dependencies**:
    ```bash
    pip install selenium
    ```
4. **Download ChromeDriver**:
   - Ensure that ChromeDriver is installed and added to your system PATH.
   - You can download it from [ChromeDriver Download Page](https://chromedriver.chromium.org/downloads).

5. **Edit Configuration**:
    - Replace the placeholder email, password, and file path in the script:
      ```python
      gmail_email = 'your_email@gmail.com'
      gmail_password = 'your_password'
      file_path = 'path_to_your_channel_list.txt'
      ```
    - The `file_path` should point to a text file containing YouTube channel URLs, one per line.

6. **Run the Script**:
    ```bash
    python youtube_auto_subscriber.py
    ```

## 📝 Usage

1. Prepare a text file with YouTube channel URLs, one URL per line. You retrieve your subscriptions from your existing account and ask https://www.perplexity.ai/ to make the text file. 
2. Replace your Gmail credentials and the file path in the script.
3. Run the script to log in to Gmail and subscribe to the channels automatically.
4. The script will indicate success, existing subscriptions, or any errors during the process.

## 📚 Example

### Sample Input File:
```
https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg
https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ
```

### Output:
```
Loaded 3 channels from file: ['https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw', ...]
Logging in to Gmail...
Login successful!
Navigating to the channel: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
Successfully subscribed to the channel!
Navigating to the channel: https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg
Already subscribed to the channel.
Navigating to the channel: https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ
Subscribe button not found or is in a different state.
```

## 🛡️ Security Note

- Avoid using your primary Gmail account. Consider creating a separate account for this tool.
- Do not share or commit sensitive information like email or password to public repositories.

## 🤝 Contribution

Contributions are welcome! If you have ideas for improving the project, feel free to fork the repository and submit a pull request.

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Viraj Mishra
