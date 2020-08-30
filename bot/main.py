from telegram.ext import Updater

updater = Updater(token='', use_context=True)

def main():
    dp = updater.dispatcher

    updater.start_polling()

    updater.idle()

    updater.stop()

if __name__ == '__main__':
    main()