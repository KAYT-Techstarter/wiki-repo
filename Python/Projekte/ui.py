from tkinter import *
from tkhtmlview import HTMLLabel
# nachinstallieren durch pip install tkhtmlview
# und python3 -m pip install tkhtmlview in der bash

# Hauptfenster erstellen
root = Tk()
root.title("Webseite einbetten")
root.geometry("600x400")

# HTML-Inhalt einbetten
html_content = """
<h1>Willkommen!</h1>
<p>Das ist eine HTML-Seite innerhalb von Tkinter.</p>
<p>Besuche <a href='https://www.google.com'>Google</a> für mehr Informationen.</p>
"""

html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)

# Hauptloop starten
root.mainloop()