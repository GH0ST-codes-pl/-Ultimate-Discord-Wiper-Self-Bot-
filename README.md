# 🛡️ Ultimate Discord Wiper (Self-Bot)

![Banner](banner.png)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord](https://img.shields.io/badge/Discord-Selfbot-7289DA)
![License](https://img.shields.io/badge/License-MIT-green)

---

**Ultimate Discord Wiper** is an advanced, automated tool designed to manage and delete your Discord Direct Messages (DMs) efficiently and securely. Unlike basic deletion scripts, this tool focuses on **privacy protection**, **safety against bans**, and **ease of use** via an interactive CLI.

**Ultimate Discord Wiper** to zaawansowane, zautomatyzowane narzędzie zaprojektowane do wydajnego i bezpiecznego zarządzania oraz usuwania wiadomości prywatnych (DM) na Discordzie. W przeciwieństwie do podstawowych skryptów, to narzędzie skupia się na **ochronie prywatności**, **bezpieczeństwie przed banami** i **łatwości obsługi** dzięki interaktywnemu menu CLI.

> [!WARNING]
> **Use at your own risk.** Automating user accounts (Self-botting) is technically against Discord Terms of Service. This tool includes safety delays to mimic human behavior, but safety is never 100% guaranteed.
>
> **Używasz na własne ryzyko.** Automatyzacja kont użytkowników (Self-botting) jest technicznie sprzeczna z Regulaminem Discorda. To narzędzie zawiera opóźnienia symulujące zachowanie człowieka, ale bezpieczeństwo nigdy nie jest gwarantowane w 100%.

---

## 🚀 Key Features / Główne Funkcje

### 🛠️ Functionality / Funkcjonalność
*   **📅 Delete by Date / Usuwanie po Dacie**: Remove messages older than a specific day (e.g., wipe everything before 2024). / Usuń wiadomości starsze niż konkretny dzień.
*   **🔍 Phrase Filter / Filtr Fraz**: Delete only messages containing a specific word or sentence. / Usuń tylko wiadomości zawierające określone słowo lub zdanie.
*   **🔢 Amount Limit / Limit Ilości**: Delete only the last N messages (or leave empty for a full wipe). / Usuń tylko ostatnie N wiadomości (lub zostaw puste dla pełnego czyszczenia).
*   **📂 Multi-Channel / Wybór Rozmów**: Interactive menu to select any DM from your recent history (Top 50). / Interaktywne menu do wyboru dowolnego DM z Twojej ostatniej historii (Top 50).
*   **☢️ Safe Global Wipe / Masowe Czyszczenie**: "Clean ALL DMs" mode that safely clears every open conversation one by one. / Tryb "Wyczyść WSZYSTKIE DM", który bezpiecznie czyści każdą otwartą rozmowę po kolei.

### 🛡️ Security / Bezpieczeństwo
*   **🔒 Secure Delete (Anti-Logger)**: Edits messages to random gibberish before deleting to bypass message logging plugins. / Edytuje wiadomości na losowe znaki przed usunięciem, aby ominąć wtyczki logujące wiadomości.
*   **💾 Local Backup**: Saves your messages to `backups/deleted_msgs.log` before they vanish. / Zapisuje Twoje wiadomości w `backups/deleted_msgs.log` zanim znikną.
*   **🕒 Smart Delays**: Mimics human behavior with random pauses and a 30s cool-down between different conversations. / Symuluje zachowanie człowieka dzięki losowym pauzom i 30-sekundowej przerwie między różnymi rozmowami.
*   **📅 Automatic Retention**: Keep your history fresh by auto-deleting messages older than X days in the background. / Utrzymuj historię w czystości, automatycznie usuwając w tle wiadomości starsze niż X dni.

---

## 🛠️ Installation / Instalacja

### 💻 Windows
1.  **Download Python**: Install Python 3.8+ from [python.org](https://www.python.org/) (Check "Add Python to PATH"). / Zainstaluj Pythona 3.8+ (Zaznacz "Add Python to PATH").
2.  **Download Bot**: `git clone https://github.com/GH0ST-codes-pl/-Ultimate-Discord-Wiper-Self-Bot-.git` / Pobierz bota.
3.  **Install Requirements**: `pip install -r requirements.txt` / Zainstaluj wymagania.
4.  **Run**: `python bot.py` / Uruchom.

### 🐧 Linux / macOS
1.  **Install Python**: `sudo apt install python3 python3-pip git` / Zainstaluj Pythona i Git.
2.  **Clone Repo**: `git clone https://github.com/GH0ST-codes-pl/-Ultimate-Discord-Wiper-Self-Bot-.git` / Sklonuj repozytorium.
3.  **Install Requirements**: `pip3 install -r requirements.txt` / Zainstaluj wymagania.
4.  **Run**: `python3 bot.py` / Uruchom.

### 📱 Android (Termux)
1.  **Install Termux** (from F-Droid).
2.  **Update**: `pkg update && pkg upgrade -y`
3.  **Install Build Tools**: `pkg install python git clang make -y`
4.  **Clone & Install**: `git clone ...` then `pip install -r requirements.txt`
5.  **Run**: `python bot.py`

---

## 📖 How to Use / Jak Używać

### ⚙️ Step 1: Configuration / Konfiguracja
Edit **`config.txt`**:
*   `USER_TOKEN`: Your Discord authorization token. / Twój token autoryzacji Discord.
*   `SECURE_DELETE`: `true` to edit messages before deleting. / `true`, aby edytować wiadomości przed usunięciem.
*   `BACKUP_ENABLED`: `true` to save logs locally. / `true`, aby zapisywać logi lokalnie.
*   `RETENTION_DAYS`: Set to e.g., `30` to auto-clean old messages. / Ustaw np. `30`, aby automatycznie czyścić stare wiadomości.

### ⌨️ Step 2: Interactive Menu / Menu Interaktywne
Run `python3 bot.py` and choose:

1.  **Start Auto-Delete**: Real-time cleaning of the current target channel. / Czyszczenie wybranego kanału w czasie rzeczywistym.
2.  **Delete History (Selected Channel)**: / Usuwanie historii (wybrany kanał):
    *   First, it asks for a **Limit** (how many). / Najpierw pyta o **Limit** (ile).
    *   Second, it asks for a **Date** (from when). / Potem pyta o **Datę** (od kiedy).
    *   Third, it asks for a **Phrase** (filter content). / Na końcu pyta o **Frazę** (treść).
3.  **Select Target**: Pick someone from your DM list. / Wybierz kogoś z listy DM.
4.  **Clean ALL DMs**: Safely wipe every single DM conversation you have open. / Bezpiecznie wyczyść każdą otwartą rozmowę DM. 

---

## ⚠️ Disclaimer / Zastrzeżenie

This tool is for educational purposes only. Validating security vulnerabilities in Discord's API or automating user actions may result in account termination. The developer is not responsible for any bans or damages caused by the use of this tool.

To narzędzie służy wyłącznie do celów edukacyjnych. Badanie luk w zabezpieczeniach API Discorda lub automatyzacja działań użytkownika może skutkować zamknięciem konta. Autor nie ponosi odpowiedzialności za jakiekolwiek bany lub szkody spowodowane korzystaniem z tego narzędzia.
