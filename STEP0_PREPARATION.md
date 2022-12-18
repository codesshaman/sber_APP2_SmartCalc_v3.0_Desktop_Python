# Подготовка

По заданию среда, в которой мы будем работать - Python 3.11. Значит, необходимо настроить эту среду на тех ПК, на которых мы будем работать, желательно ещё и сделать эту среду переносимой чтобы не привязываться к одному рабочему месту.

Задача: 
- Запустить среду python-3.11 на любом компе без сложных танцев с бубном.
- По возможности разоворачивать эту среду быстро и на разных ПК.
Методы: 
- Установка brew. Пакетный менеджер brew работает только на unix-системах, стало быть, любой ПК с windows придётся настраивать отдельно.
- Использование виртуальной машины. Виртуализация доступна на любой платформе, виртуальная конфигурация переносима.

Попробовав настроить brew на школьном маке я пришёл к выводу, что работать через него крайне неудобно. Долгая установка, частые ошибки и необходимость постоянного запуска установочного скрипта на каждом новом маке с последующим ожиданием отталкивают.

А вот виртуальная машина с установленным python на текущем этапе кажется мне более предпочтительным вариантом. Именно его я выбрал для выполнения задач ветки питона.

### Шаг 1. Знакомство с Vagrant

Дабы создание виртуальной операционной системы не было сложным, я автоматизировал его при помощи vagrant. Vagrant - система конфигурирования среды виртуализации, позволяющая запускать виртуальные машины при помощи набора скриптов.

Сначала запустим центр приложений и установим vagrant:

![vagrant](media/vagrant/step_00.png)

Затем убедимся, что наш virtualbox сохраняет свои конфигурации в goinfre:

![vagrant](media/vagrant/step_02.png)

Иначе может не хватить памяти на школьном маке. На домашних машинах можно выбирать любой удобный раздел.

Специально под эту задачу я подготовил конфигурацию vagrant на debian с python3.11. Скачаем её в goinfree:

``git clone https://github.com/codesshaman/vagrant_python_debian.git``

Далее нам необходимо скачать образ debian11 с [vagrantup](https://app.vagrantup.com/bento/boxes/debian-11 "vagrantup"):

![vagrant](media/vagrant/step_01.png)

Скачиваем из строки с virtualbox и сохраняем в папку склонированного репозитория под именем debian.

Теперь редактируем Vagrantfile, изменив в нём переменные с выделенным процессором, памятью и ссылкой на гит-репозиторий. На школьных маках выделенные ресурсы можно не менять, а вот на более слабых ПК можно уменьшить количество выделенных ресурсов во избежании подвисаний. Ну а ссылку на свой проект указывать не обязательно, можно склонировать его уже после установки вручную.

Далее надо выполнить последовательно лишь две команды:

``make build`` и ``make``.

Подробнее процесс установки описан в Readme репозитория.

### Шаг 2. Подключение к конфигурации

Чтобы зайти на созданную виртуальную машину достаточно команды ``make connect`` из каталога репозитория или же подключения по ssh из любого терминала:

``ssh vagrant@192.168.58.98``

Если мы указали в Vagrantfile ссылку на репозиторий нашего проекта, мы должны увидеть папку с именем репозитория в корневой директории.

Но подключаться по ssh из терминала неудобно, потому используем плагин remote_SSH чтобы работать непосредственно из VsCode.

Находим в поиске по плагинам "Remote - SSH" и устанавливаем его.

Создаём новое соединение:

![vagrant](media/vagrant/step_03.png)

Вводим следующую команду для подключения:

``ssh vagrant@192.168.58.98``

И добавляем его в конфиг ssh. Теперь, после того как мы обновим список соединений, мы увидим наш локальный сервер и сможем с ним соединиться:

![vagrant](media/vagrant/step_04.png)