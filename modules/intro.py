from engine.glide import StoryMap
from engine.var import Var

from modules.init import npc, score, docs

description = "Интро"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Привет!"),
        npc.Squirrel.say("Вы запустили игру «Взлом медиа». Эта игра познакомит вас с базовыми правилами кибербезопасности. "
                         "Прохождение займёт примерно час. Сейчас я введу вас в курс дела — представлюсь сама, познакомлю вас "
                         "со своей командой и расскажу, что будет происходить."),
        npc.Squirrel.say("Вы находитесь в чате сотрудников журнала «Сорокин хвост». Наш журнал посвящён жизни птиц, зверей "
                         "и рыб в Хвойном Лесу (так мы называем наш дом) и соседних районах. Я Белка, менеджерка в "
                         "«Сорокином хвосте»."),
        npc.Squirrel.say("Сейчас мы переживаем тяжёлые времена. По всему лесу происходят тревожные события, но у нас не хватает "
                          "лап, чтобы своевременно их освещать. "),
        npc.Squirrel.say("Если вы поможете нам с парой небольших задач, в благодарность мы поделимся с вами знаниями о "
                        "кибербезопасности. Мы как журналисты очень заботимся о сохранности своих данных - и научим вас "
                        "тому же. "),
        npc.Squirrel.say("Давайте познакомимся. Пусть каждый участник игры пришлёт свой любимый стикер. Это важно, "
                         "чтобы я всех запомнила. Как закончите, пусть кто-то один напишет слово *Готово*"),
        npc.Squirrel.acquaintance(
            reply_phrases=["Приятно познакомиться!", "Привееет", "Йоу! Напишите *Готово* когда закончите"]),
        npc.Squirrel.say("Ура, спасибо! Теперь я знаю всех участников. Давайте представлю вам нашу постоянную команду. "),
        npc.Floppa.say("Я каракал! Рррр"),
        npc.Floppa.sticker('good_day'),
        npc.Squirrel.say("Это Флоппа - партнер нашего журнала. У нас много классных совместных проектов!"),
        npc.Magpie.say("привет новеньким"),
        npc.Squirrel.say(
            "Сорока - наша корреспондентка. Из-за нехватки кадров не ней сейчас висят ещё и читательские материалы, "
            "но она иногда не успевает делать всё сразу("),
        npc.Squirrel.say(
            "А ещё у нас есть Сова - наша безопасница. Сова, поприветствуй ребят!"),
        npc.Owl.say("Вы забыли, что я ночная птица? Я же просила вас не писать мне днём."),
        npc.Squirrel.say(
            "Прости, Сова! У нас важный повод, нужно ввести новичков в курс дела "),
        npc.Owl.say("Ладно."),
        npc.Owl.say("Привет всем."),
        npc.Squirrel.say(
            "Фух, вроде всех представила. А теперь к делу. Расскажу, зачем вас всех собрала "),
        npc.Squirrel.say("Нам пришло сообщение от читателя. Его нужно отредактировать, а Сорока не успевает это сделать. "),
        npc.Magpie.say("это кошмар, времени нет вообще("),
        npc.Squirrel.say("Менять структуру и что-то переписывать не нужно. Но важно убедиться, что в сообщении нет ничего, "
                         "что выдало бы наш источник. "),
        npc.Owl.info(
            "Да, самое важное — анонимизация респондента. Мы стараемся не разглашать чужие данные, будь то *имя* или "
            "*место жительства*, даже если источник не против. Это опасно и для респондента, и для нас самих. "),
        npc.Magpie.say("а вот и само письмо"),
        npc.Magpie.info(
            "_Я живу на Пихтовой улице и буквально только что увидел, как лисичкам снова продавали спички! "
            "Это возмутительно! Прошлым летом они подожгли море, и мы всем лесом ходили его тушить, Вы же сами "
            "об этом писали. Я уверен, что они опять что-то задумали. Надо предпринять какие-то меры! Сейчас по "
            "всей области идут пожары, поэтому мы все должны быть крайне осторожны со спичками._"),
        npc.Squirrel.say("Пожалуйста, прочитайте его и напишите в чат, какие слова выдают данные Кролика — мы их уберём)"),
        #М: А МОЖЕТ, В ЗАМЕТКЕ ЗАМЕНИТЬ КРОЛИКА НА КОГО-ТО ЕЩЁ? ПРОСТО ПОТОМ ТОЖЕ КРОЛИК ПОЯВЛЯЕТСЯ, И МОЖНО ЗАПУТАТЬСЯ В ГЕРОЯХ
        npc.Floppa.say("Не стесняйтесь обсуждать в чате детали!"),
        npc.Squirrel.say("Прямо тут, да! Или вообще соберите общий звонок в Телеграме. Для этого всем участникам нужно "
                         "нажать облачко в правом верхнем углу. "),
        npc.Floppa.say("Сроки у нас не особо горящие, но вам нужно научиться быстро договариваться друг с другом, это суперрррр важно!"),
        npc.Squirrel.say("Итак, какие слова выдают местоположение или личные данные Кролика? Слов всего 4 — напишите их "
                         "сюда, а мы уберём их из письма. "),
        npc.Squirrel.say("И не забудьте нажать Готово, когда закончите)"),
        #М: ПРО ГОТОВО НУЖНО БУДЕТ УБРАТЬ, КОГДА ИЗМЕНИМ ЛОГИКУ ОТВЕТОВ, ПОКА ОСТАВИЛА КАК ЕСТЬ 
        npc.Squirrel.ask(docs['fox_note'], [("Готово", "ready")], Var.null),
        npc.Squirrel.say("Круто, вы нам очень помогли!"),
        score.instantiate(),
        score.add(2),
        npc.Floppa.say("Уррра! У нас +2 балла по шкале крутости!"),
        npc.Floppa.say("Чем круче наш журнал, тем быстрее распространяются наши материалы в лесу"),
        npc.Floppa.say("А чем быстрее это происходит, тем больше у нас читателей"),
        npc.Floppa.say("А чем больше у нас читателей, тем мы круче!"),
        npc.Magpie.say("флоппа, остановись"),
        npc.Magpie.say("у меня проблема, ребята"),
        npc.Magpie.say("сейчас одновременно по всей области происходят очень важные вещи, а я только одна"),
        npc.Squirrel.say("Сорока, мы сами со всем справимся!"),
        npc.Squirrel.say("Вылетай сейчас туда, куда можешь"),
        npc.Squirrel.say("А мы с ребятами будем тебя ждать"),
        npc.Magpie.say("окей"),
        npc.Magpie.say("только добавь кролика в чат"),
        npc.Magpie.say("а то я зашиваюсь"),
        npc.Squirrel.invite(npc.Rabbit),
        npc.Rabbit.say("Алоха!"),
        npc.Squirrel.say(
            "Кролик - сотрудник некоммерческой организации «Наш дом». Он с Сорокой подготовил кое-что для вас, но у нас остались ещё кое-какие "
            "моменты, будем прямо тут всё решать"),
        #М: НЕ СОВСЕМ ПОНИМАЮ ПО СЮЖЕТУ, ЧТО ТАКОЕ НАШ ДОМ, И В КАКОЙ РОЛИ ВЫСТУПАЕТ КРОЛИК. НУЖНО ПОЯСНЕНИЕ, ЧТОБЫ СДЕЛАТЬ ЧАСТЬ НИЖЕ ЧУТЬ ПОНЯТНЕЕ 
        npc.Squirrel.say("Совсем скоро будем обрабатывать материалы Кролика и Сороки!"),
        npc.Floppa.say("Ещё один партнёр???"),
        npc.Floppa.say("Этот чят слишком мал для нас двоих...."),
        npc.Floppa.say("ПОГОДИТЕ а что за наш дом? "),
        npc.Rabbit.say("Мы сейчас обустраиваем лагерь для погорельцев из грибного района"),
        npc.Rabbit.say("Вы бы видели, сколько тут зверей и птиц"),
        npc.Rabbit.say("Грустно смотреть"),
        npc.Floppa.say("И они хотят жить в хвойном лесу?"),
        npc.Rabbit.say("А где ещё? "),
        npc.Floppa.say("Наверное, в лесу им не все рады("),
        npc.Rabbit.say("Вот за этим мы к вам и обратились"),
        npc.Rabbit.say("Мы сильно переживаем насчёт интеграции"),
        #М: НУЖНА ПОЯСНИТЕЛЬНАЯ БРИГАДА. НЕ ДО КОНЦА ПОНИМАЮ, ЧТО ТАКОЕ НАШ ДОМ, ЧТО ЗА ИНТЕГРАЦИЯ, И ЗАЧЕМ ДОБАВЛЯТЬ КРОЛИКА В ЧАТ
        npc.Squirrel.say("Сорока, ну что? "),
        npc.Squirrel.say("Ты можешь сейчас вылетать?"),
        npc.Magpie.say("да "),
        npc.Magpie.say("только выдайте мне сначала редзадание"),
        npc.Squirrel.say(
            "Давайте сделаем так. Я сейчас вышлю темы, а наши новенькие выберут, с чего им будет лучше начинать!")
    ]
)
