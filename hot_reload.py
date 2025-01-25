import tkinter as tk

class ElasticScrollbar(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Elastic Scrollbar Example")
        self.geometry("400x300")

        # Create canvas to contain the scrollable content
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create vertical scrollbar linked to canvas
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold content
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Add content to the frame
        for i in range(50):
            label = tk.Label(self.frame, text=f"Item {i+1}")
            label.pack()

        # Bind the canvas to adjust the scrollbar thumb size dynamically
        self.canvas.bind("<Configure>", self.update_scrollbar)
        self.frame.bind("<Configure>", self.update_scrollbar)

    def update_scrollbar(self, event=None):
        """Update the scrollbar thumb size based on the content height"""
        canvas_height = self.canvas.winfo_height()
        frame_height = self.frame.winfo_height()

        # Adjust the scrollbar thumb size dynamically
        thumb_height = max(canvas_height / frame_height * canvas_height, 20)
        self.scrollbar.config(command=self.canvas.yview, height=thumb_height)

    def elastic_scroll(self):
        """Create the elastic effect by stretching or shrinking the scrollbar thumb"""
        current_thumb_height = self.scrollbar.winfo_height()

        # Find the desired height based on canvas size
        desired_thumb_height = max(min(current_thumb_height + 1, self.canvas.winfo_height() - 20), 20)

        # Stretch or shrink the scrollbar thumb smoothly
        if current_thumb_height != desired_thumb_height:
            self.scrollbar.config(height=desired_thumb_height)
            self.after(50, self.elastic_scroll)  # Repeat the elastic effect

if __name__ == "__main__":
    app = ElasticScrollbar()
    app.after(10, app.elastic_scroll)  # Start the elastic effect after initial setup
    app.mainloop()
