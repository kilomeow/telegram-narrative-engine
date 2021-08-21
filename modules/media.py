from engine.glide import StoryMap
from engine.var import Var, Proceed, Jump

from modules.init import npc, score, docs

description = "Социальные сети и мессенджеры"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Сорока, вы там готовы?"),
        npc.Magpie.say("да мы почти закончили"),
        npc.Floppa.say("УРА"),
        npc.Floppa.say("Это ведь материалы про лагерь погорельцев, в котором работает Кролик, да??"),
        npc.Rabbit.say("так точно"),
        npc.Rabbit.say("мы на месте ещё"),
        npc.Floppa.say("Как там сейчас?"),
        npc.Rabbit.say("если честно, то очень тяжело"),
        npc.Rabbit.say("здесь очень много пострадавших, и у нас проблемы с водой"),
        npc.Floppa.say("Жеееесть сил вам!!"),
        npc.Rabbit.say("спасибо!"),
        npc.Squirrel.say("ВНИМАНИЕ"),
        npc.Squirrel.say(
            "Жду редактуру! Нужно сделать источники анонимными (Наш дом это НЕ анонимная организация, мы про них и пишем, если что, можете считать это партнёрским материалом), если они есть, и убрать авторские примечания "
            "в скобках"),
        npc.Squirrel.say(docs['note1']),
        npc.Floppa.say("Да! И не забывайте советоваться друг с другом в чятике"),
        npc.Floppa.say("Командная работа это не пельмени варить"),
        npc.Floppa.say("Хотя..."),
        npc.Squirrel.say("Мне сейчас срочно надо развесить грибы сушиться"),
        npc.Squirrel.ask("Напишите готово, когда закончите, и я тут же вернусь", [("Готово", "ready")], Var.null),

        score.add(3),

        npc.Magpie.say("тут нам прислали кое-что"),
        npc.Floppa.say("ЧТО?????"),
        npc.Magpie.say("кое-что неприятное"),
        npc.Magpie.say("я не уверена что новеньким стоит это читать"),
        npc.Floppa.say("Там что-то жуткое?"),
        npc.Magpie.say("вы новенькие меня поймите я тут давно уже и всякого насмотрелась"),
        npc.Magpie.say("но мне бы не хотелось чтобы вы воспринимали это как-то близко к сердцу"),
        npc.Floppa.say("ДА ЧТО ТАМ"),
        npc.Magpie.ask("хорошо но не пугайтесь особо", [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""Вы хотели привлечь внимание и вы его привлекли. Не все здесь хотят видеть немытых""" +
                        """мигрантов у себя под окнами. Скажите вашим пушистым друзьям, чтобы сворачивали свои""" +
                        """палатки и шли в другое 
место, пока мы их не нашли. Мы не станем кормить их за свой счет. Ровно так же, как и вашу газетёнку. 

Прекращайте этот балаган немедленно. """),
        npc.Rabbit.say("вот об этом я и говорил"),
        npc.Squirrel.say("Так, и что делаем? Мы продолжаем?"),
        npc.Rabbit.say("ну я пока ничего страшного не вижу"),
        npc.Rabbit.say("чем больше зверей узнают о нас, тем лучше"),
        npc.Magpie.say("зверей и птиц прошу заметить"),
        npc.Rabbit.say("короче, я о том, что не важно че там пишут"),
        npc.Rabbit.say("ладно, давайте следующую заметку тогда"),
        npc.Rabbit.say(docs["note2"]),  # вот он тут, я не знаю, почему его нет в игре
        npc.Rabbit.say(
            "вот этот текст вычитайте прям очень внимательно, пожалуйста, я торопился и мог что-то проглядеть"),
        npc.Squirrel.say("Работаем! "),
        npc.Squirrel.say("Ребята-зверята, Кролик не убрал пару примечаний за собой, найдите их и уберите, пожалуйста."),
        npc.Squirrel.ask('Закончили?', [("Готово", "ready")], Var.null),

        score.add(3),
        npc.Magpie.say(".........."),
        npc.Magpie.say("они не унимаются"),
        npc.Magpie.say("видимо нас читают бескультурные звери которым нечем заняться "),
        npc.Magpie.say("нам в бота снова присылают гадости"),
        npc.Magpie.say("теперь тут прямо лично про меня"),
        npc.Magpie.ask("очень мерзко", [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""```Привет, Сорока! Я уже купил спички и собираюсь устроить пикник недалеко от леса! Скажи ты 
любишь загорать? Если да то тебе понравится гореть будет очень ярко! А потом я обязательно зайду к вам в 
гости я слышал что вы любите всякие горячие новости а будет очень горячо.... 

З.Ы. Передавай обгоревшим уродам привет```"""),
        npc.Rabbit.say("забей"),
        npc.Rabbit.say("это тупо какой-то третьеклассник писал"),
        npc.Floppa.say("Буквы в интернете ещё никого не убивали"),
        npc.Magpie.say("ну это как посмотреть"),
        npc.Magpie.say("я раньше часто с таким сталкивалась когда вела блог"),
        npc.Magpie.say("и это каждый раз было одинаково неприятно"),
        npc.Magpie.say("я бы сказала что подобные вещи убивают тебя но постепенно"),
        npc.Magpie.say("тип это всё накапливается а потом ты вообще ничего не можешь делать"),
        npc.Rabbit.say("всмы не можешь??? типа боишься или как??"),
        npc.Magpie.say("не знаю как объяснить"),
        npc.Magpie.say("ну то есть ты вот хочешь написать огромный пост тебе прямо это очень нужно но ты не можешь"),
        npc.Magpie.say("потому что вот это вот всё в комментах просто забирает твои силы"),
        npc.Floppa.say("Мне кажется, что к этому нужно просто привыкнуть???? Ну это же им надо, чтобы ты ничего не писала, а не тебе. Поэтому ты просто сжимаешь клюв до скрипа и дешаешь вещи дальше!"),
        Proceed(photo=True)
    ],

    photo=[
        npc.Rabbit.info("а вот сейчас я реально напрягся"),
        npc.Rabbit.say("выложил в инсту фотографию лагеря, и в комменты набежали какие-то типы"),
        npc.Rabbit.say("никогда не видел столько хейта"),
        npc.Rabbit.say("пишут, что хотят всё сжечь"),
        npc.Floppa.say("Посмотри на юзернеймы, наверняка боты"),
        npc.Floppa.say(
            "Не переживай, такое часто случается! Даже если это живые люди, такие обычно сидят дома и "
            "ничего не делают)"),
        npc.Magpie.say("ТЫ ЗАЧЕМ ВЫЛОЖИЛ "),
        npc.Magpie.say("разве не ты просил меня не писать где лагерь??"),
        npc.Floppa.say("Да всё нормально! Вряд ли вас кто-то вычислит по веткам))"),
        npc.Magpie.say("уже"),
        npc.Magpie.say("вот что пишут в телеграм-канале Чистый Лес:"),
        npc.Magpie.info(""" ```Мы уже оперативно вычислили всех, кто сочувствует облезлому Сорокиному хвосту. Их имена и 
адреса установлены, их любимая газетёнка даже не думала их спасать. Мы настоятельно рекомендуем всем, 
кто хочет открыть свою пасть, немедленно её заткнуть ради своей же безопасности.```"""),
        npc.Rabbit.say("шо за экстремальные типы???"),
        npc.Floppa.say("ЭТО ВАЩЕ КТО"),
        npc.Rabbit.say("пусть только попробуют я им блин все хвосты повыдёргиваю"),
        npc.Magpie.say("это короче наши родные ретарды"),
        npc.Rabbit.say("раз на раз без маек на траве"),
        npc.Magpie.say("они уже давно топят за Хвойный лес для хвойнослесных "),
        npc.Magpie.say("я не знаю как это описать"),
        npc.Magpie.say("но они раньше подобным не промышляли"),
        npc.Squirrel.say("Спокойно"),
        npc.Squirrel.say("Как они вообще это сделали???"),
        npc.Squirrel.say("Сова, что теперь делать?"),
        npc.Owl.say(
            "Это обычная ситуация, Кролику не стоило выкладывать эту фотографию в общий доступ. Сейчас обнаружить то "
            "или иное место по окружению достаточно легко: это может быть и вид из окна, и какое-то строение на фоне, "
            "что угодно."),
        npc.Rabbit.say("на фотку попал огромный дуб"),
        npc.Rabbit.say("блин реально его же все в лесу знают"),
        npc.Rabbit.say("как я мог так факапнуться"),
        npc.Rabbit.say("капец"),
        npc.Owl.say(
            "Кролик, бери лапы в лапы и беги к нотариусу. Тебе нужен *«Акт осмотра страницы в сети «Интернет»* двух "
            "этих скриншотов с угрозами*.* Жалобу в телеграм я уже отправил, хотя это может ни на что не повлиять."),
        npc.Owl.say(
            "Можно было бы ещё обратиться в полицию, но я не уверена, что они будут что-то предпринимать, тут будем "
            "действовать по ситуации"),
        npc.Rabbit.say("мне сейчас реально нужно бежать к нотариусу???"),
        npc.Owl.say("ДА"),
        npc.Squirrel.say("Да!"),
        npc.Rabbit.say("ладно ладно"),
        npc.Rabbit.say("побежал!!"),
        npc.Squirrel.say("А нам что делать? Тут и про нас есть!"),
        npc.Owl.say("Ну тут надо пораскинуть мозгами"),
        npc.Owl.say(
            "Наверное, вы сейчас можете сообщить об угрозах читателям, это сто проц привлечет внимание. Но с другой стороны, "
            "недоброжелателей так тоже можно спровоцировать."),
        npc.Magpie.say("хммм"),
        npc.Floppa.say("Как это в шахматах назвается??"),
        npc.Floppa.say("Точно, вилка!"),
        npc.Squirrel.say("Нужно подумать, это очень серьёзная ситуация. Давайте проголосуем."),
        npc.Squirrel.ask("У вас только одно нажатие!", [("Сообщаем", "public"), ("Не сообщаем", "not_public")],
                         Var.threat_public),
        Jump(Var.threat_public)
    ],
    # ЗДЕСЬ———————игроки голосуют———————

    # ПОСЛЕДСТВИЯ: Сообщаем

    public=[
        npc.Squirrel.say("Ух"),
        npc.Magpie.say("хорошо! я подготовлю заявление и скоро отправлю"),
        score.add(2),
        npc.Squirrel.say("У поста очень много просмотров! Наверное, это хорошо..."),
        npc.Floppa.say("Вы молодцы!"),
        npc.Magpie.say("в бот приходит очень много слов поддержки"),
        npc.Magpie.say("мне даже как-то легче стало"),
        npc.Squirrel.say("Это хорошо. А теперь работаем дальше!"),
        Proceed(threat=True)
    ],

    not_public=[
        npc.Squirrel.say("Ладно, будем следить за ситуацией"),
        npc.Floppa.say("Правильно! Им нельзя давать никакую публичность"),
        npc.Floppa.say("Кролик напишет заявление и пусть полиция с ними говорит"),
        npc.Magpie.say("если заявление вообще примут"),
        npc.Squirrel.say("В любом случае работаем дальше"),
        Proceed(threat=True)
    ],
    threat=[
        npc.Magpie.say("блин"),
        npc.Magpie.say("эти придурки поджигатели распугали моих респондентов"),
        npc.Magpie.say("посмотрите"),
        npc.Magpie.say("```Мы уже оперативно вычислили всех, кто сочувствует облезлому Сорокиному хвосту. Их имена и "
                       "адреса установлены, их любимая газетёнка даже не думала их спасать.```"
                       "```Мы настоятельно рекомендуем всем, кто хочет открыть свою пасть, немедленно её заткнуть ради "
                       "своей же безопасности.```"),
        npc.Magpie.say("они правда нашли адреса?"),
        npc.Owl.say(
            "Возможно. Как я и говорил, найти личные данные любого пользователя проще, чем кажется. Пара фотографий, "
            "общие друзья, один лайк под постом и всё, вас сцапали."),
        npc.Floppa.say("рррррр"),
        npc.Magpie.say("ну а я-то тут причем"),
        npc.Magpie.say("как мне доказать что со мной можно безопасно разговаривать??"),
        npc.Owl.say("В телеграме для этого есть несколько важных функций."),
        npc.Owl.info(
            "Первое - это *сикрет-чаты.* В них информация не хранится на серверах, а пересылается между собеседниками "
            "лично, в них используется сквозное шифрование. **В таких чатах есть *удаление сообщений по таймеру*. "),
        npc.Owl.say("Сейчас во всех чатах можно настроить автоудаление, никогда не забывайте об этом."),
        npc.Floppa.say("Только тут ничего не удаляйте, пожалуйста...."),
        npc.Owl.info(
            "В телеграме можно не показывать свой номер никому, кроме тех, у кого он уже записан, а вот ```Signal``` "
            "позволяет использовать вообще любой номер телефона, делая общение практически анонимным для третьих лиц, "
            "и в нём есть все те же функции: от автоудаления до сквозного шифрования. Кроме того, у него полностью "
            "открытый код, и мы точно знаем, как именно он работает. Например, он точно-точно не собирает метаданные!"),
        npc.Owl.info(
            "Ещё есть такая штука, как ```Delta Chat```! Она полностью децентрализована, а чтобы ей пользоваться нужна "
            "всего лишь электронная почта! Более того, твои сообщения дойдут даже в том случае, если у адресата не "
            "стоит ```Delta Chat```. Но я вынуждена сказать, что эта штучка работает только для незащищённых почт, "
            "так что будьте внимательны!"),
        npc.Magpie.say("хмм неплохо"),
        npc.Magpie.say("надеюсь это поможет"),
        npc.Owl.say(
            "Погоди! Если тебе попадётся уж очень пугливый источник, то тогда тебе на помощь придёт ```Wire``` - это "
            "мессенджер, в котором тоже есть автоудаление и другие полезные функции, но в нём вообще всё защищено "
            "сквозным шифрованием, вплоть до видеозвонков."),
        npc.Squirrel.say("Было бы круто найти хверей и птиц, которым тоже могли угрожать из-за сотрудничества с Нашим домом"),
        npc.Squirrel.say("Когда начались пожары, у них было достаточно много волонтёров, которые потом ушли"),
        npc.Magpie.say("кажется мне понадобится помощь"),
        npc.Magpie.say("Сова, ты полетишь со мной?"),
        npc.Owl.say("Конечно! "),
        npc.Squirrel.say("Удачи вам!"),
        npc.Squirrel.say("Новенькие, можете отдохнуть сейчас"),
        npc.Squirrel.say("Или скрыть свои номера телефонов, например!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("""Прямо сейчас у вас есть возможность зайти в настройки телеграма и изменить настройки
         приватности. Самое важное что вы можете сделать:
+ Скрыть свой номер телефона
+ Отключить p2p звонки
+ Отключить доступ к вашему профилю через пересланные сообщения   
"""),
        npc.Squirrel.say("Слушайте, перед Совой было стыдно, можно сейчас признаюсь"),
        npc.Squirrel.say(
            "Мне очень жаль, что мы начали думать о безопасности только сейчас, когда у нас и наших друзей"
            " неприятности"),
        npc.Squirrel.say("Мне кажется, я сегодня всех сильно подставила"),
        npc.Floppa.say("Эй"),
        npc.Floppa.say("Ну камон"),
        npc.Floppa.say(
            "Ну откуда ты могла знать, что в соседней норе живут звери, которые будут себя так гадко вести? Всего не "
            "предугадаешь"),
        npc.Floppa.say(
            "Вы сегодня смогли защитить друг друга и прекрасного меня! И больше с вами никаких ужасов не случится! "
            "РРРРР"),
        npc.Floppa.say("Так что давайте наконец-то хоть немного расслабимся"),
      
        Proceed(game_break=True)
    ],

    game_break=[
        npc.Squirrel.ask(
            "Так, сейчас мы больше ничего не можем сделать. Постарайтесь чуть-чуть отдохнуть, заварите себе чай."
            "Приступайте только когда почувствуете что есть силы продолжать игру.",
            [("Отдохнули", "relax")], Var.null),
        # Proceed(vzlom=True)
        # Окей, я добавила меню в конце, но я не знаю, как именно оно работает
    ]
)
