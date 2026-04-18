import customtkinter as ctk
import random
from tkinter import messagebox

# Configuração de Cores Oficiais
COLOR_BG = "#121213"
COLOR_EMPTY = "#3a3a3c"
COLOR_CORRECT = "#6aaa64"
COLOR_MISPLACED = "#c9b458"
COLOR_WRONG = "#787c7e"
COLOR_TEXT = "#ffffff"

class WordlePro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Wordle Pro - Multi-Mode 2026")
        self.geometry("850x900")
        self.configure(fg_color=COLOR_BG)
        
        # Lista unificada corretamente
        self.full_word_list = [
            # 5 LETRAS
            "ARROZ", "PIZZA", "CARNE", "PASTA", "MESA", "CAMA", "SOFA", "APPLE", 
            "KIWIS", "PERAS", "MELAO", "TESLA", "DADOS", "CLOUD", "LOJAS", "MOUSE",
            "TELA", "FORCA", "PLANO", "MUNDO", "DADOS", "GATOS", "ZEBRA",
            # 6 LETRAS
            "QUEIJO", "BANANA", "TOMATE", "MANGAS", "SOFAS", "MESAS", "CAMAS", 
            "PORTAS", "GOOGLE", "AMAZON", "ADIDAS", "PYTHON", "CODING", "LOGICA", 
            "MOBILE", "DESIGN", "OBJETO", "VARIAV", "STRING", "LISTAS", "TUPLAS",
            "CLASSE", "METODO", "CLIENT", "SERVER", "DOCKER", "TECLADO",
            # 7 LETRAS
            "LARANJA", "BATATA", "SALADA", "CADEIRA", "JANELA", "TAPETE", "ARMARIO", 
            "NETFLIX", "ARQUIVO", "GRAFICO", "SISTEMA", "USUARIO", "MEMORIA", 
            "BOOLEAN", "INTEGER", "DICION", "HERANC", "ATRIBU", "IMPORT", "IFELSE",
            "TRYEXC", "ASSERT", "MODULO", "PROJETO",
            # Extras
            "REPROD", "BROWSE", "FUNCAO"
        ]
        
        self.game_running = False
        self.setup_menu()

    # ... (O restante do seu código permanece igual abaixo)
    def setup_menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(expand=True)

        ctk.CTkLabel(self.menu_frame, text="WORDLE MULTI-MODO", font=("Helvetica", 32, "bold")).pack(pady=20)

        ctk.CTkLabel(self.menu_frame, text="Quantidade de Palavras:").pack()
        self.word_count_var = ctk.IntVar(value=1)
        self.word_count_btn = ctk.CTkSegmentedButton(self.menu_frame, values=["1", "2", "3", "4"],
                                                     command=lambda v: self.word_count_var.set(int(v)))
        self.word_count_btn.set("1")
        self.word_count_btn.pack(pady=(5, 20))

        ctk.CTkLabel(self.menu_frame, text="Tamanho das Letras:").pack()
        self.word_len_var = ctk.IntVar(value=6)
        self.word_len_btn = ctk.CTkSegmentedButton(self.menu_frame, values=["5", "6", "7"],
                                                   command=lambda v: self.word_len_var.set(int(v)))
        self.word_len_btn.set("6")
        self.word_len_btn.pack(pady=(5, 30))

        ctk.CTkButton(self.menu_frame, text="JOGAR AGORA", font=("Helvetica", 16, "bold"),
                      fg_color=COLOR_CORRECT, command=self.start_game).pack()

    def start_game(self):
        self.num_words = self.word_count_var.get()
        self.word_len = self.word_len_var.get()
        
        filtered = [w.upper() for w in self.full_word_list if len(w) == self.word_len]
        self.secret_words = [random.choice(filtered) for _ in range(self.num_words)]
        
        self.max_attempts = self.num_words + 5
        self.current_attempt = 0
        self.current_guess = ""
        self.words_solved = [False] * self.num_words
        self.game_over = False

        self.menu_frame.destroy()
        self.setup_ui()
        self.bind("<Key>", self.handle_keypress)

    def setup_ui(self):
        self.header = ctk.CTkLabel(self, text="WORDLE PRO", font=("Helvetica", 24, "bold"))
        self.header.pack(pady=10)

        self.scroll_container = ctk.CTkScrollableFrame(self, fg_color="transparent", height=450)
        self.scroll_container.pack(fill="both", expand=True, padx=20)

        grid_wrapper = ctk.CTkFrame(self.scroll_container, fg_color="transparent")
        grid_wrapper.pack()
        
        cols = 2 if self.num_words > 1 else 1
        self.all_cells = []

        for w_idx in range(self.num_words):
            w_frame = ctk.CTkFrame(grid_wrapper, fg_color="#1a1a1b", border_width=1, border_color=COLOR_EMPTY)
            w_frame.grid(row=w_idx // cols, column=w_idx % cols, padx=10, pady=10)
            
            ctk.CTkLabel(w_frame, text=f"PALAVRA {w_idx+1}", font=("Arial", 10)).pack()
            
            g_inner = ctk.CTkFrame(w_frame, fg_color="transparent")
            g_inner.pack(padx=5, pady=5)
            
            w_cells = []
            for r in range(self.max_attempts):
                r_cells = []
                for c in range(self.word_len):
                    cell = ctk.CTkLabel(g_inner, text="", width=40, height=40, fg_color=COLOR_EMPTY,
                                        corner_radius=3, font=("Helvetica", 18, "bold"))
                    cell.grid(row=r, column=c, padx=1, pady=1)
                    r_cells.append(cell)
                w_cells.append(r_cells)
            self.all_cells.append(w_cells)

        self.setup_keyboard()

    def setup_keyboard(self):
        self.kbd_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.kbd_frame.pack(side="bottom", pady=20)
        self.key_btns = {}
        
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for i, row in enumerate(rows):
            row_f = ctk.CTkFrame(self.kbd_frame, fg_color="transparent")
            row_f.pack(pady=1)
            
            if i == 2:
                ctk.CTkButton(row_f, text="ENTER", width=60, height=45, font=("Arial", 10, "bold"),
                              fg_color="#565758", command=self.submit_guess).pack(side="left", padx=1)

            for char in row:
                btn = ctk.CTkButton(row_f, text=char, width=38, height=45, font=("Arial", 12, "bold"),
                                   fg_color=COLOR_WRONG, command=lambda c=char: self.add_letter(c))
                btn.pack(side="left", padx=1)
                self.key_btns[char] = btn

            if i == 2:
                ctk.CTkButton(row_f, text="⌫", width=60, height=45, font=("Arial", 14),
                              fg_color="#565758", command=self.delete_letter).pack(side="left", padx=1)

    def handle_keypress(self, event):
        if self.game_over: return
        key = event.keysym.upper()
        if key == "RETURN": self.submit_guess()
        elif key == "BACKSPACE": self.delete_letter()
        elif len(key) == 1 and key.isalpha(): self.add_letter(key)

    def add_letter(self, char):
        if len(self.current_guess) < self.word_len and not self.game_over:
            self.current_guess += char
            self.update_grid()

    def delete_letter(self):
        if len(self.current_guess) > 0:
            self.current_guess = self.current_guess[:-1]
            self.update_grid()

    def update_grid(self):
        for w_idx in range(self.num_words):
            if self.words_solved[w_idx]: continue
            row = self.all_cells[w_idx][self.current_attempt]
            for i, cell in enumerate(row):
                if i < len(self.current_guess):
                    cell.configure(text=self.current_guess[i], fg_color="#565758")
                else:
                    cell.configure(text="", fg_color=COLOR_EMPTY)

    def submit_guess(self):
        if len(self.current_guess) != self.word_len or self.game_over: return
        guess = self.current_guess
        
        for w_idx in range(self.num_words):
            if self.words_solved[w_idx]: continue
            secret = list(self.secret_words[w_idx])
            colors = [COLOR_WRONG] * self.word_len
            
            for i in range(self.word_len):
                if guess[i] == secret[i]:
                    colors[i] = COLOR_CORRECT
                    secret[i] = None
            
            for i in range(self.word_len):
                if colors[i] != COLOR_CORRECT and guess[i] in secret:
                    colors[i] = COLOR_MISPLACED
                    secret[secret.index(guess[i])] = None
            
            for i, color in enumerate(colors):
                self.all_cells[w_idx][self.current_attempt][i].configure(fg_color=color)
                self.update_key_color(guess[i], color)

            if guess == self.secret_words[w_idx]:
                self.words_solved[w_idx] = True

        if all(self.words_solved):
            self.game_over = True
            messagebox.showinfo("Wordle Pro", "VITÓRIA COMPLETA!")
        elif self.current_attempt == self.max_attempts - 1:
            self.game_over = True
            messagebox.showinfo("Wordle Pro", f"GAME OVER!\nPalavras: {', '.join(self.secret_words)}")

        self.current_attempt += 1
        self.current_guess = ""

    def update_key_color(self, char, color):
        if char not in self.key_btns: return
        btn = self.key_btns[char]
        curr = btn.cget("fg_color")
        if curr == COLOR_CORRECT: return
        if curr == COLOR_MISPLACED and color == COLOR_WRONG: return
        btn.configure(fg_color=color)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = WordlePro()
    app.mainloop()