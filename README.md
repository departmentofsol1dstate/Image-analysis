# Инструкция по работе с программой (программа поддерживает ОС Windows 7-10)

<h4>0. Загрузите из репозитория файлы: 'GUI.py', 'image_analysis.py', 'requirements.txt'.</h4>
<h4>1. Проверьте что 'GUI.py', 'image_analysis.py', 'requirements.txt' лежат в одной папке (лучше создать под них отдельную папку).</h4>
<h4>2. Установите python:</h4>

	1) Скачайте установщик python (с учетом разрядности вашей ОС): https://www.python.org/downloads/release/python-3810/.
	2) Запустите файл 'python-3.8.10-64.exe', если у вас 64 разрядная система или 'python-3.8.10-32.exe', если 32 разрядная.
	3) Поставьте ✓ напротив пункта: 'ADD Python 3.8 to PATH'.
	4) Нажмите 'Install Now'.
	5) Закройте установщик.
<h4>4. Откройте командную строку:</h4>

	1 способ: нажмите 'win'+'r' на клавиатуре и в окне выполнить введите 'cmd', после нажмите 'OK'.
	2 способ: нажмите на 'Пуск' в левом нижнем углу экрана, введите в поисковой строке 'Командная строка', выбирите ее из списка, запустите ее.
<h4>5. В появившейся командной строке последовательно введите команды (с подключением к интернету):</h4>

	1) 'python -V', если вы увидели: 'Python 3.8.10...', продолжайте; иначе установите python по инструкции еще раз (пункт 2).
	2) 'pip install -r requirements.txt.
	3) 'exit'.
<h4>6. Запустите файл 'GUI.py':</h4>

	1 способ: нажмите правой кнопкой мыши на 'GUI.py', из предложенного выберите: 'Открыть с помощью'->'Python'. Должно открыться окно, в котором отображается графический интерфейс программы.
	2 способ: (Если 1 способ не работает): снова откройте командную строку, выполните команду 'cd [путь к папке с файлами GUI.py, image_analysis.py]'.
<h4>7. Интерфейс программы:</h4>

(Про параметры ф-ий читать в приложении) В открывшемся окне нажмите 'Выберите фотографию' и выберите нужную фотографию в формате '.png' (при необходимости предварительно переведите в этот формат).
На первой вкладке выведутся 2 изображения: левое - исходное, правое - обработанное с контурами длинее 50 пикселей (синим цветом закрашены контуры, также эти контуры пронумерованы), оно выведено с параметрами: 140, 50. На панели снизу выводится количество контуров: до и после обработки.
Перейдите на вторую вкладку (Пока на ней то же изображение, что и на первой вкладке справа).
На второй вкладке есть 2 шкалы, отвечающие за изменяемые параметры. Отрегулируйте ползунок на шкалах на нужное значение и нажмите на кнопку 'Анализ'. 
На второй вкладке вам выведется обработанное изображение с выбранным пороговым значением для выделения контуров и выбранным ограничением на длину контуров.
Правое изображение на первой вкладке теперь обработано с выбранным пороговым значением для выделения контуров, без ограничения на длину контуров.

Можно эксперементировать с параметрами, пока не получится найти параметры, при которых дефекты лучше всего детектируются. После можно выбрать следующую фотографию для анализа.
<h4>8. Закройте программу, нажав на крестик в правом верхнем углу экрана.</h4>


<h3>Когда вы установите питон и нужные библиотеки для него, больше вам не придется этого делать!</h3>
