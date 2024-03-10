import tkinter as tk
from tkinter import ttk, messagebox

class CredentialsPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Credenciais do Aluno, Para o Exame AZ-900")
        self.root.geometry("500x300")  # Definindo um tamanho maior para a janela

        self.name_label = ttk.Label(root, text="Nome do Aluno:", font=("Arial", 14, "bold"))
        self.name_label.pack(pady=10)

        self.name_entry = ttk.Entry(root)
        self.name_entry.pack(pady=5)

        self.cpf_label = ttk.Label(root, text="CPF do Aluno:", font=("Arial", 14, "bold"))
        self.cpf_label.pack(pady=10)

        self.cpf_entry = ttk.Entry(root)
        self.cpf_entry.pack(pady=5)

        self.next_button = ttk.Button(root, text="Avançar", command=self.start_quiz)
        #self.next_button["font"] = ("Arial", 16, "bold")  # Define a fonte do botão
        self.next_button.pack(pady=10)
        

    def start_quiz(self):
        nome = self.name_entry.get().title()  # Capitaliza as primeiras letras de cada palavra no nome
        cpf = self.cpf_entry.get()

        # Verifica se os campos estão preenchidos
        if nome and cpf:
            self.root.destroy()  # Fecha a janela de credenciais
            quiz_root = tk.Tk()  # Cria a janela principal do quiz
            style = ttk.Style()
            style.configure("TRadiobutton", font=("Arial", 20))
            app = QuizApp(quiz_root, nome, cpf)  # Inicializa o aplicativo do quiz
            quiz_root.mainloop()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

class QuizApp:
    def __init__(self, root, nome, cpf):
        self.root = root
        self.root.title("Azure AZ-900")
        self.nome = nome  # Corrigindo o nome da variável
        self.cpf = cpf

        # Configurar a geometria da janela principal para tela cheia
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        self.root.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.titulo_label = ttk.Label(self.root, text="Simulado Para Treinamento Do Exame - AZ-900", font=("Arial", 25, "bold"))
        self.titulo_label.pack(side="top", fill="x", pady=10)
        self.titulo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.titulo_label.pack(side="top", pady=50)

        self.credentials_label = ttk.Label(self.root, text=f"Nome: {self.nome}\nCPF: {self.cpf}", font=("Arial", 16))
        self.credentials_label.pack(pady=10)

        # Restante do código da prova...
        self.questions = [
            "1. Qual é o serviço de computação em nuvem da Microsoft?",
            "2. O que significa SaaS?",
            "3. Qual dos seguintes é um exemplo de um serviço de nuvem IaaS?",
            "4. Quais são as três categorias principais de serviços de nuvem?",
            "5. Qual serviço de nuvem oferece uma plataforma para desenvolvimento e execução de aplicativos?",
            "6. O que é SLA no contexto de computação em nuvem?",
            "7. Qual dos seguintes é um exemplo de um serviço de nuvem SaaS?",
            "8. Qual é o significado de IaaS?",
            "9. O que significa PaaS?",
            "10. Qual é um exemplo de um serviço de nuvem PaaS?"
        ]

        self.answers = [
            ["a) Azure", "b) AWS", "c) Google Cloud", "d) Oracle Cloud"],
            ["a) Platform as a Service", "b) Software as a Service", "c) Infrastructure as a Service", "d) None of the above"],
            ["a) Azure Virtual Machines", "b) Azure Active Directory", "c) Azure Functions", "d) Azure Blob Storage"],
            ["a) IaaS, PaaS, SaaS", "b) Public, Private, Hybrid", "c) Web, Mobile, Desktop", "d) None of the above"],
            ["a) Azure Functions App Service", "b) Azure Virtual Machines", "c) Azure Active Directory", "d) Azure App Service"],
            ["a) Service Level Agreement", "b) Software License Agreement", "c) Security Logging and Auditing", "d) None of the above"],
            ["a) None of the above", "b) Azure Virtual Machines", "c) Azure Active Directory", "d) Office 365"],
            ["a) Infrastructure as a Service", "b) Platform as a Service", "c) Software as a Service", "d) None of the above"],
            ["a) Process as a Service", "b) Product as a Service", "c) Process as a ServicePlatform as a Service", "d) None of the above"],
            ["a) Azure Functions", "b) Azure App Service", "c) Azure Virtual Machines", "d) None of the above"]
        ]

        self.correct_answers = ["a", "b", "a", "a", "d", "a", "d", "a", "c", "b"]

        self.user_answers = []

        self.current_question_idx = 0

        self.question_label = ttk.Label(root, text=self.questions[self.current_question_idx], font=("Arial", 14, "bold"))
        self.question_label.pack(pady=16)

        self.radio_var = tk.StringVar()

        style = ttk.Style()
        style.configure("TRadiobutton", font=("Arial", 16))

        self.radio_btns = []  # Lista para armazenar os botões de opção

        for i in range(4):
            radio_btn = ttk.Radiobutton(root, text=self.answers[self.current_question_idx][i], variable=self.radio_var, value=chr(97 + i), style="TRadiobutton")
            radio_btn.pack(anchor=tk.W, padx=16)
            self.radio_btns.append(radio_btn)  # Adiciona o botão à lista

        
        self.next_button = ttk.Button(root, text="Próxima", command=self.next_question)
        self.next_button.pack(pady=8)

        self.prev_button = ttk.Button(root, text="Voltar", command=self.prev_question)
        self.prev_button.pack(pady=8)
        self.prev_button.config(state=tk.DISABLED)  # Inicia desabilitado

        self.restart_button = ttk.Button(root, text="Recomeçar", command=self.restart_quiz)
        self.restart_button.pack(pady=8)


        self.review_button = ttk.Button(root, text="Revisar Prova", command=self.review_quiz)
        self.review_button.pack(pady=8)
        self.review_button.config(state=tk.DISABLED)  # Inicia desabilitado

        self.quit_button = ttk.Button(root, text="Sair", command=root.quit)
        self.quit_button.pack(pady=8)

    def next_question(self):
        self.user_answers.append(self.radio_var.get())
        self.current_question_idx += 1

        if self.current_question_idx < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_idx])
            self.radio_var.set("")  # Limpa a seleção do usuário
            for i in range(4):
                self.radio_btns[i].config(text=self.answers[self.current_question_idx][i])  # Atualiza os textos dos botões
            self.prev_button.config(state=tk.NORMAL)  # Habilita o botão Voltar
        else:
            self.next_button.pack_forget()
            self.review_button.config(state=tk.NORMAL)  # Habilita o botão Revisar Prova
            self.restart_button.pack(pady=8)
            self.quit_button.pack(pady=8)
            self.show_score()

    def prev_question(self):
        if self.current_question_idx > 0:
            self.current_question_idx -= 1
            self.question_label.config(text=self.questions[self.current_question_idx])
            self.radio_var.set(self.user_answers[self.current_question_idx])
            for i in range(4):
                self.radio_btns[i].config(text=self.answers[self.current_question_idx][i])  # Atualiza os textos dos botões
            if self.current_question_idx == 0:
                self.prev_button.config(state=tk.DISABLED)  # Desabilita o botão Voltar se estiver na primeira questão

    def review_quiz(self):
        if len(self.user_answers) < len(self.questions):
            messagebox.showinfo("Aviso", "Por favor, finalize a prova antes de revisá-la.")
        else:
            review_text = ""
            for i, (user_ans, correct_ans) in enumerate(zip(self.user_answers, self.correct_answers), start=1):
                if user_ans == correct_ans:
                    review_text += f"Questão {i}: Correta\n"
                else:
                    review_text += f"Questão {i}: Incorreta (Resposta correta: {correct_ans})\n"
            messagebox.showinfo("Revisão da Prova", review_text)

    def restart_quiz(self):
        self.user_answers.clear()
        self.current_question_idx = 0
        self.question_label.config(text=self.questions[self.current_question_idx])
        self.radio_var.set("")
        for i in range(4):
            self.radio_btns[i].config(text=self.answers[self.current_question_idx][i])
        self.next_button.pack(pady=8)
        self.review_button.config(state=tk.DISABLED)  # Desabilita o botão Revisar Prova
        self.prev_button.config(state=tk.DISABLED)  # Desabilita o botão Voltar
        self.restart_button.pack_forget()
        self.quit_button.pack_forget()

    def show_score(self):
        score = sum(1 for user_ans, correct_ans in zip(self.user_answers, self.correct_answers) if user_ans == correct_ans)
        total_questions = len(self.questions)
        messagebox.showinfo("Pontuação", f"Sua pontuação é: {score}/{total_questions}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CredentialsPage(root)
    root.mainloop()
