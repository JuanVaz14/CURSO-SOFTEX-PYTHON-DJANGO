class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if "@" not in novo_email:
            print("❌ Erro: o e-mail informado é inválido.")
            return
        self.__email = novo_email
        print("✔️ E-mail atualizado com sucesso!")

class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("Este método precisa ser implementado nas subclasses.")

class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📧 Enviando para servidor de email: {mensagem}")


class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📱 Enviando para operadora telefônica: {mensagem}")

class SistemaAlerta:
    def __init__(self, usuario, canal_envio):
        self.usuario = usuario
        self.canal_envio = canal_envio

    def disparar(self, texto):
        print(f"\n🔔 Enviando alerta para {self.usuario.nome}...")
        self.canal_envio.enviar(texto)

if __name__ == "__main__":
    
    print("\n=== Teste 1: Segurança do e-mail ===")
    usuario = Usuario("João Silva", "joao@gmail.com")

    # Com erro
    print("\nTentando definir um e-mail inválido:")
    usuario.email = "email-invalido"

    # Fucionando
    print("\nAgora definindo um e-mail válido:")
    usuario.email = "novojoao@gmail.com"


    print("\n=== Teste 2: Envio via E-MAIL ===")
    canal_email = Email()
    sistema_email = SistemaAlerta(usuario, canal_email)
    sistema_email.disparar("Seu pagamento foi aprovado!")


    print("\n=== Teste 3: Envio via SMS (Polimorfismo) ===")
    canal_sms = SMS()
    sistema_sms = SistemaAlerta(usuario, canal_sms)
    sistema_sms.disparar("Servidor caiu! Equipe técnica acionada.")
