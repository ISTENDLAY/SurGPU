from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from src.keyboards.inline import startKeyboard, forStudents, back2main, bachelor, master, postgraduate, back2bachelor, back2master, back2postgraduate, spamkb
from src.db.database import addUser, updateMessage, lastMessage
from src.handlers.delete import deleteMessage
from src.images.images import logo, choice

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    name = message.from_user.first_name
    id = message.from_user.id
    await addUser(id, name)
    message_id = await message.answer_photo(caption=f'Здравствуй, <i>{name}</i>, это информационный бот СурГПУ, здесь ты можешь найти полезную информацию для поступления.', reply_markup=startKeyboard, photo=logo)
    await deleteMessage(id, message_id.message_id - 1)
    await updateMessage(id, message_id.message_id)


@router.callback_query(F.data=='general')
async def getGeneral(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='''Сургутский Педагогический – это современный университет, единственный в Югре и на  Севере Западной Сибири профильный педагогический вуз, ведущий свою историю с 1986 года.

СурГПУ – это вуз с уже сложившимися многолетними традициями, профессиональной и прогрессивной командой педагогов-исследователей и сотрудников, яркими и талантливыми студентами.

Для нас роль педагогического образования заключается в обеспечении роста интеллектуального и научного потенциала отечественной молодежи, вставшей на путь освоения учительской и других социально-ориентированных профессий.

Роль педагога и наставника в жизни каждого человека невозможно переоценить. Именно они являются движущей силой общества, мотивирующей подрастающее поколение к постижению нового знания. Сегодня особую важность приобрела и воспитательная миссия педагога. Это уже прочно укрепилось в массовом сознании.

Наша задача – не допустить диссонанса между социальными ожиданиями по отношению к учительской профессии и квалификационными требованиями к ней, актуализированными современной реальностью.

Обучение в Сургутском Педагогическом – это время становления молодых людей как самостоятельных взрослых личностей, способных принимать решения и преодолевать возникающие на новом этапе их жизненного пути трудности.

В школах округа с каждым годом все больше учителей, которые успешно завершили обучение в нашем университете. Его выпускники востребованы не только в области образования, некоммерческом социально-ориентированном секторе, науке, но и на государственной и муниципальной службе, в бизнесе.

Мы в своей работе руководствуемся следующим принципом: в педагогическом образовании необходим переход от подготовки «педагогов индустриальной эпохи» к подготовке «педагогов информационного общества», что позволяет формировать новый облик как педагогической профессии, так и наставничества.

Добро пожаловать в Сургутский государственный педагогический университет!

<i>Ректор</i>
<i>Сургутского государственного</i>
<i>педагогического университета,</i>
<i>доктор социологических наук, доцент</i>
<i>В.П. Засыпкин</i>
''', reply_markup=back2main)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='enrollee')
async def getGeneral(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer_photo(caption='Какой уровень образования Вы планируете получить?', reply_markup=forStudents, photo=choice)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='contacts')
async def getGeneral(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='<a href="http://www.surgpu.ru/Abitur/">Официальный сайт</a>\nТелефон приёмной комиссии: +73462774411',reply_markup=back2main)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='back2main')
async def getGeneral(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id-1)
    await deleteMessage(user_id, message_id)
    name = callback.from_user.first_name
    message_id = await callback.message.answer_photo(caption=f'Здравствуй, <i>{name}</i>, это информационный бот СурГПУ, здесь ты можешь найти полезную информацию для поступления.', reply_markup=startKeyboard, photo=logo)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='bachelor')
async def forBachelors(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Прием документов осуществляется до 7 июля.\n\nНаправления для поступления:', reply_markup=bachelor)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='master')
async def forMasters(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Прием документов осуществляется до 22 августа.\n\nНаправления для поступления:', reply_markup=master)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='postgraduate')
async def forCrazyPeople(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Прием документов осуществляется до 20 августа.\n\nНаправления для поступления:', reply_markup=postgraduate)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='bachelor1')
async def bachelorInf(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Вступительные испытания:\n– Русский язык (ЕГЭ, не менее 40 баллов)\n– Математика (ЕГЭ, не менее 39 баллов)\n– Информатика и ИКТ\n\nБолее подробная <a href="https://www.surgpu.ru/Abitur/bachelor/">информация</a>', reply_markup=back2bachelor)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='bachelor2')
async def bachelorPhys(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Вступительные испытания:\n– Русский язык (ЕГЭ, не менее 40 баллов)\n– Математика (ЕГЭ, не менее 39 баллов)\n– Физика\n\nБолее подробная <a href="https://www.surgpu.ru/Abitur/bachelor/">информация</a>', reply_markup=back2bachelor)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='master1')
async def bachelorPhys(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='Вступительное испытание – Профильный междисциплинарный экзамен (устно)\n\nБолее подробная <a href="https://www.surgpu.ru/Abitur/magistratura/">информация</a>', reply_markup=back2master)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='post1')
async def bachelorPhys(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='– Специальная дисциплина, соответствующая направленности (профилю) программы подготовки научно-педагогических кадров в аспирантуре\n– Философия\n– Иностранный язык\n\nБолее подробная <a href="https://www.surgpu.ru/Abitur/aspirantura">информация</a>', reply_markup=back2postgraduate)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.callback_query(F.data=='post2')
async def bachelorPhys(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    message_id = await lastMessage(user_id)
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id)
    message_id = await callback.message.answer(text='– Специальная дисциплина, соответствующая направленности (профилю) программы подготовки научно-педагогических кадров в аспирантуре\n– Философия\n– Иностранный язык\n\nБолее подробная <a href="https://www.surgpu.ru/Abitur/aspirantura">информация</a>', reply_markup=back2postgraduate)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)


@router.message(F.text)
async def spam(message: Message):
    user_id = message.from_user.id
    message_id = message.message_id
    dot_message = await callback.message.answer(text='.')
    await deleteMessage(user_id, message_id - 1)
    await deleteMessage(user_id, message_id)
    message_id = await message.answer('Ориентация по боту осуществляется с помощью кнопок, вам не нужно отправлять сообщения.\nЕсли вы не смогли найти ответ на свой вопрос вы можете связаться с нами.', reply_markup=spamkb)
    await deleteMessage(user_id, dot_message.message_id)
    await updateMessage(user_id, message_id.message_id)