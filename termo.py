"""
WORDLE PRO - Multi-Mode 2026
Desenvolvido por: LUIS GUILHERME G.B. E OTAVIO CESAR

Banco de palavras carregado de: words_db.json
"""

import customtkinter as ctk
import random
import json
import os
from tkinter import messagebox

# ============================================================
#  CORES
# ============================================================

COLOR_BG         = "#121213"
COLOR_EMPTY      = "#3a3a3c"
COLOR_CORRECT    = "#6aaa64"
COLOR_MISPLACED  = "#c9b458"
COLOR_WRONG      = "#787c7e"
COLOR_TEXT       = "#ffffff"
COLOR_ACCENT     = "#6aaa64"

SAVE_FILE  = "wordle_stats.json"
WORDS_FILE = "words_db.json"


# ============================================================
#  JOGO PRINCIPAL
# ============================================================

class WordlePro(ctk.CTk):

    # --------------------------------------------------------
    #  INICIALIZAÇÃO
    # --------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.title("Wordle Pro — Multi-Mode 2026")
        self.geometry("880x900")
        self.configure(fg_color=COLOR_BG)

        self.stats    = self._load_stats()
        self.word_db  = self._load_word_db()

        self._show_menu()

    # --------------------------------------------------------
    #  BANCO DE PALAVRAS EXTERNO
    # --------------------------------------------------------

    def _load_word_db(self) -> dict:
        """
        Carrega words_db.json do mesmo diretório do script.
        Retorna um dict  {tamanho_str: [lista_de_palavras]}.
        Se o arquivo não existir, grava um banco mínimo de fallback.
        """
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), WORDS_FILE)

        if not os.path.exists(db_path):
            # Fallback embutido – cria o arquivo automaticamente
            fallback = {
                "5": ["ARROZ","CARNE","PASTA","PRAIA","ZEBRA",
                      "SONHO","CHUVA","VERDE","NOITE","FELIZ"],
                "6": ["QUEIJO","BANANA","TOMATE","JANELA","CIDADE",
                      "HABITO","PADRAO","ORIGEM","BRILHO","MESTRE"],
                "7": ["FAMILIA","JORNADA","VITORIA","TALENTO","SUCESSO",
                      "PROJETO","MEMORIA","ESPELHO","SAUDADE","DESTINO"],
            }
            try:
                with open(db_path, "w", encoding="utf-8") as f:
                    json.dump(fallback, f, ensure_ascii=False, indent=2)
                messagebox.showinfo(
                    "Banco de palavras",
                    f"'{WORDS_FILE}' não encontrado.\n"
                    f"Um banco mínimo foi criado em:\n{db_path}"
                )
            except Exception as e:
                messagebox.showwarning("Aviso", f"Não foi possível criar o banco de palavras:\n{e}")
            return fallback

        try:
            with open(db_path, "r", encoding="utf-8") as f:
                raw: dict = json.load(f)

            # Normaliza: chaves como str, palavras em maiúsculas e sem duplicatas
            cleaned = {}
            for key, words in raw.items():
                size     = str(key)
                wordlist = list({w.upper().strip() for w in words if isinstance(w, str)})
                # Mantém apenas palavras com o tamanho exato declarado na chave
                wordlist = [w for w in wordlist if len(w) == int(size)]
                if wordlist:
                    cleaned[size] = sorted(wordlist)
            return cleaned

        except Exception as e:
            messagebox.showerror("Erro ao carregar banco", str(e))
            return {}

    def _get_words_for_size(self, size: int) -> list[str]:
        """Retorna a lista de palavras para o tamanho dado."""
        return self.word_db.get(str(size), [])

    # --------------------------------------------------------
    #  PERSISTÊNCIA DE ESTATÍSTICAS
    # --------------------------------------------------------

    def _load_stats(self) -> dict:
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"jogos": 0, "vitorias": 0, "sequencia": 0, "melhor_seq": 0}

    def _save_stats(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.stats, f)

    # --------------------------------------------------------
    #  MENU PRINCIPAL
    # --------------------------------------------------------

    def _show_menu(self):
        self._clear_window()
        self.configure(fg_color=COLOR_BG)
        self.geometry("880x900")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=40, pady=20)

        # ── Cabeçalho ──────────────────────────────────────────────────────────
        header = ctk.CTkFrame(scroll, fg_color="#1a1a1b", corner_radius=16)
        header.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(header, text="WORDLE PRO",
                     font=("Helvetica", 52, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=(24, 0))
        ctk.CTkLabel(header, text="MULTI  MODE  2026",
                     font=("Consolas", 14),
                     text_color="#555555").pack()

        sep = ctk.CTkFrame(header, height=2, fg_color=COLOR_ACCENT)
        sep.pack(fill="x", padx=40, pady=(8, 0))

        # Estatísticas
        stats_row = ctk.CTkFrame(header, fg_color="transparent")
        stats_row.pack(pady=(8, 20))

        for label, value in [
            ("JOGOS",     str(self.stats["jogos"])),
            ("VITÓRIAS",  str(self.stats["vitorias"])),
            ("SEQUÊNCIA", str(self.stats["sequencia"])),
            ("RECORDE",   str(self.stats["melhor_seq"])),
        ]:
            col = ctk.CTkFrame(stats_row, fg_color="#111113", corner_radius=10,
                               width=90, height=70)
            col.pack(side="left", padx=8)
            col.pack_propagate(False)
            ctk.CTkLabel(col, text=value,
                         font=("Consolas", 24, "bold"),
                         text_color="white").place(relx=0.5, rely=0.38, anchor="center")
            ctk.CTkLabel(col, text=label,
                         font=("Consolas", 9),
                         text_color="#555555").place(relx=0.5, rely=0.75, anchor="center")

        # ── Status do banco de palavras ────────────────────────────────────────
        db_frame = ctk.CTkFrame(scroll, fg_color="#1a1a1b", corner_radius=16)
        db_frame.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(db_frame, text="BANCO DE PALAVRAS",
                     font=("Helvetica", 18, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=(16, 8), padx=24, anchor="w")

        total = sum(len(v) for v in self.word_db.values())
        db_info_row = ctk.CTkFrame(db_frame, fg_color="transparent")
        db_info_row.pack(padx=24, pady=(0, 16), fill="x")

        for size in ["5", "6", "7"]:
            count = len(self.word_db.get(size, []))
            col = ctk.CTkFrame(db_info_row, fg_color="#111113", corner_radius=10,
                               width=100, height=64)
            col.pack(side="left", padx=6)
            col.pack_propagate(False)
            ctk.CTkLabel(col, text=str(count),
                         font=("Consolas", 20, "bold"),
                         text_color="white").place(relx=0.5, rely=0.35, anchor="center")
            ctk.CTkLabel(col, text=f"{size} LETRAS",
                         font=("Consolas", 9),
                         text_color="#555555").place(relx=0.5, rely=0.75, anchor="center")

        ctk.CTkLabel(db_frame,
                     text=f"  Total: {total} palavras  ·  Fonte: {WORDS_FILE}",
                     font=("Consolas", 11),
                     text_color="#444444").pack(pady=(0, 12), padx=24, anchor="w")

        # ── Como jogar ─────────────────────────────────────────────────────────
        how_frame = ctk.CTkFrame(scroll, fg_color="#1a1a1b", corner_radius=16)
        how_frame.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(how_frame, text="COMO JOGAR",
                     font=("Helvetica", 18, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=(16, 8), padx=24, anchor="w")

        rules = [
            (COLOR_CORRECT,   "🟩", "Letra CERTA na posição CERTA"),
            (COLOR_MISPLACED, "🟨", "Letra existe, mas está no lugar ERRADO"),
            (COLOR_WRONG,     "⬛", "Letra NÃO existe na palavra secreta"),
        ]
        for color, emoji, text in rules:
            row = ctk.CTkFrame(how_frame, fg_color="transparent")
            row.pack(fill="x", padx=24, pady=3)
            ind = ctk.CTkFrame(row, width=24, height=24, fg_color=color, corner_radius=4)
            ind.pack(side="left")
            ind.pack_propagate(False)
            ctk.CTkLabel(row, text=f"  {emoji}  {text}",
                         font=("Consolas", 13),
                         text_color="#cccccc").pack(side="left")

        ctk.CTkLabel(how_frame,
                     text="  Digite uma palavra e pressione ENTER. Você tem 6 tentativas!",
                     font=("Consolas", 11), text_color="#555555").pack(
                         pady=(4, 16), padx=24, anchor="w")

        # ── Configurações da partida ────────────────────────────────────────────
        cfg_frame = ctk.CTkFrame(scroll, fg_color="#1a1a1b", corner_radius=16)
        cfg_frame.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(cfg_frame, text="CONFIGURAR PARTIDA",
                     font=("Helvetica", 18, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=(16, 12), padx=24, anchor="w")

        ctk.CTkLabel(cfg_frame, text="Quantas palavras simultâneas?",
                     font=("Consolas", 13),
                     text_color="#888888").pack(padx=24, anchor="w")

        self.word_count_var = ctk.IntVar(value=1)
        wc_btn = ctk.CTkSegmentedButton(cfg_frame, values=["1", "2", "3", "4"],
                                        selected_color=COLOR_ACCENT,
                                        selected_hover_color="#4d8b50",
                                        command=lambda v: self.word_count_var.set(int(v)))
        wc_btn.set("1")
        wc_btn.pack(padx=24, pady=(6, 14), fill="x")

        # Só exibe os tamanhos disponíveis no banco
        available_sizes = sorted(
            [s for s in ["5", "6", "7"] if self.word_db.get(s)],
            key=int
        )
        if not available_sizes:
            available_sizes = ["5", "6", "7"]

        ctk.CTkLabel(cfg_frame, text="Tamanho das palavras?",
                     font=("Consolas", 13),
                     text_color="#888888").pack(padx=24, anchor="w")

        default_size = available_sizes[1] if len(available_sizes) > 1 else available_sizes[0]
        self.word_len_var = ctk.IntVar(value=int(default_size))

        wl_btn = ctk.CTkSegmentedButton(cfg_frame, values=available_sizes,
                                        selected_color=COLOR_ACCENT,
                                        selected_hover_color="#4d8b50",
                                        command=lambda v: self.word_len_var.set(int(v)))
        wl_btn.set(default_size)
        wl_btn.pack(padx=24, pady=(6, 20), fill="x")

        # ── Botão Jogar ─────────────────────────────────────────────────────────
        ctk.CTkButton(scroll, text="▶   JOGAR AGORA",
                      font=("Helvetica", 20, "bold"),
                      fg_color=COLOR_ACCENT,
                      hover_color="#4d8b50",
                      text_color="black",
                      height=60, corner_radius=12,
                      command=self._start_game).pack(fill="x", pady=(0, 20))

    # --------------------------------------------------------
    #  INÍCIO DO JOGO
    # --------------------------------------------------------

    def _start_game(self):
        self.num_words = self.word_count_var.get()
        self.word_len  = self.word_len_var.get()

        filtered = self._get_words_for_size(self.word_len)
        if not filtered:
            messagebox.showerror(
                "Sem palavras",
                f"Nenhuma palavra de {self.word_len} letras encontrada em '{WORDS_FILE}'.\n"
                "Adicione palavras ao banco e reinicie o jogo."
            )
            return

        self.secret_words    = [random.choice(filtered) for _ in range(self.num_words)]
        self.max_attempts    = self.num_words + 5
        self.current_attempt = 0
        self.current_guess   = ""
        self.words_solved    = [False] * self.num_words
        self.game_over       = False

        self.stats["jogos"] += 1
        self._save_stats()

        self._clear_window()
        self.configure(fg_color=COLOR_BG)
        self._setup_game_ui()
        self.bind("<Key>", self._handle_keypress)

    # --------------------------------------------------------
    #  UI DO JOGO
    # --------------------------------------------------------

    def _setup_game_ui(self):
        hud = ctk.CTkFrame(self, fg_color="#1a1a1b", height=52, corner_radius=0)
        hud.pack(fill="x")
        hud.pack_propagate(False)

        ctk.CTkButton(hud, text="← MENU",
                      font=("Consolas", 12), width=90, height=34,
                      fg_color="transparent", text_color="#555555",
                      hover_color="#222222",
                      command=self._show_menu).pack(side="left", padx=12, pady=8)

        ctk.CTkLabel(hud, text="WORDLE PRO",
                     font=("Helvetica", 22, "bold"),
                     text_color=COLOR_ACCENT).pack(side="left", expand=True)

        info_text = (
            f"{self.num_words} palavra{'s' if self.num_words > 1 else ''} · "
            f"{self.word_len} letras · {self.max_attempts} tentativas"
        )
        ctk.CTkLabel(hud, text=info_text,
                     font=("Consolas", 11),
                     text_color="#444444").pack(side="right", padx=16)

        ctk.CTkFrame(self, height=1, fg_color="#333333").pack(fill="x")

        self.scroll_container = ctk.CTkScrollableFrame(self, fg_color="transparent", height=440)
        self.scroll_container.pack(fill="both", expand=True, padx=20, pady=10)

        grid_wrapper = ctk.CTkFrame(self.scroll_container, fg_color="transparent")
        grid_wrapper.pack()

        cols           = 2 if self.num_words > 1 else 1
        self.all_cells = []

        for w_idx in range(self.num_words):
            w_frame = ctk.CTkFrame(grid_wrapper, fg_color="#1a1a1b",
                                   border_width=1, border_color="#2a2a2c",
                                   corner_radius=12)
            w_frame.grid(row=w_idx // cols, column=w_idx % cols, padx=10, pady=10)

            ctk.CTkLabel(w_frame, text=f"PALAVRA {w_idx + 1}",
                         font=("Consolas", 10),
                         text_color="#444444").pack(pady=(8, 4))

            g_inner = ctk.CTkFrame(w_frame, fg_color="transparent")
            g_inner.pack(padx=8, pady=(0, 8))

            w_cells = []
            for r in range(self.max_attempts):
                r_cells = []
                for c in range(self.word_len):
                    cell = ctk.CTkLabel(g_inner, text="", width=42, height=42,
                                        fg_color=COLOR_EMPTY, corner_radius=4,
                                        font=("Helvetica", 18, "bold"))
                    cell.grid(row=r, column=c, padx=2, pady=2)
                    r_cells.append(cell)
                w_cells.append(r_cells)
            self.all_cells.append(w_cells)

        self._setup_keyboard()

    def _setup_keyboard(self):
        self.kbd_frame = ctk.CTkFrame(self, fg_color="#111113", corner_radius=0)
        self.kbd_frame.pack(side="bottom", fill="x", pady=0)

        ctk.CTkFrame(self.kbd_frame, height=1, fg_color="#333333").pack(fill="x")

        inner = ctk.CTkFrame(self.kbd_frame, fg_color="transparent")
        inner.pack(pady=12)

        self.key_btns = {}
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

        for i, row in enumerate(rows):
            row_f = ctk.CTkFrame(inner, fg_color="transparent")
            row_f.pack(pady=2)

            if i == 2:
                ctk.CTkButton(row_f, text="ENTER", width=65, height=46,
                              font=("Arial", 10, "bold"),
                              fg_color="#565758", hover_color="#686969",
                              corner_radius=6,
                              command=self._submit_guess).pack(side="left", padx=2)

            for char in row:
                btn = ctk.CTkButton(row_f, text=char, width=38, height=46,
                                    font=("Arial", 13, "bold"),
                                    fg_color=COLOR_WRONG,
                                    hover_color="#606060",
                                    corner_radius=6,
                                    command=lambda c=char: self._add_letter(c))
                btn.pack(side="left", padx=2)
                self.key_btns[char] = btn

            if i == 2:
                ctk.CTkButton(row_f, text="⌫", width=65, height=46,
                              font=("Arial", 15),
                              fg_color="#565758", hover_color="#686969",
                              corner_radius=6,
                              command=self._delete_letter).pack(side="left", padx=2)

    # --------------------------------------------------------
    #  INPUT
    # --------------------------------------------------------

    def _handle_keypress(self, event):
        if self.game_over:
            return
        key = event.keysym.upper()
        if   key == "RETURN":    self._submit_guess()
        elif key == "BACKSPACE": self._delete_letter()
        elif len(key) == 1 and key.isalpha(): self._add_letter(key)

    def _add_letter(self, char: str):
        if len(self.current_guess) < self.word_len and not self.game_over:
            self.current_guess += char
            self._update_grid()

    def _delete_letter(self):
        if self.current_guess:
            self.current_guess = self.current_guess[:-1]
            self._update_grid()

    def _update_grid(self):
        for w_idx in range(self.num_words):
            if self.words_solved[w_idx]:
                continue
            row = self.all_cells[w_idx][self.current_attempt]
            for i, cell in enumerate(row):
                if i < len(self.current_guess):
                    cell.configure(text=self.current_guess[i],
                                   fg_color="#565758", text_color="white")
                else:
                    cell.configure(text="", fg_color=COLOR_EMPTY)

    # --------------------------------------------------------
    #  AVALIAÇÃO DO PALPITE
    # --------------------------------------------------------

    def _submit_guess(self):
        if len(self.current_guess) != self.word_len or self.game_over:
            return

        guess = self.current_guess

        for w_idx in range(self.num_words):
            if self.words_solved[w_idx]:
                continue

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
                self.all_cells[w_idx][self.current_attempt][i].configure(
                    fg_color=color, text_color="white"
                )
                self._update_key_color(guess[i], color)

            if guess == self.secret_words[w_idx]:
                self.words_solved[w_idx] = True
                try:
                    frame = self.all_cells[w_idx][0][0].master.master
                    for child in frame.winfo_children():
                        if isinstance(child, ctk.CTkLabel):
                            child.configure(text_color=COLOR_CORRECT)
                            break
                except Exception:
                    pass

        self.current_attempt += 1
        self.current_guess = ""

        if all(self.words_solved):
            self.game_over = True
            self.stats["vitorias"]  += 1
            self.stats["sequencia"] += 1
            if self.stats["sequencia"] > self.stats["melhor_seq"]:
                self.stats["melhor_seq"] = self.stats["sequencia"]
            self._save_stats()
            self.after(400, lambda: self._show_result(True))

        elif self.current_attempt >= self.max_attempts:
            self.game_over = True
            self.stats["sequencia"] = 0
            self._save_stats()
            self.after(400, lambda: self._show_result(False))

    def _update_key_color(self, char: str, color: str):
        if char not in self.key_btns:
            return
        btn  = self.key_btns[char]
        curr = btn.cget("fg_color")
        if curr == COLOR_CORRECT:
            return
        if curr == COLOR_MISPLACED and color == COLOR_WRONG:
            return
        btn.configure(fg_color=color)

    # --------------------------------------------------------
    #  TELA DE RESULTADO
    # --------------------------------------------------------

    def _show_result(self, won: bool):
        win = ctk.CTkToplevel(self)
        win.title("Resultado")
        win.geometry("380x300")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()
        win.configure(fg_color="#1a1a1b")

        accent = COLOR_CORRECT if won else "#FF4444"

        ctk.CTkFrame(win, height=4, fg_color=accent, corner_radius=0).pack(fill="x")

        emoji  = "🎉" if won else "😔"
        titulo = "VITÓRIA COMPLETA!" if won else "GAME OVER"
        ctk.CTkLabel(win, text=f"{emoji}  {titulo}",
                     font=("Helvetica", 26, "bold"),
                     text_color=accent).pack(pady=(20, 8))

        ctk.CTkFrame(win, height=1, fg_color="#333333").pack(fill="x", padx=30)

        if not won:
            palavras = "  ·  ".join(self.secret_words)
            ctk.CTkLabel(win, text="As palavras eram:",
                         font=("Consolas", 12),
                         text_color="#666666").pack(pady=(12, 2))
            ctk.CTkLabel(win, text=palavras,
                         font=("Consolas", 15, "bold"),
                         text_color="white").pack()

        stats_row = ctk.CTkFrame(win, fg_color="transparent")
        stats_row.pack(pady=16)
        for label, val in [
            ("Jogos",    self.stats["jogos"]),
            ("Vitórias", self.stats["vitorias"]),
            ("Sequência",self.stats["sequencia"]),
        ]:
            col = ctk.CTkFrame(stats_row, fg_color="#111113", corner_radius=8,
                               width=80, height=58)
            col.pack(side="left", padx=6)
            col.pack_propagate(False)
            ctk.CTkLabel(col, text=str(val),
                         font=("Consolas", 20, "bold"),
                         text_color="white").place(relx=0.5, rely=0.35, anchor="center")
            ctk.CTkLabel(col, text=label,
                         font=("Consolas", 9),
                         text_color="#555555").place(relx=0.5, rely=0.75, anchor="center")

        btn_frame = ctk.CTkFrame(win, fg_color="transparent")
        btn_frame.pack(fill="x", padx=24, pady=(0, 20))

        ctk.CTkButton(
            btn_frame, text="⟳  NOVA PARTIDA",
            font=("Arial", 13, "bold"),
            fg_color=accent, text_color="black", height=42,
            command=lambda: [win.destroy(), self._start_game()]
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_frame, text="🏠  MENU",
            font=("Arial", 13, "bold"),
            fg_color="#0d0d0d", text_color="#888888",
            border_color="#333333", border_width=1, height=42,
            command=lambda: [win.destroy(), self._show_menu()]
        ).pack(side="left", expand=True, fill="x", padx=(6, 0))

    # --------------------------------------------------------
    #  UTILITÁRIOS
    # --------------------------------------------------------

    def _clear_window(self):
        self.unbind("<Key>")
        for w in self.winfo_children():
            w.destroy()


# ============================================================
#  ENTRADA
# ============================================================

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = WordlePro()
    app.mainloop()
