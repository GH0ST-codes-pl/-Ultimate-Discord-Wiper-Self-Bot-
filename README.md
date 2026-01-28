# 🛡️ Ultimate Discord Wiper (Self-Bot)

![Banner](banner.png)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord](https://img.shields.io/badge/Discord-Selfbot-7289DA)
![License](https://img.shields.io/badge/License-MIT-green)

**Ultimate Discord Wiper** is an advanced, automated tool designed to manage and delete your Discord Direct Messages (DMs) efficiently and securely. Unlike basic deletion scripts, this tool focuses on **privacy protection**, **safety against bans**, and **ease of use** via an interactive CLI.

> [!WARNING]
> **Use at your own risk.** Automating user accounts (Self-botting) is technically against Discord Terms of Service. This tool includes safety delays to mimic human behavior, but safety is never 100% guaranteed.

---

## 🚀 Key Features

*   **🔒 Secure Deletion (Anti-Logger)**: Before deletion, messages are edited to random characters (e.g., `x8K9z`). This defeats "Message Logger" plugins used by other users, ensuring your original message is truly gone.
*   **🛡️ Safety First**:
    *   **Human-like Delays**: Random intervals between deletions.
    *   **Sequential Processing**: When cleaning multiple chats, the bot waits 30 seconds between conversations to avoid API rate limits.
*   **💾 Backup System**: (Optional) Automatically saves a local log of your deleted messages before they are removed.
*   **📅 Retention Policy**: (Optional) Background task to automatically delete messages older than X days every hour.
*   **🖥️ Interactive CLI**: No coding required. Launch the bot and choose options from a professional menu.
    *   Auto-Delete (Real-time monitoring)
    *   Delete History (with Date and Phrase filters)
    *   Clean ALL DMs (Mass wipe)
*   **⚙️ Easy Config**: Simple `config.txt` file for all settings.

---

## 🛠️ Installation / Instalacja

### 💻 Windows
1.  **Download Python**: Install Python 3.8+ from [python.org](https://www.python.org/) (Check "Add Python to PATH" during installation).
2.  **Download Bot**: Download this repository as a ZIP and extract it, or use git:
    ```cmd
    git clone https://github.com/GH0ST-codes-pl/discord-dm-auto-deleter-github.git
    cd discord-dm-auto-deleter-github
    ```
3.  **Install Requirements**: Open command prompt (`cmd`) in the folder and run:
    ```cmd
    pip install -r requirements.txt
    ```
4.  **Run**:
    ```cmd
    python bot.py
    ```

### 🐧 Linux / macOS
1.  **Install Python**: `sudo apt install python3 python3-pip git` (Debian/Ubuntu) or via Homebrew (macOS).
2.  **Clone Repo**:
    ```bash
    git clone https://github.com/GH0ST-codes-pl/discord-dm-auto-deleter-github.git
    cd discord-dm-auto-deleter-github
    ```
3.  **Install Requirements**:
    ```bash
    pip3 install -r requirements.txt
    ```
4.  **Run**:
    ```bash
    python3 bot.py
    ```

### 📱 Android (Termux)
1.  **Install Termux**: Download from F-Droid (Play Store version is outdated).
2.  **Update & Install Packages**:
    ```bash
    pkg update && pkg upgrade -y
    pkg install python git clang make -y
    ```
3.  **Clone Repo**:
    ```bash
    git clone https://github.com/GH0ST-codes-pl/discord-dm-auto-deleter-github.git
    cd discord-dm-auto-deleter-github
    ```
4.  **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```
    *(If `aiohttp` fails, try: `CFLAGS="-Wno-error=incompatible-function-pointer-types" pip install aiohttp`)*
5.  **Run**:
    ```bash
    python bot.py
    ```

### ⚙️ Configuration / Konfiguracja
1.  Open `config.txt` file.
2.  Paste your **User Token**.
3.  (Optional) Adjust settings like `SECURE_DELETE` or `BACKUP_ENABLED`.

---

## 📖 How to Use (English)

Run the bot:
```bash
python3 bot.py
```

### Main Menu Options:
1.  **Start Auto-Delete (Real-time)**
    *   Target: The specific channel set in `config.txt` or selected via Option 3.
    *   Action: Monitors for NEW messages from you and deletes them after a short delay.
    *   Best for: Privacy in an active conversation.

2.  **Delete History (Selected Channel)**
    *   Target: The specific channel set in `config.txt` or selected via Option 3.
    *   Action: Wipes OLD messages.
    *   **Filters**:
        *   **Limit**: "Delete last 100 messages" (Press Enter for ALL).
        *   **Date**: "Delete messages older than 2024-01-01" (Press Enter for ALL).
    
3.  **Select Target Channel from List**
    *   Action: Displays a list of your 50 most recent DMs.
    *   Usage: Type the number (e.g., `1`) to select that person as the current target for Option 1 or 2.

4.  **Clean ALL DMs (Sequential & Safe)**
    *   Action: The "Nuclear Option". Iterates through **ALL** your open DMs.
    *   **Safety**: Deletes messages from Person A -> Waits 30s -> Deletes messages from Person B -> ...
    *   **Warning**: This takes time but is safe against bans.

---

## 🇵🇱 Jak Używać (Polish)

Uruchom bota poleceniem:
```bash
python3 bot.py
```

### Opcje Menu:
1.  **Start Auto-Delete (Real-time)**
    *   Cel: Wybrany kanał (z pliku config lub opcji 3).
    *   Działanie: Nasłuchuje NOWYCH wiadomości od Ciebie i usuwa je po kilku sekundach.
    *   Zastosowanie: Utrzymanie prywatności podczas aktywnej rozmowy.

2.  **Delete History (Selected Channel)**
    *   Cel: Wybrany kanał.
    *   Działanie: Usuwa STARE wiadomości.
    *   **Filtry**:
        *   **Limit**: "Usuń ostatnie 100 wiadomości" (Enter = Wszystkie).
        *   **Data**: "Usuń starsze niż 2024-01-01" (Enter = Wszystkie).

3.  **Select Target Channel from List**
    *   Działanie: Wyświetla listę 50 ostatnich rozmów.
    *   Użycie: Wpisz numer (np. `1`), aby wybrać tę osobę jako cel dla Opcji 1 lub 2.

4.  **Clean ALL DMs (Sequential & Safe)**
    *   Działanie: "Opcja Nuklearna". Przechodzi przez **WSZYSTKIE** otwarte rozmowy DM.
    *   **Bezpieczeństwo**: Czyści rozmowę z osobą A -> Czeka 30s -> Czyści rozmowę z osobą B -> ...
    *   **Uwaga**: Proces trwa dłużej, ale chroni przed banem za spamowanie API.

---

## ⚠️ Disclaimer

This tool is for educational purposes only. Validating security vulnerabilities in Discord's API or automating user actions may result in account termination. The developer is not responsible for any bans or damages caused by the use of this tool.

