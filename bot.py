# bot.py
# AxisHub / Escreva.me | Bot de Vendas Oficiais
# Stack: pyTelegramBotAPI (telebot) - simples e estável

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")


# -----------------------------
# Menus (Inline Keyboards)
# -----------------------------
def main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("📚 Conhecer o Escreva.me", callback_data="CONHECER"),
        InlineKeyboardButton("💎 Planos e Acesso", callback_data="PLANOS"),
        InlineKeyboardButton("⚙️ Plataformas do AxisHub", callback_data="PLATAFORMAS"),
        InlineKeyboardButton("💬 Suporte", callback_data="SUPORTE"),
    )
    return kb


def back_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="MENU"))
    return kb


def plano_unico_menu() -> InlineKeyboardMarkup:
    # Coloque aqui o SEU link Kiwify do plano R$29,90
    link_plano = url="https://pay.kiwify.com.br/iQG1j4Y"

    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("✅ Liberar acesso (R$ 29,90/mês)", url=link_plano),
        InlineKeyboardButton("💬 Falar com Suporte", callback_data="SUPORTE"),
        InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="MENU"),
    )
    return kb


# -----------------------------
# /start
# -----------------------------
@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "👋 Olá! Sou o bot oficial do *AxisHub*.\n\n"
        "Escolha uma opção abaixo para conhecer o *Escreva.me* e liberar acesso."
    )
    bot.send_message(message.chat.id, text, reply_markup=main_menu())


# -----------------------------
# Callback Handler (botões)
# -----------------------------
@bot.callback_query_handler(func=lambda call: True)
def on_callback(call):
    data = call.data
    chat_id = call.message.chat.id

    # MENU
    if data == "MENU":
        text = (
            "👋 Olá! Sou o bot oficial do *AxisHub*.\n\n"
            "Escolha uma opção abaixo para conhecer o *Escreva.me* e liberar acesso."
        )
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=main_menu(),
        )
        return

    # CONHECER
    if data == "CONHECER":
        text = (
            "📚 *Escreva.me*\n\n"
            "Uma plataforma para escritoras criarem com mais velocidade e qualidade.\n\n"
            "• Editor IA\n"
            "• Revisão e organização\n"
            "• Ferramentas criativo-editoriais\n\n"
            "Quer ver planos e liberar acesso?"
        )
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=back_menu(),
        )
        return

    # PLANOS
    if data == "PLANOS":
        text = (
            "💎 *Plano Oficial Escreva.me*\n\n"
            "💰 *R$ 29,90 / mês*\n\n"
            "✅ Editor IA para escrita criativa\n"
            "✅ Clareza, ritmo e estrutura de texto\n"
            "✅ Escrita com constância (sem bloqueio)\n\n"
            "🔓 Clique abaixo e libere seu acesso agora:"
        )
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=plano_unico_menu(),
        )
        return

    # PLATAFORMAS
    if data == "PLATAFORMAS":
        text = (
            "⚙️ *Ecossistema AxisHub*\n\n"
            "• *Escreva.me* — escrita criativa com IA\n"
            "• *AxisHub* — central de projetos e automações\n\n"
            "A ideia é simples: um hub que vende e entrega."
        )
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=back_menu(),
        )
        return

    # SUPORTE
    if data == "SUPORTE":
        # Você pode trocar por um @seu_user ou link
        text = (
            "💬 *Suporte*\n\n"
            "Para liberar acesso e tirar dúvidas, fale com o suporte.\n\n"
            "👉 Responda aqui no Telegram ou envie mensagem para o responsável."
        )
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=back_menu(),
        )
        return


# -----------------------------
# Rodar
# -----------------------------
if __name__ == "__main__":
    print("Bot iniciado. Pressione Ctrl+C para parar.")
    bot.infinity_polling()

