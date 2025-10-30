import tkinter as tk
import random

# --- 問題データ ---
kanji_questions = {
    "1年生": [
        {"sentence": "大きなイヌ。", "kanji": "大", "reading": "おお"},
        {"sentence": "小さい声。", "kanji": "小", "reading": "ちい"},
        {"sentence": "あめを九つたべた。", "kanji": "九", "reading": "ここの"},
        {"sentence": "男の子のわらいごえ。", "kanji": "男", "reading": "おとこ"},
        {"sentence": "さんすうの学しゅう。", "kanji": "学", "reading": "がく"},
        {"sentence": "日の出をみる。", "kanji": "日", "reading": "ひ"},
        {"sentence": "じてん車をこぐ。", "kanji": "車", "reading": "しゃ"},
        {"sentence": "なつ休み。", "kanji": "休", "reading": "やす"},
        {"sentence": "夕ごはんをたべる。", "kanji": "夕", "reading": "ゆう"},
        {"sentence": "音がくの先生。", "kanji": "音", "reading": "おん"},
    ],
    "2年生": [
        {"sentence": "ともだちに会う。", "kanji": "会", "reading": "あ"},
        {"sentence": "海でおよぐ。", "kanji": "海", "reading": "うみ"},
        {"sentence": "教科書を読む。", "kanji": "教", "reading": "きょう"},
        {"sentence": "頭がいたい。", "kanji": "頭", "reading": "あたま"},
        {"sentence": "ふかい谷。", "kanji": "谷", "reading": "たに"},
        {"sentence": "名前を記す。", "kanji": "記", "reading": "しる"},
        {"sentence": "主語を探す。", "kanji": "語", "reading": "ご"},
        {"sentence": "車が止まる。", "kanji": "止", "reading": "と"},
        {"sentence": "船にのる。", "kanji": "船", "reading": "ふね"},
        {"sentence": "原っぱであそぶ。", "kanji": "原", "reading": "はら"},
    ],
    "3年生": [
        {"sentence": "ゆう名な詩を読む。", "kanji": "詩", "reading": "し"},
        {"sentence": "黄金に輝く金閣寺。", "kanji": "黄金", "reading": "おうごん"},
        {"sentence": "おもしろい物語。", "kanji": "物語", "reading": "ものがたり"},
        {"sentence": "かきが実る。", "kanji": "実", "reading": "みの"},
        {"sentence": "まほうの館。", "kanji": "館", "reading": "やかた"},
        {"sentence": "問いに答える。", "kanji": "問", "reading": "と"},
        {"sentence": "農家のおじさん。", "kanji": "農家", "reading": "のうか"},
        {"sentence": "相手に伝える。", "kanji": "相手", "reading": "あいて"},
        {"sentence": "形を整える。", "kanji": "整", "reading": "ととの"},
        {"sentence": "新たな発見。", "kanji": "発見", "reading": "はっけん"},
    ],
    "4年生": [
        {"sentence": "季節に関する言葉。", "kanji": "季節", "reading": "きせつ"},
        {"sentence": "節目の年。", "kanji": "節", "reading": "ふし"},
        {"sentence": "お米が配給される。", "kanji": "配給", "reading": "はいきゅう"},
        {"sentence": "最も古い寺。", "kanji": "最", "reading": "もっと"},
        {"sentence": "昨日の出来事。", "kanji": "昨日", "reading": "きのう"},
        {"sentence": "信号が赤だ。", "kanji": "信号", "reading": "しんごう"},
        {"sentence": "図書館にある資料。", "kanji": "資料", "reading": "しりょう"},
        {"sentence": "友達とあそぶ。", "kanji": "友達", "reading": "ともだち"},
        {"sentence": "夏休みの半ば。", "kanji": "半", "reading": "なか"},
        {"sentence": "海底の生き物を調査する。", "kanji": "海底", "reading": "かいてい"},
    ],
    "5年生": [
        {"sentence": "学校の校舎。", "kanji": "校舎", "reading": "こうしゃ"},
        {"sentence": "家と学校を往復する。", "kanji": "往復", "reading": "おうふく"},
        {"sentence": "馬が暴れる。", "kanji": "暴", "reading": "あば"},
        {"sentence": "土地を肥やす。", "kanji": "肥", "reading": "こ"},
        {"sentence": "豊かな心情。", "kanji": "情", "reading": "じょう"},
        {"sentence": "明るい態度。", "kanji": "態", "reading": "たい"},
        {"sentence": "司会を任せる。", "kanji": "司会", "reading": "しかい"},
        {"sentence": "画像を加工する。", "kanji": "像", "reading": "ぞう"},
        {"sentence": "原因が分かる。", "kanji": "原因", "reading": "げんいん"},
        {"sentence": "コードを接続する。", "kanji": "接続", "reading": "せつぞく"},
    ],
    "6年生": [
        {"sentence": "姿勢を正す。", "kanji": "姿勢", "reading": "しせい"},
        {"sentence": "胸がドキドキする。", "kanji": "胸", "reading": "むね"},
        {"sentence": "布が垂れ下がる。", "kanji": "垂", "reading": "た"},
        {"sentence": "視線を感じる。", "kanji": "視線", "reading": "しせん"},
        {"sentence": "乱暴な発言だ。", "kanji": "乱暴", "reading": "らんぼう"},
        {"sentence": "テスト範囲を確認する。", "kanji": "確認", "reading": "かくにん"},
        {"sentence": "純白のウエディングドレス。", "kanji": "純白", "reading": "じゅんぱく"},
        {"sentence": "ワクチンを注射する。", "kanji": "注射", "reading": "ちゅうしゃ"},
        {"sentence": "電源を切る。", "kanji": "源", "reading": "げん"},
        {"sentence": "密接な関係。", "kanji": "密接", "reading": "みっせつ"},
    ],
}

# --- アプリ本体 ---
class KanjiDrillApp:
    def __init__(self, master):
        self.master = master
        master.title("🌸 かんじのもり 🌸")
        master.geometry("600x700")
        master.configure(bg="#f4f9f1")
        self.show_menu()

    # メニュー画面
    def show_menu(self):
        for w in self.master.winfo_children(): w.destroy()
        tk.Label(self.master, text="🌳 かんじのもり 🌳", font=("Arial", 28, "bold"), bg="#f4f9f1").pack(pady=40)
        for grade in kanji_questions.keys():
            tk.Button(self.master, text=grade, font=("Arial", 16), bg="#b9e8b5", width=15,
                      command=lambda g=grade: self.start_quiz(g)).pack(pady=6)

    # クイズ開始
    def start_quiz(self, grade):
        self.questions = random.sample(kanji_questions[grade], len(kanji_questions[grade]))
        self.index = 0
        self.show_question()

    # 問題表示
    def show_question(self):
        for w in self.master.winfo_children(): w.destroy()
        q = self.questions[self.index]

        tk.Label(self.master, text=f"({self.index+1}/{len(self.questions)}) のもんだい",
                 font=("Arial", 16), bg="#f4f9f1").pack(pady=20)

        text_box = tk.Text(self.master, font=("Arial", 22), height=3, width=25, bg="#f4f9f1", bd=0)
        text_box.tag_configure("underline", underline=True)
        s, k = q["sentence"], q["kanji"]
        i = s.index(k)
        text_box.insert("1.0", s)
        text_box.tag_add("underline", f"1.{i}", f"1.{i+len(k)}")
        text_box.configure(state="disabled")
        text_box.pack(pady=40)

        # --- プレースホルダー付きEntry ---
        self.entry = tk.Entry(self.master, font=("Arial", 18), fg="gray")
        self.entry.insert(0, "ひらがなで入力してね")
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)

        self.result = tk.Label(self.master, text="", font=("Arial", 16), bg="#f4f9f1")
        self.result.pack(pady=10)

        # --- ボタン類 ---
        self.answer_button = tk.Button(self.master, text="こたえる", bg="#ffeb99", font=("Arial", 16),
                                       command=self.check_answer)
        self.answer_button.pack(pady=10)

        self.next_button = tk.Button(self.master, text="▶ 次へ", bg="#b0d6ff", font=("Arial", 16),
                                     command=self.next_question)
        self.next_button.pack(pady=5)

        # Enterキーでこたえる or 次へ
        self.master.bind("<Return>", self.handle_enter)

        self.entry.focus_set()

    # --- プレースホルダー処理 ---
    def clear_placeholder(self, event):
        if self.entry.get() == "ひらがなで入力してね":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def restore_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "ひらがなで入力してね")
            self.entry.config(fg="gray")

    # --- Enterキー操作 ---
    def handle_enter(self, event):
        if not self.result["text"]:
            self.check_answer()
        else:
            self.next_question()

    # --- 答え合わせ ---
    def check_answer(self):
        q = self.questions[self.index]
        ans = self.entry.get().strip()
        if ans == q["reading"]:
            self.result.config(text="💮 正解！", fg="green")
        else:
            self.result.config(text=f"❌ 不正解！ 正しくは「{q['reading']}」", fg="red")

    # --- 次の問題へ ---
    def next_question(self):
        if self.index + 1 < len(self.questions):
            self.index += 1
            self.show_question()
        else:
            self.show_finish()

    # --- 終了画面 ---
    def show_finish(self):
        for w in self.master.winfo_children(): w.destroy()
        tk.Label(self.master, text="✨おつかれさまでした✨",
                 font=("Arial", 26, "bold"), bg="#f4f9f1").pack(pady=60)
        tk.Button(self.master, text="🏠 メニューにもどる",
                  bg="#b9e8b5", font=("Arial", 18), command=self.show_menu).pack(pady=20)

# --- 起動 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = KanjiDrillApp(root)
    root.mainloop()