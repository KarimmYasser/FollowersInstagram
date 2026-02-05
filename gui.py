import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import threading
from pathlib import Path

class InstagramFollowersGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Followers Analyzer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # File paths
        self.followers_file = tk.StringVar()
        self.following_file = tk.StringVar()
        
        # Create and pack the main interface
        self.create_widgets()
        
        # Center the window
        self.center_window()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Instagram Followers Analyzer", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # File selection section
        file_frame = ttk.LabelFrame(main_frame, text="Select Files", padding="10")
        file_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        # Followers file selection
        ttk.Label(file_frame, text="Followers JSON:").grid(row=0, column=0, sticky=tk.W, pady=2)
        followers_entry = ttk.Entry(file_frame, textvariable=self.followers_file, state="readonly")
        followers_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=2)
        ttk.Button(file_frame, text="Browse", 
                  command=lambda: self.browse_file(self.followers_file, "Select Followers JSON")).grid(row=0, column=2, pady=2)
        
        # Following file selection
        ttk.Label(file_frame, text="Following JSON:").grid(row=1, column=0, sticky=tk.W, pady=2)
        following_entry = ttk.Entry(file_frame, textvariable=self.following_file, state="readonly")
        following_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=2)
        ttk.Button(file_frame, text="Browse", 
                  command=lambda: self.browse_file(self.following_file, "Select Following JSON")).grid(row=1, column=2, pady=2)
        
        # Analyze button
        self.analyze_button = ttk.Button(main_frame, text="Analyze Followers", 
                                        command=self.analyze_followers)
        self.analyze_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, 
                                                     width=70, height=20, state=tk.DISABLED)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Please select your Instagram JSON files")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def browse_file(self, var, title):
        """Open file dialog to select JSON file"""
        filename = filedialog.askopenfilename(
            title=title,
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            var.set(filename)
            self.update_status("File selected: " + Path(filename).name)
    
    def update_status(self, message):
        """Update the status bar"""
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def update_results(self, text):
        """Update the results text area"""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, text)
        self.results_text.config(state=tk.DISABLED)
    
    def analyze_followers(self):
        """Start the analysis in a separate thread"""
        if not self.followers_file.get() or not self.following_file.get():
            messagebox.showerror("Error", "Please select both followers and following JSON files.")
            return
        
        # Disable button and start progress
        self.analyze_button.config(state=tk.DISABLED)
        self.progress.start()
        self.update_status("Analyzing followers...")
        
        # Run analysis in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self.run_analysis)
        thread.daemon = True
        thread.start()
    
    def run_analysis(self):
        """Run the actual analysis"""
        try:
            # Load followers
            self.update_status("Loading followers...")
            followers = self.load_followers(self.followers_file.get())
            
            # Load following
            self.update_status("Loading following...")
            following = self.load_following(self.following_file.get())
            
            # Analyze
            self.update_status("Analyzing data...")
            not_following_back = [user for user in following if user not in followers]
            
            # Prepare results
            results = f"📊 INSTAGRAM FOLLOWERS ANALYSIS\n"
            results += f"{'='*50}\n\n"
            results += f"✅ Total following: {len(following)}\n"
            results += f"✅ Total followers: {len(followers)}\n"
            results += f"📈 Follow ratio: {len(followers)/len(following):.2f}\n\n"
            
            results += f"🚫 Users not following you back ({len(not_following_back)}):\n"
            results += f"{'-'*40}\n"
            
            if not_following_back:
                for i, user in enumerate(not_following_back, 1):
                    results += f"{i:3d}. {user}\n"
            else:
                results += "🎉 Everyone you follow is following you back!\n"
            
            # Update GUI in main thread
            self.root.after(0, lambda: self.analysis_complete(results))
            
        except Exception as e:
            error_msg = f"Error during analysis: {str(e)}"
            self.root.after(0, lambda: self.analysis_error(error_msg))
    
    def analysis_complete(self, results):
        """Called when analysis is complete"""
        self.progress.stop()
        self.analyze_button.config(state=tk.NORMAL)
        self.update_results(results)
        self.update_status("Analysis complete!")
    
    def analysis_error(self, error_msg):
        """Called when analysis encounters an error"""
        self.progress.stop()
        self.analyze_button.config(state=tk.NORMAL)
        messagebox.showerror("Analysis Error", error_msg)
        self.update_status("Analysis failed - check your files and try again")
    
    def extract_username(self, data_entry):
        """Extract username from string_list_data entry.
        Can handle both formats:
        - {value: "username", ...}
        - {href: "https://www.instagram.com/_u/username", ...}
        """
        # First try to get the value field directly
        if "value" in data_entry:
            return data_entry["value"]
        
        # If not, try to extract from href
        href = data_entry.get("href", "")
        if href:
            # Handle both URL formats
            if "/_u/" in href:
                return href.split('/_u/')[-1]
            else:
                # Format: https://www.instagram.com/username
                return href.split('/')[-1]
        
        return None
    
    def load_followers(self, path):
        """Load followers from JSON file"""
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            usernames = []
            for entry in data:
                if "string_list_data" in entry and entry["string_list_data"]:
                    username = self.extract_username(entry["string_list_data"][0])
                    if username:
                        usernames.append(username)
            return usernames
    
    def load_following(self, path):
        """Load following from JSON file"""
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            following_data = data.get("relationships_following", [])
            usernames = []
            for entry in following_data:
                if "string_list_data" in entry and entry["string_list_data"]:
                    username = self.extract_username(entry["string_list_data"][0])
                    if username:
                        usernames.append(username)
            return usernames

def main():
    root = tk.Tk()
    app = InstagramFollowersGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()