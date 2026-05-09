from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser
import google.generativeai as genai

# --- AI CONFIGURATION ---
# നിന്റെ സുരക്ഷയ്ക്കായി API Key ഇവിടെ ചേർക്കാം
GEMINI_KEY = "AIzaSyDc9UeVRumoMS5MDDR96bQTN-Df2HYVYR8"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

class MBrowser(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # 1. സെർച്ച് ബാർ (നിന്റെ സ്റ്റൈലിൽ)
        self.top_bar = BoxLayout(size_hint_y=0.15, spacing=5, padding=10)
        self.url_input = TextInput(
            hint_text='Search or type URL...',
            multiline=False, 
            font_size=18,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.go_btn = Button(
            text='GO', 
            size_hint_x=0.2, 
            background_color=(1, 0, 0, 1) # റെഡ് കളർ
        )
        self.go_btn.bind(on_press=self.handle_search)
        
        self.top_bar.add_widget(self.url_input)
        self.top_bar.add_widget(self.go_btn)
        self.add_widget(self.top_bar)

        # 2. എൻജിൻ സെലക്ഷൻ
        self.engine_bar = BoxLayout(size_hint_y=0.1, spacing=2, padding=5)
        engines = ['Google', 'Gemini AI']
        for eng in engines:
            btn = Button(text=eng, background_color=(0.2, 0.2, 0.2, 1))
            btn.bind(on_press=self.handle_engine)
            self.engine_bar.add_widget(btn)
        self.add_widget(self.engine_bar)

        # 3. ഡിസ്പ്ലേ ഏരിയ (AI മറുപടിക്കായി)
        self.display = Label(
            text="M-BROWSER PRO\nPrivate & Secure", 
            color=(1, 0, 0, 1), 
            font_size=20,
            halign='center'
        )
        self.add_widget(self.display)

    def handle_search(self, instance):
        query = self.url_input.text
        if query:
            # ഡിഫോൾട്ട് ബ്രൗസറിൽ സെർച്ച് ഓപ്പൺ ചെയ്യും
            webbrowser.open(f"https://www.google.com/search?q={query}")

    def handle_engine(self, instance):
        engine = instance.text
        query = self.url_input.text
        
        if engine == 'Gemini AI':
            if not query:
                self.display.text = "Type a question first!"
                return
            try:
                self.display.text = "M-AI is thinking..."
                response = model.generate_content(query)
                self.display.text = response.text
                self.display.font_size = 14
            except Exception:
                self.display.text = "AI Error. Check Internet."
        else:
            self.handle_search(None)

class MBrowserApp(App):
    def build(self):
        return MBrowser()

if __name__ == '__main__':
    MBrowserApp().run()
