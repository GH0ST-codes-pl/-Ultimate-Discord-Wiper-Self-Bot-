"""
Discord DM Auto-Deleter Bot
Advanced CLI Tool for managing Discord DMs

WARNING: Self-bots violate Discord Terms of Service.
Use at your own risk!
"""

import discord
import asyncio
import os
import random
import string
from datetime import datetime, timedelta
from discord.ext import tasks
from colorama import Fore, Style, init
from config import Config

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class DMDeleterBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.delete_count = 0
        self.is_running = True
        
        # Create backups directory if needed
        if self.config.backup_enabled and not os.path.exists("backups"):
            os.makedirs("backups")
            
    def log(self, message, level="INFO"):
        """Colored logging with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if level == "SUCCESS":
            color = Fore.GREEN
            icon = "✓"
        elif level == "ERROR":
            color = Fore.RED
            icon = "✗"
        elif level == "WARNING":
            color = Fore.YELLOW
            icon = "⚠"
        elif level == "BACKUP":
            color = Fore.BLUE
            icon = "💾"
        elif level == "SECURE":
            color = Fore.MAGENTA
            icon = "🔒"    
        else:  # INFO
            color = Fore.CYAN
            icon = "ℹ"
            
        print(f"{Fore.WHITE}[{timestamp}] {color}{icon} {message}{Style.RESET_ALL}")
    
    async def log_backup(self, message):
        """Append message content to a local log file"""
        if not self.config.backup_enabled:
            return
            
        try:
            filename = f"backups/deleted_msgs.log"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            author = message.channel.recipient.name if hasattr(message.channel, "recipient") else f"Channel {message.channel.id}"
            
            content = message.content
            # Handle empty content (e.g. only attachments)
            if not content and message.attachments:
                content = f"[Attachment: {message.attachments[0].url}]"
            elif not content:
                content = "[No Text Content]"
                
            entry = f"[{timestamp}] To: {author} | Content: {content}\n"
            
            with open(filename, "a", encoding="utf-8") as f:
                f.write(entry)
        except Exception as e:
            self.log(f"Backup failed: {e}", "ERROR")

    async def secure_delete(self, message):
        """Edit message to random garbage before deleting"""
        if self.config.secure_delete:
            try:
                # Generate random string of same length (or fixed short length to save time)
                garbage = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                await message.edit(content=garbage)
                # Tiny sleep to ensure edit propagates
                await asyncio.sleep(0.3) 
            except Exception:
                pass # Ignore edit errors (e.g. if message too old or already deleted)
        
        await message.delete()

    async def on_ready(self):
        """Event called when logged in"""
        self.log(f"Logged in as {self.user.name} (ID: {self.user.id})", "SUCCESS")
        
        # Start retention task if enabled
        if self.config.retention_days > 0:
            self.retention_task.start()
            self.log(f"Retention policy active: deleting messages older than {self.config.retention_days} days every hour.", "INFO")

        # Interactive Menu
        await self.show_menu()

    async def show_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_banner()
            
            if self.config.channel_id:
                print(f"{Fore.CYAN}Current Target: {Fore.WHITE}{self.config.channel_id}")
            else:
                print(f"{Fore.CYAN}Current Target: {Fore.RED}NONE")
                
            print(f"\n{Fore.YELLOW}=== MENU ==={Style.RESET_ALL}")
            print(f"1. {Fore.GREEN}Start Auto-Delete (Real-time){Style.RESET_ALL}")
            print(f"2. {Fore.RED}Delete History (Selected Channel){Style.RESET_ALL}")
            print(f"3. {Fore.MAGENTA}Select Target Channel from List{Style.RESET_ALL}")
            print(f"4. {Fore.RED}Clean ALL DMs (Sequential & Safe){Style.RESET_ALL}")
            print(f"5. {Fore.BLUE}Settings Info{Style.RESET_ALL}")
            print(f"6. {Fore.RED}Exit{Style.RESET_ALL}")
            
            choice = await asyncio.to_thread(input, f"\n{Fore.CYAN}Selection: {Style.RESET_ALL}")
            
            if choice == "1":
                self.log("Auto-delete is running in background. Press Ctrl+C to stop.", "INFO")
                # Just keep running, maybe show a spinner or wait
                await asyncio.Future() # Wait forever
                
            elif choice == "2":
                if not self.config.channel_id:
                    self.log("No channel selected! Use option 3 first.", "ERROR")
                    await asyncio.sleep(2)
                    continue
                    
                channel = self.get_channel(self.config.channel_id)
                if not channel:
                    self.log("Channel not found/accessible.", "ERROR")
                    await asyncio.sleep(2)
                    continue

                await self.prompt_delete_history(channel)
                input(f"\n{Fore.CYAN}Press Enter to return to menu...{Style.RESET_ALL}")

            elif choice == "3":
                await self.select_channel_menu()

            elif choice == "4":
                print(f"\n{Fore.RED}WARNING: This will delete messaging history from ALL opened DMs.{Style.RESET_ALL}")
                confirm = await asyncio.to_thread(input, f"{Fore.YELLOW}Are you sure? (type 'confirm' to proceed): {Style.RESET_ALL}")
                if confirm.lower() == "confirm":
                    await self.clean_all_dms_sequentially()
                else:
                    self.log("Operation cancelled.", "WARNING")
                input(f"\n{Fore.CYAN}Press Enter to return to menu...{Style.RESET_ALL}")
                
            elif choice == "5":
                print(f"\n{Fore.BLUE}=== SETTINGS ==={Style.RESET_ALL}")
                print(f"Secure Delete: {self.config.secure_delete}")
                print(f"Backup Enabled: {self.config.backup_enabled}")
                print(f"Retention Days: {self.config.retention_days}")
                print(f"Auto-Delete: {self.config.auto_delete_enabled}")
                input(f"\n{Fore.CYAN}Press Enter to return to menu...{Style.RESET_ALL}")
                
            elif choice == "6":
                await self.close()
                break

    async def select_channel_menu(self):
        """Show list of DMs and allow selection"""
        dm_channels = [ch for ch in self.private_channels if isinstance(ch, discord.DMChannel)]
        # Sort by last_message_id (most recent first) to show active chats at the top
        dm_channels.sort(key=lambda x: x.last_message_id or 0, reverse=True)
        
        print(f"\n{Fore.YELLOW}=== YOUR CONVERSATIONS ==={Style.RESET_ALL}")
        for i, ch in enumerate(dm_channels[:50]): # Show max 50
            name = ch.recipient.name if hasattr(ch, "recipient") else "Unknown"
            print(f"{i+1}. {name} (ID: {ch.id})")
            
        print(f"\n{Fore.CYAN}Enter number to select, or paste ID manually.{Style.RESET_ALL}")
        choice = await asyncio.to_thread(input, "Selection: ")
        
        selected_id = None
        if choice.isdigit() and 1 <= int(choice) <= len(dm_channels):
            selected_id = dm_channels[int(choice)-1].id
        elif choice.isdigit(): # Maybe they pasted an ID
            selected_id = int(choice)
            
        if selected_id:
            self.config.channel_id = selected_id
            self.log(f"Selected channel ID: {selected_id}", "SUCCESS")
        else:
            self.log("Invalid selection.", "ERROR")
        
        await asyncio.sleep(1)

    async def prompt_delete_history(self, channel):
        limit_input = await asyncio.to_thread(input, f"{Fore.CYAN}How many messages to delete? (Press Enter for ALL): {Style.RESET_ALL}")
        limit = int(limit_input) if limit_input.isdigit() else None
        
        date_str = await asyncio.to_thread(input, f"{Fore.CYAN}Delete messages older than? (YYYY-MM-DD, Press Enter for ALL): {Style.RESET_ALL}")
        before_date = None
        if date_str.strip():
            try:
                before_date = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            except ValueError:
                self.log("Invalid date format! Ignoring date filter.", "WARNING")

        phrase = await asyncio.to_thread(input, f"{Fore.CYAN}Delete only messages containing phrase? (Press Enter for NO FILTER): {Style.RESET_ALL}")
        phrase = phrase.strip() if phrase.strip() else None

        await self.delete_all_messages(channel, limit=limit, phrase=phrase, before_date=before_date)

    async def clean_all_dms_sequentially(self):
        """Safely cleans all DMs one by one"""
        dm_channels = [ch for ch in self.private_channels if isinstance(ch, discord.DMChannel)]
        # Sort by last_message_id (oldest first)
        dm_channels.sort(key=lambda x: x.last_message_id or 0)
        total = len(dm_channels)
        
        self.log(f"Found {total} conversations. Starting sequential cleanup...", "INFO")
        self.log(f"SAFTEY DELAY enabled: 30s break between channels.", "WARNING")
        
        for i, channel in enumerate(dm_channels):
            recipient = channel.recipient.name if hasattr(channel, "recipient") else "Unknown"
            self.log(f"[{i+1}/{total}] Processing DM with {recipient}...", "INFO")
            
            # Clean this channel
            await self.delete_all_messages(channel)
            
            if i < total - 1:
                # Safety delay
                self.log("Waiting 30 seconds before next channel (Safety Break)...", "WARNING")
                await asyncio.sleep(30)
        
        self.log("All conversations processed!", "SUCCESS")

    async def on_message(self, message):
        """Event called for every new message"""
        if (self.config.auto_delete_enabled and 
            message.author.id == self.user.id and 
            message.channel.id == self.config.channel_id):
            
            try:
                human_delay = random.uniform(2.0, 5.0) # Slower delay for safety
                await asyncio.sleep(human_delay)
                
                if self.config.backup_enabled:
                    await self.log_backup(message)
                
                await self.secure_delete(message)
                self.delete_count += 1
                self.log(f"Auto-deleted message (Total: {self.delete_count})", "SUCCESS")
                
            except Exception as e:
                self.log(f"Error auto-deleting: {e}", "ERROR")

    async def delete_all_messages(self, channel, limit=None, phrase=None, before_date=None):
        """Deletes user's messages from the channel"""
        info_parts = []
        if limit: info_parts.append(f"limit: {limit}")
        if before_date: info_parts.append(f"older than {before_date.strftime('%Y-%m-%d')}")
        
        info_str = ", ".join(info_parts) if info_parts else "ALL history"
        self.log(f"Starting deletion ({info_str})...", "INFO")
        
        deleted = 0
        try:
            async for message in channel.history(limit=None, before=before_date):
                if limit and deleted >= limit:
                    break
                    
                if message.author.id == self.user.id:
                    try:
                        if self.config.backup_enabled:
                            await self.log_backup(message)
                            
                        await self.secure_delete(message)
                        deleted += 1
                        self.delete_count += 1
                        
                        if deleted % 10 == 0:
                            self.log(f"Deleted {deleted} messages...", "INFO")
                            
                        # Dynamic delay based on operation cost
                        base_delay = random.uniform(2.0, 4.0)
                        if self.config.secure_delete:
                            base_delay += random.uniform(1.5, 2.5) # Extra delay for edit operation
                            
                        await asyncio.sleep(base_delay)
                        
                    except Exception as e:
                        if isinstance(e, discord.errors.HTTPException) and e.status == 429:
                             # Rate limit hit, wait significantly longer
                             retry = e.retry_after if hasattr(e, "retry_after") else 10
                             self.log(f"Rate limited! Sleeping for {retry:.1f}s...", "WARNING")
                             await asyncio.sleep(retry + 2)
                        else:
                             self.log(f"Error: {e}", "ERROR")
            
            self.log(f"Completed! Deleted {deleted} messages.", "SUCCESS")
            
        except Exception as e:
            self.log(f"Error fetching history: {e}", "ERROR")

    @tasks.loop(hours=1)
    async def retention_task(self):
        """Background task to enforce retention policy"""
        if self.config.retention_days <= 0:
            return
            
        self.log("Running retention cleanup...", "INFO")
        cutoff = datetime.now() - timedelta(days=self.config.retention_days)
        
        # Determine which channels to clean
        # If we only have one TARGET channel, maybe clean that?
        # Or maybe clean ALL priv channels? The user request implies "bot deletes... from given date", 
        # usually retention implies universal policy or monitored channel. 
        # Safest is monitored channel only for now.
        if self.config.channel_id:
            channel = self.get_channel(self.config.channel_id)
            if channel:
                await self.delete_all_messages(channel, before_date=cutoff)

def print_banner():
    banner = rf"""
{Fore.GREEN}
      .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                     __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.               .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   {Fore.RED}DIE{Fore.GREEN}    `98v8P'  {Fore.RED}HUMAN{Fore.GREEN}   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
{Fore.CYAN}    ULTIMATE DISCORD WIPER v2.0 {Fore.WHITE}| {Fore.GREEN}Created by gh0st
{Fore.MAGENTA}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                      ║
║  "SPEED IS THE ESSENCE OF WAR. TAKE ADVANTAGE OF THE ENEMY'S UNREADINESS."                           ║
║                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)

def main():
    print_banner()
    config = Config()
    
    if not config.user_token:
        print(f"{Fore.RED}ERROR: No USER_TOKEN in config.txt file{Style.RESET_ALL}")
        return
    
    client = DMDeleterBot()
    try:
        client.run(config.user_token)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Shutting down bot...{Style.RESET_ALL}")
        try:
            client.loop.run_until_complete(client.close())
        except:
            pass
        os._exit(0)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
