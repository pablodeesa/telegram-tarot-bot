import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

cartas = [
    "Cavaleiro: notícias chegando",
    "Trevo: sorte rápida",
    "Navio: viagens e mudanças",
    "Casa: estabilidade",
    "Árvore: crescimento",
    "Nuvens: confusão",
    "Cobra: inveja e falsidade",
    "Caixão: fim de ciclo",
    "Buquê: alegria e presente",
    "Foice: corte repentino",
    "Chicote: conflitos",
    "Pássaros: ansiedade",
    "Criança: novidade",
    "Raposa: cuidado com engano",
    "Urso: força e proteção",
    "Estrela: esperança",
    "Cegonha: mudanças positivas",
    "Cão: amizade",
    "Torre: isolamento",
    "Jardim: socialização",
    "Montanha: obstáculos",
    "Caminhos: decisões",
    "Ratos: perda",
    "Coração: amor",
    "Aliança: união",
    "Livro: segredo",
    "Carta: mensagem",
    "Homem: energia masculina",
    "Mulher: energia feminina",
    "Lírios: paz",
    "Sol: sucesso",
    "Lua: emoções",
    "Chave: solução",
    "Peixes: dinheiro",
    "Âncora: estabilidade",
    "Cruz: destino"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Digite /tirar para ver sua carta 🔮")

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos:\n/start\n/ajuda\n/tirar")

# 🔮 FUNÇÃO QUE FALTAVA
async def tirar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    carta = random.choice(cartas)
    await update.message.reply_text(f"🔮 Sua carta:\n{carta}")
async def tirar6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selecionadas = random.sample(cartas, 6)

    passado = selecionadas[:2]
    presente = selecionadas[2:4]
    futuro = selecionadas[4:]
    
    resposta = "🔮 Leitura Cigana 🔮\n\n"

    resposta += "🕰️ Passado:\n"
    for c in passado:
        resposta += f"- {c}\n"

    resposta += "\n⚡ Presente:\n"
    for c in presente:
        resposta += f"- {c}\n"

    resposta += "\n🔮 Futuro:\n"
    for c in futuro:
        resposta += f"- {c}\n"

    resposta += "\n✨ Interpretação:\n"

    if any("Cobra" in c or "Ratos" in c for c in selecionadas):
        resposta += "Há inveja ou desgaste ao seu redor.\n"

    if any("Sol" in c or "Chave" in c for c in selecionadas):
        resposta += "Caminhos estão se abrindo.\n"

    if any("Coração" in c or "Aliança" in c for c in selecionadas):
        resposta += "Amor em destaque.\n"

    resposta += "\n🧿 Conselho:\nConfie na sua intuição."

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ajuda", ajuda))
app.add_handler(CommandHandler("tirar", tirar))  # <-- ESSA LINHA FALTAVA
app.add_handler(CommandHandler("tirar6", tirar6)
)
print("Bot Online Laroye ...")
app.run_polling()
