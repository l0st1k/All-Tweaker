import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import ttkbootstrap as ttk
import subprocess

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}x{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def select_all_for_tabs(tab_frame):
    select_all_checkbox_var = tk.BooleanVar()
    select_all_checkbox = ttk.Checkbutton(tab_frame, text='Выделить всё', variable=select_all_checkbox_var)
    select_all_checkbox.grid(row=0, column=0, sticky='w')

    def select_all():
        select_state = select_all_checkbox_var.get()
        for checkbox in checkboxes.values():
            checkbox.set(select_state)

    select_all_checkbox.configure(command=select_all)

def execute():
    for checkbox_name, checkbox_var in checkboxes.items():
        if checkbox_var.get():
            subprocess.call(f'tweaks\\"{checkbox_name}"', shell=True)
            subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', f'tweaks\\{checkbox_name}.ps1'])
            # usage of JetBrains WinElevator (https://github.com/JetBrains/intellij-community/tree/master/native/WinElevator)
            # subprocess.run(['launcher.exe', f'powershell.exe -ExecutionPolicy Bypass -File tweaks\\{checkbox_name}.ps1'])

def restart():
    subprocess.run(['shutdown', '/r', '/t', '0'])

# Кастомизация консоли
subprocess.call("title All Tweaker Beta & mode con: cols=100 lines=25 & color a & echo Welcome to All Tweaker", shell=True)

# Создание главного окна
root = ttk.Window(themename='vapor')
# root = ttk.Window(themename='cyborg')
# root.iconbitmap(r'icon.ico')
root.title('All Tweaker Beta')
root.attributes('-fullscreen', True)

# Создание вкладок
tab_control = ttk.Notebook(root)

tabs = {
    'База': [
                        'Основная оптимизация + приватность Windows 10',    'Вернуть все службы',                           'Отключить UAC и smartscreen',                      'Windows 10 ALL version activator',
                        'Основная оптимизация + приватность Windows 11',    'Сделать бэкап служб',                          'Обычная перезагрузка',                             'Windows 11 ALL version activator',
                        'Углубленная оптимизация + приватность Windows 10', 'Сделать бэкап как bat',                        'Обычная перезагрузка в Безопасный режим',          'Отключить телеметрию Браузеров',
                        'Углубленная оптимизация + приватность Windows 11', 'Сделать копию реестра от Роджера Роуленда',    'Перезагрузка в Безопасный режим с поддержкой CMD', 'Терапия после обновлений винды',
                        'Хардкорная оптимизация + приватность Windows 10',  'Сделать копию реестра от studfile.net',        'Перезагрузка в Безопасный режим с поддержкой Сети','Обновить All Tweaker',
                        'Хардкорная оптимизация + приватность Windows 11',  'Импортировать копию реестра от studfile.net',  'Windows Vista - Server 2022 Activation',           'Выйти из All Tweaker',
    ],

'Поддержка': ['Поддержка\\Бесплатно поддержать автора (зарегаться в sharem по реф. ссылке).bat', 'Поддержка\\Бесплатно поддержать автора (посмотреть рекламу).bat', 'Поддержка\\Поддержать автора (Boosty).bat'],

'Приватность': ['Telemetry Disabler Ultimate', 'Оптимизировать и удалить телеметрию Google Chrome', 'Отключить телеметрию Microsoft Edge', 'Отключить телеметрию Mozilla Firefox', 'Отключить телеметрию Браузеров', 'Отключить телеметрию полностью', 'Отключить телеметрию Яндекс Браузера', 'Приватность и отпимизация от Flibustier', 'Приватность и отпимизация от ReviOS', 'Приватность от Adamx', 'Приватность от BoosterX и ios1ph', 'Приватность от IT-спец. Денис Курец', 'Приватность от Optimizer', 'Приватность от Pulse', 'Приватность от Win 10 Tweaker', 'Приватность от windowser', 'Терапия после обновлений винды', 'Удаление файла (CompatTelRunner.exe) телеметрия Windows', 'Удаление файла (mobsync.exe) синхронизация Windows', 'Удалить все приложения Microsoft', 'Удалить протокол SMBv1', 'Отключить телеметрию Браузеров//Оптимизировать и удалить телеметрию Google Chrome', 'Отключить телеметрию Браузеров//Отключить телеметрию Microsoft Edge', 'Отключить телеметрию Браузеров//Отключить телеметрию Mozilla Firefox', 'Отключить телеметрию Браузеров//Отключить телеметрию Яндекс Браузера', 'Adamx//Отключите дополнительные ненужные службы', 'Adamx//Отключить SmartSceen и блокировку загрузок', 'Adamx//Отключить взаимодействие с подключенными пользователями и телеметрию', 'Adamx//Отключить Защитник (включая исполняемый файл службы защиты от вредоносных программ)', 'Adamx//Отключить исполняемый файл службы защиты от вредоносных программ', 'Adamx//Отключить менеджер загрузки карт', 'Adamx//Отключить службы Bluetooth', 'Adamx//Отключить службы Xbox', 'Adamx//Отключить службы диагностики и телеметрии', 'Adamx//Отключить службы принтера', 'Adamx//Отключить средство устранения неполадок Центра обновления Windows', 'Adamx//Принудительно закрыть все процессы и службы(Безопасно)', 'BoosterX и ios1ph//Выключить автообновление драйверов', 'BoosterX и ios1ph//Остановить всю работу в фоне для Windows 10', 'BoosterX и ios1ph//Остановить всю работу в фоне для Windows 11', 'BoosterX и ios1ph//Отключение Spectre, Meldown, Tsx', 'BoosterX и ios1ph//Отключить антивирус Windows', 'BoosterX и ios1ph//Отключить виджеты для Windows 11', 'BoosterX и ios1ph//Отключить карты', 'BoosterX и ios1ph//Отключить обновления Windows', 'BoosterX и ios1ph//Отключить сбор данных в планировщике', 'BoosterX и ios1ph//Отключить телеметрию и прочую хрень', 'BoosterX и ios1ph//Отключить триггеры', 'BoosterX и ios1ph//Удалить телеметрию Nvidia', 'IT-спец. Денис Курец//Отключить Cortana', 'IT-спец. Денис Курец//Отключить Xbox', 'IT-спец. Денис Курец//Отключить другое', 'IT-спец. Денис Курец//Отключить историю', 'IT-спец. Денис Курец//Отключить планы', 'IT-спец. Денис Курец//Отключить сбор', 'IT-спец. Денис Курец//Отключить службы', 'IT-спец. Денис Курец//Отключить телеметрию', 'Optimizer//Отключить Cortana', 'Optimizer//Отключить «Новости и интересы»', 'Optimizer//Отключить безопасный режим Защитника Windows', 'Optimizer//Отключить общий доступ к медиаплееру', 'Optimizer//Отключить общий доступ к файлам', 'Optimizer//Отключить пограничную телеметрию', 'Optimizer//Отключить протокол SMBv1', 'Optimizer//Отключить протокол SMBv2', 'Optimizer//Отключить рекламу в Проводнике', 'Optimizer//Отключить телеметрию Office', 'Optimizer//Отключить телеметрию Visual Studio', 'Optimizer//Отключить телеметрию Xbox', 'Optimizer//Отключить телеметрию', 'Pulse//Отключить Cortana', 'Pulse//Отключить автоматическое обновление Windows', 'Pulse//Отключить ведение истории поисковых запросов', 'Pulse//Отключить и Xbox сервисы', 'Pulse//Отключить историю для приложений', 'Pulse//Отключить потенциально уязвимые службы', 'Pulse//Отключить сохранение списков последних открытых файлов', 'Pulse//Отключить телеметрию', 'Pulse//Очистка файла подкачки', 'Pulse//Убрать из планировщика запланированные задачи телеметрии', 'Win 10 Tweaker//Отключение «журналирования» Событий Windows', 'Win 10 Tweaker//Отключение ведения записи поведения пользователя', 'Win 10 Tweaker//Отключение всех видов телеметрий Office', 'Win 10 Tweaker//Отключение всех видов телеметрий Windows', 'Win 10 Tweaker//Отключение всех типов синхронизаций Windows', 'Win 10 Tweaker//Отключение и выпиливание шпионских модулей Microsoft', 'Win 10 Tweaker//Отключение определения местоположения пользователя', 'Win 10 Tweaker//Отключение проверки обращений через «Обратную связь»', 'Win 10 Tweaker//Отключение рекламного идентификатора и рекламы', 'Win 10 Tweaker//Отключение сбора данных об установленных приложениях', 'Win 10 Tweaker//Отключение сбора данных через события планировщика', 'Win 10 Tweaker//Отключение сбора и отправки данных рукописного ввода', 'Win 10 Tweaker//Отключение сбора статистики использования приложений', 'Win 10 Tweaker//Отключение сетевого доступа к доменам сбора данных', 'Win 10 Tweaker//Отключение скрытого мониторинга системы', 'Win 10 Tweaker//Отключение скрытого фонового обновления синтеза речи', 'Win 10 Tweaker//Отключение телеметрии NVIDIA', 'Win 10 Tweaker//Отключение удалённых экспериментов над ПК', 'windowser//Блокировать нежелательные веб узлы в файл hosts', 'windowser//Блокировка портов (безопасность)', 'windowser//Добавление правил брандмауэра. Блокировка нежелательных IP адресов', 'windowser//Отключить биометрическую службу Windows', 'windowser//Отключить все службы Xbox', 'windowser//Отключить камеру', 'windowser//Отключить нежелательные свойства Windows', 'windowser//Отключить обслуживание сенсорной клавиатуры и панели рукописного ввода', 'windowser//Отключить поиск в Windows', 'windowser//Отключить протокол SMB (общий доступ к файлам и принтерам)', 'windowser//Отключить розничную демонстрационную услугу', 'windowser//Отключить службу Bluetooth', 'windowser//Отключить службу Windows Update', 'windowser//Отключить службу геолокации', 'windowser//Отключить службу менеджера скачанных карт', 'windowser//Отключить службу общего доступа к проигрывателю Windows Media по сети', 'windowser//Отключить службу помощника по совместимости программ', 'windowser//Отключить службу предварительной оценки Windows', 'windowser//Отключить службу родительского контроля', 'windowser//Отключить службу удаленного реестора', 'windowser//Отключить службу управления корпоративными приложениями', 'windowser//Отключить Центр безопасности', 'windowser//Приватность Windows 10', 'windowser//Удалить шпионские службы от windowser'],

'Оптимизация': ['Основная оптимизация//W10 Старое меню питании', 'Основная оптимизация//Включить GameMode', 'Основная оптимизация//Включить TRIM', 'Основная оптимизация//Включить VBS', 'Основная оптимизация//Выключение гибернации', 'Основная оптимизация//Выключение залипания клавиш', 'Основная оптимизация//Выключить FSO и GameBar', 'Основная оптимизация//Выключить sysmain', 'Основная оптимизация//Выключить автостарт программ', 'Основная оптимизация//Выключить прозрачность', 'Основная оптимизация//Выключить уведомления защиты', 'Основная оптимизация//Максимальная производительность', 'Основная оптимизация//Обновить Windows без перезагрузки', 'Основная оптимизация//Остановить всю работу в фоне  для Windows 10', 'Основная оптимизация//Остановить всю работу в фоне для Windows 11', 'Основная оптимизация//Отключение Spectre, Meldown, Tsx', 'Основная оптимизация//Отключить HDCP для ноутов', 'Основная оптимизация//Отключить HDCP для ПК', 'Основная оптимизация//Отключить UAC и smartscreen', 'Основная оптимизация//Отключить VBS - W11', 'Основная оптимизация//Отключить антивирус Windows', 'Основная оптимизация//Отключить брандмауер', 'Основная оптимизация//Отключить виджеты для Windows 11', 'Основная оптимизация//Отключить карты', 'Основная оптимизация//Отключить оптимизацию доставки', 'Основная оптимизация//Отключить сбор данных в планировщике', 'Основная оптимизация//Отключить телеметрию и прочую хрень', 'Основная оптимизация//Открыть параметры быстродействия', 'Основная оптимизация//Открыть Электропитание', 'Основная оптимизация//Показывать все иконки в трее', 'Основная оптимизация//Старое контекстное меню для Windows 11', 'Основная оптимизация//Удалить высокую производительность', 'Основная оптимизация//Удалить скачанные файлы обновлений Windows', 'Основная оптимизация//Удалить телеметрию Nvidia', 'Основная оптимизация//Удалить энергосбережение', 'Углубленная оптимизация//Autoruns', 'Углубленная оптимизация//Desktop tweaks', 'Углубленная оптимизация//Keyboard Data Queue 50', 'Углубленная оптимизация//Large System Cache', 'Углубленная оптимизация//Mouse Data Queue 54 (ios1ph recommended)', 'Углубленная оптимизация//MSI Mode Tool', 'Углубленная оптимизация//NetworkThrottling', 'Углубленная оптимизация//System Responsiveness', 'Углубленная оптимизация//Более жесткая уборка', 'Углубленная оптимизация//Выключить службы брандмауера', 'Углубленная оптимизация//Вырубить обслуживание HDD SSD', 'Углубленная оптимизация//Качество фона 100', 'Углубленная оптимизация//Отключить автообновления store', 'Углубленная оптимизация//Отключить обновления Windows', 'Углубленная оптимизация//Отключить триггеры', 'Углубленная оптимизация//Открывать pow файлы', 'Углубленная оптимизация//Открыть Электропитание', 'Углубленная оптимизация//Рекомендованные службы 2', 'Углубленная оптимизация//Рекомендованные службы', 'Углубленная оптимизация//Сделать бэкап как bat', 'Углубленная оптимизация//Тесты режимов электропитания', 'Углубленная оптимизация//Ускорить завершение работы', 'Углубленная оптимизация//Установить оптимизацию при входе', 'Углубленная оптимизация//Режимы электропитания//Amit_v1_lowlatency', 'Углубленная оптимизация//Режимы электропитания//Amit_v2_extreme performance', 'Углубленная оптимизация//Режимы электропитания//Amit_v3_low latency', 'Углубленная оптимизация//Режимы электропитания//Atlas Power Plan', 'Углубленная оптимизация//Режимы электропитания//Bitsum Highest Performance', 'Углубленная оптимизация//Режимы электропитания//Calypto', 'Углубленная оптимизация//Режимы электропитания//GGOSv0_8_5_Idle_Enabled', 'Углубленная оптимизация//Режимы электропитания//Muren_Idle_Enabled', 'Углубленная оптимизация//Режимы электропитания//Unixcorn_Idle_Enabled', 'Углубленная оптимизация//Режимы электропитания//Zoyata_Low Latency', 'Хардкор//Выключить службы 2', 'Хардкор//Отключить устройства разом', 'Хардкор//Открыть Электропитание', 'Хардкор//Смертельная очистка планировщика от AtlasOS', 'Хардкор//Тесты режимов электропитания', 'Хардкор//Адские режимы электропитания//Amit_v1', 'Хардкор//Адские режимы электропитания//Amit_v2', 'Хардкор//Адские режимы электропитания//Amit_v3', 'Хардкор//Адские режимы электропитания//Calypto', 'Хардкор//Адские режимы электропитания//GGOSv0_8_5', 'Хардкор//Адские режимы электропитания//Muren', 'Хардкор//Адские режимы электропитания//RekOS_Power_Plan', 'Хардкор//Адские режимы электропитания//Unixcorn', 'Хардкор//Адские режимы электропитания//Zoyata', 'Хардкор//Уменьшить количество svhost и другие твики//интернет батник', 'Хардкор//Уменьшить количество svhost и другие твики//чистка 1', 'Хардкор//Уменьшить количество svhost и другие твики//чистка 2', 'Хардкор//Уменьшить количество svhost и другие твики//чистка 3'],

'Другая оптимизация': ['Fortnite нормальные приоритеты', 'pssuspend', 'Ultimate Optimization', 'Windows 10 Debloater (Advanced)', 'Windows 10 Debloater', 'Windows 10 Driver Disabler', 'Windows 10 Service Disabler', 'Включить зарезервированное хранилище', 'Восстановить счетчики производительности', 'Выключить автообновление драйверов', 'Выключить режим гибернации', 'Выключить службы', 'Глобальное отключение FSO и GameBar', 'Максимальная производительность', 'Настройки задержки BCD от Adamx', 'Оптимизация Windows c Github', 'Оптимизация мыши', 'Оптимизация приоритетов Windows', 'Оптимизация редактирования BCD', 'Оптимизация сети', 'Оптимизация управления памятью', 'Оптимизируйте все настройки Windows от Adamx', 'Остановить всю работу в фоне', 'Отключение резерва 20% CPU для фоновых процессов', 'Отключение службы Windows 10', 'Отключите ненужные драйверы Windows 10', 'Отключите ненужные службы', 'Отключить BitLocker', 'Отключить Ease Of Access', 'Отключить Game Bar', 'Отключить HPET, ST_DT', 'Отключить HPET', 'Отключить зарезервированное хранилище', 'Отключить Защитник Windows', 'Отключить отслеживание и телеметрию Windows', 'Отключить полноэкранную оптимизацию Fortnite', 'Отключить предварительную выборку', 'Отключить работу приложений в фоновом режиме', 'Отключить регулирование мощности', 'Отключить службу менеджера скачанных карт', 'Отключить службы от EverythingTech', 'Отключить телеметрию Браузеров', 'Отключить триггеры', 'Отключить файл гибернации', 'Отключить экран блокировки', 'Отключить эксперименты над ПК', 'Открывать pow файлы', 'Отобразить скрытые пункты Электропитания', 'Полное отключение Центра уведомлений', 'Порог разделения SvcHost', 'Приватность от Adamx', 'Приватность от windowser', 'Проверить сжатие системы', 'Расширенная оптимизация DWM', 'Расширенная оптимизация GameDVR', 'Регулирование сети', 'Сжать систему', 'Службы от garbuzilia', 'Старое меню питании для Windows 10', 'Твики от garbuzilia', 'Твики реестора от Adamx', 'Убить DWM', 'Убрать Input Lag', 'Убрать задержку появления контекстного меню', 'Увеличение системного кэша', 'Удаление временных файлов и файлов предварительной выборки', 'Удалить вредоносные UWP приложения', 'Удалить основные приложения Microsoft', 'Удалить файлы конфигурации Fortnite в Appdata', 'Удалить файлы предварительной выборки', 'Уменьшение времени отключения процессов и показа меню', 'Уменьшить задержку запуска приложений из автозагрузки', 'Уменьшить размер файла гибернации', 'Ускорение появления превью на панели задач', 'Ускоренное мерцание курсора', 'Ускорить ввод с Клавиатуры', 'Ускорить запуск Windows', 'Ускорить открытие папок', 'Меньшая задержка ввода и более плавный игровой процесс//16 Hex – самый гладкий', 'Меньшая задержка ввода и более плавный игровой процесс//25 Hex – Баланс', 'Меньшая задержка ввода и более плавный игровой процесс//28 Hex — самая низкая задержка ввода', 'Меньшая задержка ввода и более плавный игровой процесс//По умолчанию — 26 Hex (приоритет программ)'],

'Очистка': ['Запуск меню очистки', 'Запуск очистки', 'Очистить Windows v2.0', 'Очистить Windows', 'Очистить автозапуск в реестре', 'Очистить временные файлы и кэш иконок', 'Очистить кэш', 'Очистка и оптимизация дисков', 'Очистка кэша обновлений', 'Очистка папок Temp', 'Очистка файла подкачки', 'Очистка хранилища WinSxS', 'Сбросить счетчик изображений', 'Удалить временные файлы от Adamx', 'Удалить временные файлы', 'Удалить кеш Центра обновления Windows', 'Удалить лог файлы', 'Удалить скачанные файлы обновлений Windows', 'Хардкор чистка 1', 'Хардкор чистка 2', 'Хардкор чистка 3'],

'Обновления Windows': ['Включить обновления Windows 10', 'Запретить Windows 10 восстановить себя от Windows Update', 'Обновить Windows без перезагрузки', 'Обновить и перезагрузить Windows', 'Обновление Windows - получать только непосредственно от Microsoft', 'Отключить автоматическое обновление Windows', 'Отключить обновления Windows 10', 'Отключить обновления Windows от ios1ph', 'Отключить службу Windows Update', 'Терапия после обновлений винды', 'Удалить скачанные файлы обновлений Windows', 'Терапия после обновлений винды//Выключить автообновление драйверов', 'Терапия после обновлений винды//Отключить UAC и smartscreen', 'Терапия после обновлений винды//Отключить обновления Windows', 'Терапия после обновлений винды//Отключить оптимизацию доставки', 'Терапия после обновлений винды//Отключить сбор данных в планировщике', 'Терапия после обновлений винды//Отключить телеметрию и прочую хрень', 'Терапия после обновлений винды//Отключить триггеры'],

'Удалить приложения Microsoft': ['Возврат приложений от Microsoft', 'Отключить Defender, SmartScreen и Antimalware', 'Удалить 3D Builder', 'Удалить Bing Sports', 'Удалить Cortana', 'Удалить Groove Music', 'Удалить Internet Explorer', 'Удалить Microsoft Edge Appx', 'Удалить Microsoft Edge и WebView', 'Удалить Microsoft Edge', 'Удалить Microsoft Office от Darren White', 'Удалить Microsoft Office', 'Удалить Mobile Plans', 'Удалить OneDrive', 'Удалить Paint 3D', 'Удалить Print 3D', 'Удалить Windows Defender (DefenderKiller)', 'Удалить Windows Defender (Fuck Windows Defender)', 'Удалить Windows Defender от MartyFiles', 'Удалить Windows Defender от Vlado', 'Удалить Xbox App', 'Удалить Xbox Bar', 'Удалить Xbox Game Speech', 'Удалить Будильники и часы', 'Удалить Ваш телефон', 'Удалить вредоносные UWP приложения', 'Удалить все приложения Microsoft', 'Удалить Деньги', 'Удалить Записки', 'Удалить Запись голоса', 'Удалить и другие приложения Metro', 'Удалить Калькулятор', 'Удалить Камера', 'Удалить Карты', 'Удалить Кино и ТВ', 'Удалить Люди', 'Удалить Набросок на фрагменте экрана', 'Удалить Начало', 'Удалить основные приложения Microsoft', 'Удалить Портал смешанной реальности', 'Удалить Почта и Календарь', 'Удалить Расширение для изображений HEIF', 'Удалить Расширение для изображений Webp', 'Удалить Расширение для интернет-мультимедиа', 'Удалить Советы', 'Удалить средство 3D-просмотра', 'Удалить Техническая помощь', 'Удалить Фотографии (Майкрософт)', 'Удалить Центр отзывов'],

'Исправление проблем': ['Вернуть все службы', 'Включить обслуживание HDD SSD', 'Запусти если Visual Studio не Устанавливается - Ошибка на этапе загрузки', 'Запусти если игры, в которых есть Античит - Не запускаются', 'Запусти если медленно открываются проги или игры', 'Запусти если не запускается GTA V RAGE MP', 'Запусти если не работает Bluetooth', 'Запусти если не работает Store', 'Запусти если не работает VPN', 'Запусти если не работает Антивирус Винды или Брандмауер', 'Запусти если не работает буфер WIN + V', 'Запусти если не работает дефрагментация', 'Запусти если не работает или не устанавливается панель Nvidia', 'Запусти если не работает принтер', 'Запусти если не работает Управление дисками', 'Запусти если не работают скрипты', 'Запусти если не работают уведомления', 'Запусти если поменялся интерфейс окон W7', 'Запусти если пропала иконка Сети - Нельзя зайти в поиск по Wi-Fi', 'Запусти если просел ФПС на AMD', 'Запусти если просел ФПС, скачет вар на слабых ПК', 'Запусти если слетают драйвера после перезагрузки', 'Запусти если хочешь вернуть функционал горячих клавиш громкости', 'Отмена//Desktop tweaks', 'Отмена//System Responsiveness', 'Отмена//Вернуть все службы', 'Отмена//Вернуть новое контекстное меню для Windows 11', 'Отмена//Вернуть новое меню электропитании', 'Отмена//Включить FSO и GameBar', 'Отмена//Включить HDCP для ноутбуков', 'Отмена//Включить HDCP для ПК', 'Отмена//Включить SmartSceen и блокировку загрузок', 'Отмена//Включить Spectre, Meldown, Tsx', 'Отмена//Включить VBS', 'Отмена//Включить автообновление', 'Отмена//Включить автообновления store', 'Отмена//Включить антивирус Windows', 'Отмена//Включить безопасный режим Защитника Windows', 'Отмена//Включить брандмауер', 'Отмена//Включить взаимодействие с подключенными пользователями и телеметрию', 'Отмена//Включить виджеты для Windows 11', 'Отмена//Включить гибернацию', 'Отмена//Включить дополнительные ненужные службы', 'Отмена//Включить задачи', 'Отмена//Включить Защитник (включая исполняемый файл службы защиты от вредоносных программ)', 'Отмена//Включить Защитника Windows', 'Отмена//Включить исполняемый файл службы защиты от вредоносных программ', 'Отмена//Включить менеджер загрузки карт', 'Отмена//Включить нежелательных служб от Adamx', 'Отмена//Включить обновление Windows', 'Отмена//Включить обслуживание HDD SSD', 'Отмена//Включить общий доступ к файлам', 'Отмена//Включить протокол SMBv1', 'Отмена//Включить работу программ в фоне для Windows 11', 'Отмена//Включить работу программ в фоне', 'Отмена//Включить сетевого доступа к доменам сбора данных', 'Отмена//Включить службы Bluetooth', 'Отмена//Включить службы Xbox', 'Отмена//Включить службы принтера', 'Отмена//Включить телеметрию Office', 'Отмена//Включить телеметрию Xbox', 'Отмена//Включить телеметрию', 'Отмена//Включить триггеры', 'Отмена//Включить троттлинг', 'Отмена//Выключить GameMode', 'Отмена//Выключить Large System Cache', 'Отмена//Выключить ускоренный ввод с Клавиатуры', 'Отмена//Дефолт службы win 10 11', 'Отмена//Добавить высокую производительность', 'Отмена//Добавить высокую производительность', 'Отмена//Добавить энергосбережение', 'Отмена//Добавить энергосбережение', 'Отмена//Если скачет пинг (NetworkThrottling)', 'Отмена//Качество фона 80', 'Отмена//Отменить оптимизацию реестора от EverythingTech', 'Отмена//Удалить оптимизацию при входе', 'Отмена//Ускорить завершение работы', 'Data Queue Size клава//.Дефолт 100', 'Data Queue Size клава//Keyboard Data Queue 10', 'Data Queue Size клава//Keyboard Data Queue 20', 'Data Queue Size клава//Keyboard Data Queue 30', 'Data Queue Size клава//Keyboard Data Queue 40', 'Data Queue Size клава//Keyboard Data Queue 50', 'Data Queue Size клава//Keyboard Data Queue 60', 'Data Queue Size клава//Keyboard Data Queue 70', 'Data Queue Size клава//Keyboard Data Queue 80', 'Data Queue Size клава//Keyboard Data Queue 90', 'Data Queue Size мышь//.Дефолт 100', 'Data Queue Size мышь//Mouse Data Queue 10', 'Data Queue Size мышь//Mouse Data Queue 20', 'Data Queue Size мышь//Mouse Data Queue 30', 'Data Queue Size мышь//Mouse Data Queue 40', 'Data Queue Size мышь//Mouse Data Queue 47 (~900 bytes)', 'Data Queue Size мышь//Mouse Data Queue 50', 'Data Queue Size мышь//Mouse Data Queue 54 (ios1ph recommended)', 'Data Queue Size мышь//Mouse Data Queue 60', 'Data Queue Size мышь//Mouse Data Queue 70', 'Data Queue Size мышь//Mouse Data Queue 80', 'Data Queue Size мышь//Mouse Data Queue 90'],

'Электропитание': ["Adamx's Power Plan", 'Amit_v1', 'Amit_v1_lowlatency', 'Amit_v2', 'Amit_v2_extreme performance', 'Amit_v3', 'Amit_v3_low latency', 'Atlas Power Plan', 'Balanced', 'Bitsum Highest Performance', 'Calypto', 'CPU-MaxPower', 'GGOSv0_8_5', 'GGOSv0_8_5_Idle_Enabled', 'High Peformance', 'Muren', 'Muren_Idle_Enabled', 'Power saver', 'RekOS_Power_Plan', 'Ultra Low Latency Plans', 'Unixcorn', 'Unixcorn_Idle_Enabled', 'Zoyata', 'Zoyata_Low Latency', 'Выключение гибернации', 'Добавить высокую производительность', 'Добавить энергосбережение', 'Максимальная производительность', 'Открывать pow файлы', 'Открыть Электропитание', 'Отобразить скрытые пункты Электропитания', 'Показывать все иконки в трее', 'Старое меню питании для Windows 10', 'Тесты режимов электропитания', 'Удалить высокую производительность', 'Удалить энергосбережение'],

'Программы': ['Программы\\Браузеры\\Cent Browser.bat', 'Программы\\Браузеры\\Thorium.bat', 'Программы\\Игровые платформы\\Battle.net.bat', 'Программы\\Игровые платформы\\Epic Games Launcher.bat', 'Программы\\Игровые платформы\\Origin.bat', 'Программы\\Игровые платформы\\Steam.bat', 'Программы\\Игровые платформы\\Ubisoft Connect.bat', 'Программы\\Оптимизация\\Mem Reduct.bat', 'Программы\\Приватность\\O&O ShutUp10++.bat', 'Программы\\Приватность\\Psiphon VPN.bat', 'Программы\\Приватность\\SimpleDnsCrypt.bat', 'Программы\\Приватность\\simplewall.bat', 'Программы\\Приватность\\smsniff.bat', 'Программы\\Приватность\\W10Privacy.bat', 'Программы\\Программы для общения и стриминга\\Discord.bat', 'Программы\\Программы для общения и стриминга\\OBS Studio.bat', 'Программы\\Программы для общения и стриминга\\Twitch.bat', 'Программы\\Твикеры\\BoosterX 2.bat', 'Программы\\Твикеры\\BoosterX.bat', 'Программы\\Твикеры\\Optimizer.bat', 'Программы\\Твикеры\\Win 10 Tweaker.bat', 'Программы\\Твикеры\\WinCry.bat', 'Программы\\Торрент-клиенты\\Deluge.bat', 'Программы\\Торрент-клиенты\\qBittorrent.bat'],
}
# New code to add label "All Tweaker..." to the tab "search_entry.placemh"
if 'Приватность' in tabs:
    tab_frame = ttk.Frame(tab_control)
    label = ttk.Label(tab_frame, text="""
    All Tweaker Beta (scode18) — это утилита для тонкой настройки операционной системы и программного обеспечения, которая позволяет изменять определённые параметры для персонализации и оптимизации.
    В ней объединены все лучшие твики, которые я нашел, включая Win 10 Tweaker, Booster X и другие.
    All Tweaker позволяет настроить внешний вид графического интерфейса пользователя, а также оптимизировать производительность системы и приложений.""")
    label.pack()
    tab_control.add(tab_frame, text='All Tweaker')

search_entry_var = StringVar()
search_entry = ttk.Entry(root, textvariable=search_entry_var)
search_entry.pack(side='bottom', padx=10, pady=10)
def select_all_for_tabs(tab_frame):
    select_all_checkbox_var = tk.BooleanVar()
    select_all_checkbox = ttk.Checkbutton(tab_frame, text='Выделить всё', variable=select_all_checkbox_var)
    select_all_checkbox.grid(row=0, column=0, sticky='w')

    def select_all():
        select_state = select_all_checkbox_var.get()
        for checkbox in checkboxes.values():
            checkbox.set(select_state)

    def update_checkboxes(*args):
        entered_text = search_entry_var.get().lower()
        for checkbox_name, checkbox_var in checkboxes.items():
            if entered_text in checkbox_name.lower():
                checkbox_var.set(True)
            else:
                checkbox_var.set(False)

    select_all_checkbox.configure(command=select_all)
    search_entry_var.trace_add('write', update_checkboxes)

checkboxes = {}
for tab_name, checkbox_names in tabs.items():
    tab_frame = ttk.Frame(tab_control)
    tab_control.add(tab_frame, text=tab_name)

    if tab_name:
        select_all_for_tabs(tab_frame)

    num_columns = 1
    if tab_name == 'База':
        num_columns = 4
    elif tab_name == 'Приватность':
        num_columns = 3
    elif tab_name == 'Оптимизация':
        num_columns = 3
    elif tab_name == 'Другая оптимизация':
        num_columns = 2
    elif tab_name == 'Углубленная оптимизация и Хардкор':
        num_columns = 3
    elif tab_name == 'Исправление проблем':
        num_columns = 2
    elif tab_name == 'Удалить приложения Microsoft':
        num_columns = 2
    elif tab_name == 'Электропитание':
        num_columns = 3

    for i, checkbox_name in enumerate(checkbox_names):
        checkbox_var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(tab_frame, text=checkbox_name, variable=checkbox_var)
        checkbox.grid(row=i//num_columns+1, column=i%num_columns, sticky='w')
        checkboxes[checkbox_name] = checkbox_var

# Создание кнопок
execute_button = ttk.Button(root, text='Выполнить', command=execute)
restart_button = ttk.Button(root, text='Перезагрузка', command=restart)

# Размещение элементов
tab_control.pack(expand=1, fill='both')
# search_entry.pack(side='left', padx=10, pady=10)
# search_entry.place(x=0, y=0)
# restart_button.pack(side='right', padx=10, pady=10)
# execute_button.pack(side='right', padx=10, pady=10)

# Create the "Выполнить" button
execute_button = ttk.Button(root, text='Выполнить', command=execute)

# Set the background color of the button
execute_button.configure(style='Custom.TButton')

# Create a custom style for the button
style = ttk.Style()
style.configure('Custom.TButton', background='black', foreground='white')

# Position the button in the top-right corner of the window
execute_button.place(relx=1.0, rely=0.0, anchor='ne')

# Запуск окна
root.mainloop()
