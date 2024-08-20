import tkinter as tk
from tkinter import scrolledtext
import requests

# Lyrics.ovh API function
def get_lyrics_ovh(song_title, artist_name):
    base_url = "https://api.lyrics.ovh/v1"
    response = requests.get(f"{base_url}/{artist_name}/{song_title}")
    
    if response.status_code == 200:
        lyrics = response.json().get('lyrics', "Lyrics not found.")
        return lyrics
    else:
        return f"API request failed with status code {response.status_code}."

# Function to fetch and display lyrics
def fetch_lyrics():
    song_title = song_title_entry.get()
    artist_name = artist_name_entry.get()
    lyrics = get_lyrics_ovh(song_title, artist_name)
    lyrics_text.delete(1.0, tk.END)
    lyrics_text.insert(tk.END, lyrics)

# Function to exit the application
def exit_app():
    root.destroy()

# Function to toggle full-screen mode
def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)

# Function to minimize the window
def minimize_window(event=None):
    root.iconify()

# Initialize the GUI
root = tk.Tk()
root.title("Lyrics Extractor")

# Full-screen mode
fullscreen = True
root.attributes('-fullscreen', fullscreen)

# Configure styles
root.configure(bg='#f0f8ff')

# Create a frame for centered layout
frame = tk.Frame(root, bg='#f0f8ff')
frame.pack(expand=True, fill=tk.BOTH)

# Title Label
title_label = tk.Label(frame, text="Lyrics Extractor", font=('Arial', 24, 'bold'), bg='#f0f8ff', fg='#4682b4')
title_label.pack(pady=20)

# Song Title
song_title_label = tk.Label(frame, text="Song Title:", font=('Arial', 14), bg='#f0f8ff', fg='#000080')
song_title_label.pack(anchor='w')
song_title_entry = tk.Entry(frame, width=50, font=('Arial', 14))
song_title_entry.pack(pady=5)

# Artist Name
artist_name_label = tk.Label(frame, text="Artist Name:", font=('Arial', 14), bg='#f0f8ff', fg='#000080')
artist_name_label.pack(anchor='w')
artist_name_entry = tk.Entry(frame, width=50, font=('Arial', 14))
artist_name_entry.pack(pady=5)

# Fetch Lyrics Button
fetch_button = tk.Button(frame, text="Fetch Lyrics", command=fetch_lyrics, font=('Arial', 14), bg='#4682b4', fg='#ffffff', relief='raised', padx=10, pady=5)
fetch_button.pack(pady=20)

# Lyrics Display Area
lyrics_text = scrolledtext.ScrolledText(frame, width=80, height=30, font=('Arial', 12), wrap=tk.WORD)
lyrics_text.pack(padx=20, pady=20)

# Bind keys for full-screen and minimize functionality
root.bind('<F11>', toggle_fullscreen)  # Toggle full-screen with F11 key
root.bind('<Escape>', toggle_fullscreen)  # Exit full-screen with Escape key
root.bind('<Alt-m>', minimize_window)  # Minimize with Alt+M key
root.protocol("WM_DELETE_WINDOW", exit_app)  # Handle window close button

# Run the application
root.mainloop()
