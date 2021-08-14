from engine.glide import StoryMap
from engine.var import Var, Jump

from modules.init import npc, score

description = "Шифрование"

content = StoryMap(
    entry=[
        npc.Magpie.say("вот чёрт"),
        npc.Magpie.say("капец"),
        npc.Floppa.say("Что случилось????"),
        npc.Magpie.say("кажется ребята из нашего дома узнали чо случилось с кроликом"),
        npc.Magpie.say(
            "Привет, это Варвара.\nНам стало известно, что кролика увезли на допрос в отдел полиции по вопросам "
            "миграции. У него отобрали телефон и от его имени написали в чат редакции Сорокиного хвоста. Мы не знаем, "
            "в каком отделении полиции он находится, и что именно ему пытаются вменять."),
        npc.Floppa.say("ЧЕГО"),
        npc.Floppa.say("КАКАЯ ПОЛИЦИЯ"),
        npc.Squirrel.say("Они это серьёзно?"),
        npc.Floppa.say("ЧЕ ПРОИСХОДИТ"),
        npc.Owl.say("Жесть"),
        npc.Owl.say("Но вообще похоже на правду"),
        npc.Floppa.say("ааааааа блин"),
        npc.Squirrel.say("В Хвойном лесу появилось так много новых жителей"),
        npc.Squirrel.say("Полиция не могла это просто так оставить"),
        npc.Floppa.say("Но зачем было Кролика забирать?? Они же его буквально похитили"),
        npc.Floppa.say("Жесть"),
        npc.Floppa.say("А мб это полицейские нам писали от лица Кролика???"),
        npc.Owl.say("Не исключено"),
        npc.Squirrel.say("То есть они просто забрали телефон Кролика и всё???"),
        npc.Squirrel.say("А если с нами такое случится?"),
        npc.Squirrel.say("Мы ведь сотрудничали с Кроликом"),
        npc.Owl.say("Тогда давайте готовиться к этому прямо сейчас, от этого хуже не будет"),
        npc.Owl.say(
            "Первое: отключите на своих телефонах разблокировку по FaceID или по отпечатку пальца, отключите "
            "графический пароль и поставьте символьный минимум из 6 знаков. После этого установите количество попыток "
            "ввода этого самого пароля, если у вас есть такая функция."),
        npc.Magpie.say("но это же дико неудобно"),
        npc.Owl.say(
            "Зато твой телефон будет труднее разблокировать. Бывали случаи, когда телефон отнимали, подносили к лицу "
            "и получали к нему полный доступ."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Squirrel.info(
            "Хорошо! Тогда давайте все поставим себе символьные пароли и установим количество попыток! [Готово]"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("Отлично! Вы ведь запомнили свои пароли? [Запомнили!]"),
        npc.Owl.say(
            "Раз так, то давайте вмест сделаем одну очень важную вещь. Это поможет вам в самый критический момент."),
        npc.Owl.say(
            "Речь идёт об автоудалении данных с ваших смартфонов. Это можно сделать, как на Android, так и на iOS. "),
        npc.Owl.say(
            "Если у вас iOS, то вы можете настроить автоудаление данных после десяти неудачных попыток ввода пароля."),
        npc.Floppa.say("А это не опасно? Вдруг я потеряю самое ценное??"),
        npc.Owl.say("Поэтому нужно не забывать про резервное копирование."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Найти резервное копирование можно прямо в ваших настройках! Посмотрите, как оно устроено и выберите "
            "временной интервал, через который вы бы хотели сохраняться. [Понятно]"),
        npc.Magpie.say("так"),
        npc.Magpie.say("а если у меня андроид?? тогда мои данные могут забрать если они сами не удалятся???"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Тут на помощь приходит шифрование данных! Оно есть и на Android, и на iOS. Зайдите в раздел "
            "'Безопасность' на вашем устройстве и найдите там функцию с шифрованием данных. К сожалению, "
            "ваши устройства будут работать чуть медленнее, но теперь ваши данные будет сложнее прочитать, "
            "если их вытащат из ваших телефонов. [Понятно]"),
        npc.Owl.say("Отлично! Но это ещё не всё."),
        npc.Magpie.say("В СМЫСЛЕ НЕ ВСЁ"),
        npc.Owl.say("Даже если ваш телефон заблорирован и зашифрован, с него можно всё равно кое-что стянуть,"),
        npc.Magpie.say("это как"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Теперь вам нужно найти в настройках вашего устройства отключение уведомлений при заблокированном экране. "
            "[Готово]"),
        npc.Floppa.say("Правильно! Чтобы никто не подсматривал...."),
        npc.Magpie.say("но ведь у меня много инфы лежит на ноуте"),
        npc.Magpie.say("что делать с ноутами и компами? вдруг кто-то залезет ко мне в гнездо"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Тут примерно всё то же самое! Отключите биометрию, если есть, и поставьте пароли для ваших учётных "
            "записей! [Готово]"),
        npc.Owl.say(
            "В ваших компах и ноутах могут быть встроенные сервисы для шифрования: на macOS это FireVault, на Windows "
            "это BitLocker, на Linux VeraCrypt соответственно. VeraCrypt можно использовать и на других платформах."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Вот здесь есть инструкция к VeraCrypt - [https://securityinabox.org/ru/guide/veracrypt/linux/]("
            "https://securityinabox.org/ru/guide/veracrypt/linux/) [Понятно]"),
        npc.Magpie.say("а можно ли сделать что-то ещё?"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Конечно! Вы дополнительно можете запаролить ваши папки, так к вашей важной информации будет ещё труднее "
            "добраться. Это особенно важно, если вы оставляете ваш ноут или комп без присмотра [Понятно]"),
        npc.Floppa.say("Очень круто!!!"),
        npc.Floppa.say("Я сейчас поставлю всё шифроваться"),
        npc.Squirrel.say("Ребята, мы теперь с вами немного защитили себя, но Кролика всё ещё держат в полиции"),
        npc.Floppa.say("Мы можем как-нибудь помочь ему????"),
        npc.Magpie.say("не знаю"),
        npc.Magpie.say("что мы можем сказать полиции???"),
        npc.Magpie.say("мы ведь даже не знаем что там происходит"),
        npc.Floppa.say("Мы должны написать пост в поддержку Кролика!!!"),
        npc.Floppa.say("Вывесим ГИГАНТСКИЙ баннер на сайте"),
        npc.Floppa.say("Будем дуть во все трубы"),
        npc.Magpie.say("как вариант"),
        npc.Squirrel.say("Да"),
        npc.Squirrel.say("Но мы можем конкретно огрести за это"),
        npc.Squirrel.say("С полицией шутки плохи"),
        npc.Magpie.say("но надо попробовать"),
        npc.Magpie.say("мы ведь сделали эту газету чтобы поддерживать других зверей!!!!"),
        npc.Squirrel.say("Я не могу на себя брать такую ответственность"),
        # В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask("Давайте решать вместе, стоит ли нам как изданию поддержать Кролика",
                         [("Поддержать!", "support"), ("Не сообщаем", "not_support")], Var.support_rabbit),
        Jump(Var.support_rabbit)
    ],
    support=[
        #    - ПОСЛЕДСТВИЯ: Поддержать!

        npc.Squirrel.say("Хм"),
        npc.Squirrel.say("Хорошо"),
        npc.Floppa.say("Сейчас нарисую баннер!! САМЫЙ БОЛЬШОЙ!!!!"),
        npc.Floppa.say("Готово!"),
        # В СТРОКЕ НИЖЕ ПОЯВЛЯЕТСЯ ШКАЛА!
        score.add(2),
        npc.Magpie.say("крутяк"),
        npc.Magpie.say("ребята из нашего дома нам супер благодарны"),
        npc.Floppa.say("Чувствую себя рыцарем"),
        npc.Magpie.say("погодите"),
        npc.Magpie.say("ребята пишут что Кролика выпустили!!!!!"),
        npc.Floppa.say("ГРРРРЯЯЯЯ"),
        npc.Floppa.say("Отбили!!!"),
        npc.Magpie.say("не совсем"),
        npc.Magpie.say("блин"),
        npc.Magpie.say("мне так неловко"),
        npc.Magpie.say("они просто беседовали в миграционном отделе"),
        npc.Magpie.say("кроль забыл заполнить какие-то бумажки...."),
        npc.Squirrel.say("Гениально"),
        npc.Magpie.say("они его сегодня смогли выловить и отвезли оформлять доки"),
        npc.Squirrel.say("Тогда кто взломал Кролика?????"),
        npc.Owl.say("Мда"),
        npc.Floppa.say("Сова, что думаешь об этом??"),
        npc.Owl.say("Ну если это были не менты"),
        npc.Floppa.say("???"),
        npc.Owl.say("То тогда это мб были ребята которые слали угрозы нам недавно"),
        npc.Owl.say("Но это только предположение"),
        npc.Floppa.say("Жуть"),
        npc.Magpie.say("мда"),
        npc.Squirrel.say("Да забейте"),
        npc.Squirrel.say("Главное, что всё обошлось"),
        npc.Squirrel.say("Можно хотя бы выдохнуть"),
    ],

    not_support=[
        #    - ПОСЛЕДСТВИЯ: Не поддерживать

        score.add(-2),
        npc.Magpie.say("погодите"),
        npc.Magpie.say("ребята пишут что Кролика выпустили!!!!!"),
        npc.Magpie.say("они просто беседовали в миграционном отделе"),
        npc.Magpie.say("кроль забыл заполнить какие-то бумажки...."),
        npc.Squirrel.say("Гениально"),
        npc.Magpie.say("они его сегодня смогли выловить и отвезли оформлять доки"),
        npc.Magpie.say("но мне всё равно неловко"),
        npc.Magpie.say("даже стыдно"),
        npc.Magpie.say("он всё таки наш товарищ а мы не пришли на помощь"),
        npc.Squirrel.say("Тогда кто взломал Кролика?????"),
        npc.Owl.say("Мда"),
        npc.Floppa.say("Сова, что думаешь об этом??"),
        npc.Owl.say("Ну если это были не менты"),
        npc.Floppa.say("???"),
        npc.Owl.say("То тогда это мб были ребята которые слали угрозы нам недавно"),
        npc.Owl.say("Но это только предположение"),
        npc.Floppa.say("Жуть"),
        npc.Magpie.say("мда"),
        npc.Squirrel.say("Да забейте"),
        npc.Squirrel.say("Главное, что всё обошлось"),
        npc.Squirrel.say("Можно хотя бы выдохнуть"),
        # ЗДЕСЬ     КОНЕЦ ПОСЛЕДСТВИЙ

    ],
)