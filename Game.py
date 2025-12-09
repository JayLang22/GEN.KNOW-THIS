from tkinter import *
import random
from questions import easy_dict, medium_list, hard_list
import pygame
import pickle
from functools import partial

pygame.mixer.init()
pygame.mixer.music.load("bgm1.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

correct_sound = pygame.mixer.Sound("correctfx.wav")
wrong_sound = pygame.mixer.Sound("wrongfx.wav")
wrong_sound.set_volume(0.5)
skip_sound = pygame.mixer.Sound("skipfx.wav")
skip_sound.set_volume(2.0)

LEADERBOARD_FILE = "leaderboardrank.py"


class QuizApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Game")

        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()

        try:
            self.window.state("zoomed")
        except:
            self.window.attributes("-fullscreen", True)

        base_width = 1366
        scale = screen_w / base_width
        self.window.tk.call("tk", "scaling", scale)

        self.window.config(bg="#a8dadc")

        self.title_font = ("Times New Roman", int(30 * scale), "bold")
        self.header_font = ("Times New Roman", int(22 * scale), "bold")
        self.question_font = ("Times New Roman", int(20 * scale))
        self.button_font = ("Times New Roman", int(15 * scale))
        self.small_button_font = ("Times New Roman", int(12 * scale), "bold")
        self.feedback_font = ("Times New Roman", int(14 * scale), "bold")
        self.big_feedback_font = ("Times New Roman", int(36 * scale), "bold")
        self.entry_font = ("Times New Roman", int(15 * scale))
        self.leaderboard_font = ("Times New Roman", int(14 * scale))

        self.bg_img = PhotoImage(file="bg1.png")
        self.bg_label = Label(self.window, image=self.bg_img, bd=0)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.question_color = "#457b9d"
        self.feedback_color = "#1d3557"
        self.button_color = "#f1faee"
        self.button_text = "#1d3557"

        self.score = 0
        self.index = 0
        self.questions = []
        self.diff = ""
        self.buttons = []

        self.main_menu()
        self.window.mainloop()

    def set_background(self):
        self.bg_label = Label(self.window, image=self.bg_img, bd=0)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def styled_button(self, text, font, bg, fg, command):
        return Button(
            self.window,
            text=text,
            font=font,
            bg=bg,
            fg=fg,
            command=command,
            bd=0,
            relief=FLAT,
            highlightthickness=0,
            takefocus=False
        )

    def clean_buttons(self):
        for b in self.buttons:
            b.destroy()
        self.buttons = []

    def hide_feedback(self):
        self.big_feedback_label.config(text="")
        self.big_feedback_label.place_forget()

    def main_menu(self):
        for w in self.window.winfo_children():
            w.destroy()
        self.set_background()

        Label(self.window, text="GEN.KNOW THIS",
              font=self.title_font, bg="#a8dadc",
              fg=self.question_color).pack(pady=40)

        self.styled_button("START", self.button_font,
                           self.button_color, self.button_text,
                           self.build_difficulty).pack(pady=15)

        self.styled_button("LEADERBOARD", self.button_font,
                           self.button_color, self.button_text,
                           self.show_leaderboard).pack(pady=10)

        self.styled_button("EXIT", self.button_font,
                           self.button_color, self.button_text,
                           self.window.destroy).pack(pady=10)

    def build_difficulty(self):
        for w in self.window.winfo_children():
            w.destroy()
        self.set_background()

        Label(self.window, text="Select Difficulty",
              font=self.header_font, bg="#a8dadc",
              fg=self.question_color).pack(pady=20)

        self.styled_button(
            "EASY (True / False)", self.button_font,
            self.button_color, self.button_text,
            partial(self.start_quiz, "easy")
        ).pack(pady=8)

        self.styled_button(
            "MEDIUM (Multiple Choice)", self.button_font,
            self.button_color, self.button_text,
            partial(self.start_quiz, "medium")
        ).pack(pady=8)

        self.styled_button(
            "HARD (Identification)", self.button_font,
            self.button_color, self.button_text,
            partial(self.start_quiz, "hard")
        ).pack(pady=8)

        self.styled_button("BACK", self.button_font,
                           self.button_color, self.button_text,
                           self.main_menu).pack(pady=20)

    def start_quiz(self, diff):
        self.score = 0
        self.index = 0
        self.diff = diff
        self.buttons = []

        for w in self.window.winfo_children():
            w.destroy()
        self.set_background()

        Label(self.window, text="GEN.KNOW THIS",
              font=("Times New Roman", int(14 * self.window.tk.call("tk", "scaling")), "bold"),
              bg="#a8dadc", fg=self.question_color
              ).place(relx=0.01, rely=0.97, anchor="sw")

        if diff == "easy":
            self.questions = random.sample([(q, a, None) for q, a in easy_dict.items()], 10)
        elif diff == "medium":
            self.questions = random.sample(medium_list.to_list(), 10)
        else:
            self.questions = random.sample(hard_list.to_list(), 10)

        self.styled_button("Back", self.small_button_font,
                           "#e63946", "white",
                           self.main_menu).pack(anchor="nw", padx=10, pady=5)

        self.styled_button("Skip", self.small_button_font,
                           "#ffb703", "white",
                           self.skip_question).pack(anchor="ne", padx=10, pady=5)

        self.score_label = Label(self.window, text="Score: 0",
                                 font=self.feedback_font,
                                 bg="#a8dadc",
                                 fg=self.question_color)
        self.score_label.pack(pady=5)

        self.question_label = Label(
            self.window,
            font=self.question_font,
            wraplength=int(900 * self.window.tk.call("tk", "scaling")),
            justify="center",
            bg="#f1faee",
            fg=self.question_color,
            bd=2,
            relief="solid",
            padx=20,
            pady=15
        )
        self.question_label.pack(pady=30, padx=40)

        self.big_feedback_label = Label(self.window,
                                        font=self.big_feedback_font,
                                        bg="#a8dadc")

        if diff == "hard":
            self.entry = Entry(self.window, font=self.entry_font,
                               bd=1, relief="solid")
            self.entry.pack(pady=10)

            self.styled_button("Submit", self.button_font,
                               self.button_color, self.button_text,
                               self.submit_answer).pack(pady=10)

        self.show_question()

    def show_question(self):
        self.clean_buttons()
        q, ans, choices = self.questions[self.index]
        self.current_answer = ans

        self.question_label.config(text=q)
        self.hide_feedback()

        if self.diff == "easy":
            b1 = self.styled_button("TRUE", self.button_font,
                                    "#2a9d8f", "white",
                                    partial(self.check_answer, True))
            b2 = self.styled_button("FALSE", self.button_font,
                                    "#e63946", "white",
                                    partial(self.check_answer, False))
            b1.pack(pady=6)
            b2.pack(pady=6)
            self.buttons.extend([b1, b2])

        elif self.diff == "medium":
            for c in choices:
                b = self.styled_button(
                    c, self.button_font,
                    self.button_color, self.button_text,
                    partial(self.check_answer, c)
                )
                b.pack(pady=5)
                self.buttons.append(b)
        else:
            self.entry.delete(0, END)

    def skip_question(self):
        skip_sound.play()
        self.questions.append(self.questions.pop(self.index))
        self.show_question()

    def submit_answer(self):
        user_input = self.entry.get().strip()
        if not user_input:
            self.big_feedback_label.place(relx=0.5, rely=0.42, anchor="center")
            self.big_feedback_label.lift()
            self.big_feedback_label.config(text="Please enter an answer!", fg="#e63946")
            self.window.after(800, self.hide_feedback)
            return
        self.check_answer(user_input)

    def check_answer(self, user_ans):
        self.big_feedback_label.place(relx=0.5, rely=0.42, anchor="center")
        self.big_feedback_label.lift()

        if str(user_ans).lower().strip() == str(self.current_answer).lower().strip():
            self.score += 1
            self.big_feedback_label.config(text="Correct!", fg="#2a9d8f")
            correct_sound.play()
        else:
            self.big_feedback_label.config(text="Wrong!", fg="#e63946")
            wrong_sound.play()

        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(800, self.hide_feedback)

        if self.index >= 9:
            self.window.after(1000, self.ask_name_for_leaderboard)
        else:
            self.index += 1
            self.window.after(1000, self.show_question)

    def ask_name_for_leaderboard(self):
        for w in self.window.winfo_children():
            w.destroy()
        self.set_background()

        Label(self.window, text=f"Your Score: {self.score}/10",
              font=self.header_font,
              bg="#a8dadc", fg=self.question_color).pack(pady=20)

        self.name_entry = Entry(self.window, font=self.entry_font, bd=1, relief="solid")
        self.name_entry.pack(pady=10)

        self.styled_button("Submit", self.button_font,
                           self.button_color, self.button_text,
                           self.save_to_leaderboard).pack(pady=10)

    def save_to_leaderboard(self):
        name = self.name_entry.get().strip() or "Anonymous"
        try:
            with open(LEADERBOARD_FILE, "rb") as f:
                data = pickle.load(f)
        except:
            data = []

        data.append({"name": name, "difficulty": self.diff, "score": self.score})

        with open(LEADERBOARD_FILE, "wb") as f:
            pickle.dump(data, f)

        self.show_leaderboard()

    def show_leaderboard(self):
        for w in self.window.winfo_children():
            w.destroy()
        self.set_background()

        Label(self.window, text="LEADERBOARD",
              font=self.header_font,
              bg="#a8dadc", fg=self.question_color).pack(pady=20)

        try:
            with open(LEADERBOARD_FILE, "rb") as f:
                data = pickle.load(f)
        except:
            data = []

        if not data:
            Label(self.window, text="No entries yet.",
                  font=self.feedback_font,
                  bg="#a8dadc", fg=self.feedback_color).pack()
        else:
            for i, e in enumerate(data[:10]):
                Label(self.window,
                      text=f"{i+1}. {e['name']} - {e['difficulty'].upper()} - {e['score']}/10",
                      font=self.leaderboard_font,
                      bg="#a8dadc", fg=self.feedback_color
                      ).pack(anchor="w", padx=40)

        self.styled_button("Back", self.button_font,
                           self.button_color, self.button_text,
                           self.main_menu).pack(pady=20)


QuizApp()