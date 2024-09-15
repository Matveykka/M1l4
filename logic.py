
import requests


# Функция для получения изображения покемона
def get_pokemon_image(pokemon_name):
    # Запрос к PokéAPI для получения данных о покемоне
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

    if response.status_code == 200:
        data = response.json()
        # Извлекаем url изображения покемона
        image_url = data['sprites']['front_default']
        return image_url
    else:
        return None


# Функция для обработки команды /pokemon
def pokemon(update: Update, context: CallbackContext) -> None:
    if context.args:
        pokemon_name = context.args[0]
        image_url = get_pokemon_image(pokemon_name)

        if image_url:
            update.message.reply_photo(photo=image_url)
        else:
            update.message.reply_text("Извините, покемон не найден.")
    else:
        update.message.reply_text("Пожалуйста, укажите название покемона.")


def main() -> None:
    # Замените 'YOUR_TOKEN' на токен вашего бота
    updater = Updater("7337477267:AAGwbNNaOHzz5O9Q-1Yj6YkYnvygJJh2mH4")

    # Получаем диспатчер для регистрации хэндлеров
    dispatcher = updater.dispatcher

    # Регистрация хэндлера для команды /pokemon
    dispatcher.add_handler(CommandHandler("pokemon", pokemon))

    # Запуск бота
    updater.start_polling()

    # Ожидаем остановку
    updater.idle()


if __name__ == '__main__':
    main()


