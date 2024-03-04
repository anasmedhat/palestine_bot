from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6365740550:AAGQL5ImpBOC02ayWeYXzqjH6xaUpS7BE8c'
BOT_USERNAME: Final = '@abo3obaida23bot'

questions = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Shohada ", callback_data='shohada')],
        [InlineKeyboardButton("Years", callback_data='years')],
        [InlineKeyboardButton("Palestine Breif History", callback_data='history')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Alslam alaykum this is abo 3obaida, I will help you know more about the Palestinian history \n \n  what do you want to know more about?',
        reply_markup=reply_markup)



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    response_text = "You can start using this bot by typing /start and then select the info you want to know about."
    await update.message.reply_text(response_text)



async def new_information_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can type your new information here ')
    questions[update.message.chat.id] = None



def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'alsalam alaykum' in processed:
        return 'walykum alsalam'
    if 'what is your name' in processed:
        return 'abo 3obaida'
    if '2016' in processed:
        return ('Israeli forces have killed more Palestinian children in the occupied West Bank, including East Jerusalem, in 2016 than any other year in the last decade, rights group Defence for Children International (DCI) has said. '
                'The organisation’s chapter in the occupied Palestinian territories recorded the killings of 32 Palestinian children (under 18), making 2016 “the deadliest year of the past decade” for them, the group said in a recent report.')
    if '2018' in processed:
        return ('Palestinians have experienced no respite from the Israeli occupation, let alone a breakthrough of ending it. Although no full-scale war broke out in 2018, as some had expected, it did bring a grim year of deadly violence, illegal settlement expansion and home demolitions.  \n At least 289 Palestinians – men, women and children – were killed throughout 2018, while thousands of others were wounded, including many who were maimed for life by Israeli gunfire. According to the Defense for Children organisation, the death toll includes 56 Palestinian children – an average of more than one child every week.')
    if 'the balfour declaration' in processed:
        return 'The Israeli-Palestinian issue goes back nearly a century when Britain, during World War I, pledged to establish a national home for the Jewish people in Palestine under the Balfour Declaration. British troops took control of the territory from the Ottoman Empire at the end of October 1917.'
    if 'jewish immigration to palestine' in processed:
        return 'A large-scale Jewish migration to Palestine began, accelerated by Jewish people fleeing Nazism in Europe. Between 1918 and 1947, the Jewish population in Palestine increased from 6 percent to 33 percent.   Palestinians were alarmed by the demographic change and tensions rose, leading to the Palestinian revolt from 1936 to 1939. Meanwhile, Zionist organisations continued to campaign for a homeland for Jews in Palestine. Armed Zionist militias started to attack the Palestinian people, forcing them to flee. Zionism, which emerged as a political ideology in the late 19th century, called for the creation of a Jewish homeland.'
    if 'blockade of gaza' in processed:
        return 'Israel imposed a blockade on Gaza in 2007 after the Hamas group came to power. The siege continues till date. Israel also occupies the West Bank and East Jerusalem – the territories Palestinians want to be part of their future state. Israel imposed a total blockade on the Gaza Strip on October 9, cutting its supplies of electricity, food, water, and fuel in the wake of a surprise Hamas attack inside Israel. At least 1,200 people were killed in that attack.'

    if '/newinformation' in processed:
        return
    return 'Unfortunately we have not added this topic yet, You can tell us more about it using /newinformation, it can be added later inshallah'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type != 'private':
        questions[update.message.chat.id] = text
        await update.message.reply_text('Thank you for adding more information it will be saved for later processing.')
        return

    if BOT_USERNAME in text:
        new_text: str = text.replace(BOT_USERNAME, '').strip()
        response: str = handle_response(new_text)
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

    if update.message.chat.id in questions and questions[update.message.chat.id] is None:
        with open("questions.txt", "a") as file:
            file.write(text + "\n")
        await update.message.reply_text('Thank you for adding more information it will be saved for later processing.')




async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    query.answer()
    if query.data == 'shohada':
        keyboard = [
            [InlineKeyboardButton("Tayseer Muhammad Abu Taima", callback_data='tayseer')],
            [InlineKeyboardButton("Ahmed Adeeb Alyan", callback_data='ahmed')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('Select a Shaheed:', reply_markup=reply_markup)
    elif query.data == 'years':
        keyboard = [
            [InlineKeyboardButton("2016", callback_data='2016')],
            [InlineKeyboardButton("2018", callback_data='2018')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('Select a year:', reply_markup=reply_markup)
    elif query.data == 'history':
        keyboard = [
            [InlineKeyboardButton("1. The Balfour Declaration (1917)", callback_data='the balfour declaration')],
            [InlineKeyboardButton("2. Jewish immigration to Palestine (1918 - 1947)", callback_data='jewish immigration to palestine')],
            [InlineKeyboardButton("3. The UN Partition Plan (1947)",callback_data='The UN Partition Plan')],
            [InlineKeyboardButton("4. The Nakba (1948 - 1980)", callback_data='The Nakba')],
            [InlineKeyboardButton("5. The Oslo Accords (1993)", callback_data='The Oslo Accords')],
            [InlineKeyboardButton("6. Blockade of Gaza (2007)", callback_data='Blockade of Gaza')],
            [InlineKeyboardButton("7. Palestine now (2008 - 2023)", callback_data='Palestine now')]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('select an event:', reply_markup=reply_markup)


#Shohada
    elif query.data == 'tayseer':
        message = """The Shaheed Tayseer Abu Taima, known as the “Alshaheed alsajed,” is a Palestinian resistance fighter who chose to bid farewell to life while prostrating to God after suffering serious wounds as a result of being targeted by a missile by the occupation forces. His targeting by the occupation forces’ aircraft was documented and the video was published as a form of gloating, but it is God’s will. Their plot prevailed, so the video became a reason to raise the memory of the martyr Abu Ta’imah and immortalize his biography and sacrifice.

    The Shaheed, as mentioned, is a memorizer of the Book of God. He is a member of the Al-Huffaz Brigade. He is also the imam of the Palestine Mosque in Bani Suhaila in Gaza, and the emir of an elite faction in the Al-Qassam Brigades in the Khan Yunis Brigade."""
        await query.message.reply_text(message)
    elif query.data == 'ahmed':
        # Provide information for Ahmed Adeeb Alyan if needed
        pass


# Years
    elif query.data == '2016':
        message = """"Israeli forces have killed more Palestinian children in the occupied West Bank, including East Jerusalem, in 2016 than any other year in the last decade, rights group Defence for Children International (DCI) has said.

The organisation’s chapter in the occupied Palestinian territories recorded the killings of 32 Palestinian children (under 18), making 2016 “the deadliest year of the past decade” for them, the group said in a recent report. """
        await query.message.reply_text(message)

    elif query.data == '2018':
        message = """"In 2018 Palestinians have experienced no respite from the Israeli occupation, let alone a breakthrough of ending it. Although no full-scale war broke out in 2018, as some had expected, it did bring a grim year of deadly violence, illegal settlement expansion and home demolitions.

At least 289 Palestinians – men, women and children – were killed throughout 2018, while thousands of others were wounded, including many who were maimed for life by Israeli gunfire. According to the Defense for Children organisation, the death toll includes 56 Palestinian children – an average of more than one child every week."""
        await query.message.reply_text(message)



# Events
    elif query.data == 'the balfour declaration':
        message = """The Israeli-Palestinian issue goes back nearly a century when Britain, during World War I, pledged to establish a national home for the Jewish people in Palestine under the Balfour Declaration. British troops took control of the territory from the Ottoman Empire at the end of October 1917. """
        await query.message.reply_text(message)
    elif query.data == 'jewish immigration to palestine':
        message = """ A large-scale Jewish migration to Palestine began, accelerated by Jewish people fleeing Nazism in Europe. Between 1918 and 1947, the Jewish population in Palestine increased from 6 percent to 33 percent.   Palestinians were alarmed by the demographic change and tensions rose, leading to the Palestinian revolt from 1936 to 1939. Meanwhile, Zionist organisations continued to campaign for a homeland for Jews in Palestine. Armed Zionist militias started to attack the Palestinian people, forcing them to flee. Zionism, which emerged as a political ideology in the late 19th century, called for the creation of a Jewish homeland."""
        await query.message.reply_text(message)
    elif query.data == 'The UN Partition Plan':
        message = """As violence ravaged Palestine, the matter was referred to the newly formed United Nations. In 1947, the UN adopted Resolution 181, which called for the partition of Palestine into Arab and Jewish states, handing over about 55 percent of the land to Jews. Arabs were granted 45 percent of the land, while Jerusalem was declared a separate internationalised territory.
        The city is currently divided between West Jerusalem, which is predominantly Jewish, and East Jerusalem with a majority Palestinian population. Israel captured East Jerusalem after the Six-Day War in 1967 along with the West Bank – a step not recognised by the international community.
        The Old City in occupied East Jerusalem holds religious significance for Christians, Muslims, and Jews. It is home to Al-Aqsa Mosque compound, which is known to Muslims as al-Haram al-Sharif and to Jews as Temple Mount."""
        await query.message.reply_text(message)
    elif query.data == 'The Nakba':
        message = """Leading up to Israel’s birth in 1948, more than 750,000 Palestinians were ethnically cleansed from their homes by Zionist militias. This mass exodus came to be known as the Nakba or catastrophe.

A further 300,000 Palestinians were displaced by the Six-Day War in 1967.
Israel declared the annexation of East Jerusalem in 1980, but the international community still considers it an occupied territory. Palestinians want East Jerusalem as the capital of their future state."""
        await query.message.reply_text(message)
    elif query.data == 'The Oslo Accords':
        message = """In 1993, Palestinian leader Yasser Arafat and Israeli Prime Minister Yitzhak Rabin signed the Oslo Accords, which aimed to achieve peace within five years. It was the first time the two sides recognised each other.
        In 1993, Palestinian leader Yasser Arafat and Israeli Prime Minister Yitzhak Rabin signed the Oslo Accords, which aimed to achieve peace within five years. It was the first time the two sides recognised each other."""
        await query.message.reply_text(message)
    elif query.data == 'Blockade of Gaza':
        message = """Israel imposed a blockade on Gaza in 2007 after the Hamas group came to power. The siege continues till date. Israel also occupies the West Bank and East Jerusalem – the territories Palestinians want to be part of their future state. Israel imposed a total blockade on the Gaza Strip on October 9, cutting its supplies of electricity, food, water, and fuel in the wake of a surprise Hamas attack inside Israel. At least 1,200 people were killed in that attack."""
        await query.message.reply_text(message)
    elif query.data == 'Palestine now':
        message = """Today, about 5 million Palestinians live in Gaza, the West Bank and East Jerusalem and 1.6 million Palestinians are citizens of Israel. This makes up about half of their total population. The other half lives in other countries, including Arab countries. There are about 14.7 million Jews around the world today, of which 84 percent live in Israel and the United States. The rest live in other countries including France, Canada, Argentina and Russia"""
        await query.message.reply_text(message)





if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('newinformation', new_information_command))

    # Adding the button handler
    app.add_handler(CallbackQueryHandler(button))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
