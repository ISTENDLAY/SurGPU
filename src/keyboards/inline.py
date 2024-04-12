from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


startKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='О СурГПУ',
            callback_data='general'
        )
    ],
    [
        InlineKeyboardButton(
            text='Поступающим',
            callback_data='enrollee'
        )
    ],
    [
        InlineKeyboardButton(
            text='Контакты',
            callback_data='contacts'
        )
    ]
])

forStudents = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Бакалавриат',
            callback_data='bachelor'
        )
    ],
    [
        InlineKeyboardButton(
            text='Магистратура',
            callback_data='master'
        )
    ],
    [
        InlineKeyboardButton(
            text='Аспирантура',
            callback_data='postgraduate'
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back2main'
        )
    ]
    ])

back2main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back2main'
        )
    ]
])


bachelor = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Математика и Информатика',
            callback_data='bachelor1'
        )
    ],
    [
        InlineKeyboardButton(
            text='Математика и Физика',
            callback_data='bachelor2'
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='enrollee'
        )
    ],
])


master = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Цифровизация образования: проектирование, сопровождение, экспертиза',
            callback_data='master1'
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='enrollee'
        )
    ],
])


postgraduate = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Методология и технология профессионального образования',
            callback_data='post1'
        )
    ],
    [
        InlineKeyboardButton(
            text='Общая педагогика, история педагогики и образования',
            callback_data='post2'
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='enrollee'
        )
    ],
])

back2bachelor = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='bachelor'
        )
    ],
])


back2master = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='master'
        )
    ],
])


back2postgraduate = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='postgraduate'
        )
    ],
])

spamkb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Контакты',
            callback_data='contacts'
        )
    ],
    [
        InlineKeyboardButton(
            text='В главное меню',
            callback_data='back2main'
        )
    ],
])