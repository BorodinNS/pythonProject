import re

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
text_string = 'Филип Сентер выделил в рассматриваемой литературе несколько вариантов биологического объяснения ' \
              'возможности изрыгать огонь у динозавров с подробным разбором каждого варианта (каждый из этих вариантов' \
              ' по его мнению может претендовать на статус самостоятельной гипотезы)[1]. Генри Моррис (Henry Morris) ' \
              'в 1984 году и Джеймс Гилмер (James Gilmer) в 2011 году предположили, что динозавры могли изрыгать ' \
              'самовоспламеняющийся на воздухе газ. Сентер в опровержение данной гипотезы замечает, что выпущенный ' \
              'из дыхательных путей крупного животного такой газ воспламенился бы немедленно с обжиганием морды ' \
              'или даже горла животного. При этом он замечает, что данную опасность для самого динозавра ' \
              'могли бы устранить огнестойкие ткани верхних дыхательных путей (например, негорючий минеральный покров ' \
              'из карбоната или фосфатов кальция), однако, во-первых, такие покровы не известны у животных, ' \
              'а во-вторых не обнаружены в окаменелостях динозавров (где должны были бы обязательно сохраниться)[1]. ' \
              'На основе того факта, что травоядные испускают большое количество метана Джон Моррис (John Morris) в ' \
              '1999 году высказал предположение, что крупные травоядные динозавры могли отрыгивать накапливаемый им ' \
              'метан с одновременным поджиганием. Сентер в опровержение замечает, что метан в первую очередь образовал ' \
              'бы облако, что привело бы к обширным ожогам головы динозавра[1]. DeYoung в 2000 году и Гилмер ' \
              'в 2011 году выдвинули предположение, что у динозавров могли быть аналогичные электрическим рыбам ' \
              'и электрическим скатам природные органы генерации электричества, посредством которых они вырабатывали ' \
              'искры для поджигания метана. Помимо уже упомянутой опасности метана в первую очередь для самого ' \
              'динозавра Сентер отметил, что электрический разряд легче распространяется в воде и биологических тканях' \
              ' и намного труднее в воздухе и метане. Поэтому даже в случае достаточного электрического напряжения ' \
              'между челюстями динозавра при открытой глотке произойдёт не проскакивание искры в воздухе между ' \
              'челюстями, а проход тока в обход через челюстную мускулатуру динозавра[1]. ' \
              'Гилмер в 2011 году выдвинул предположение, что динозавры могли получать искру для воспламенения метана ' \
              'путём трения твёрдых покровов «во рту, в горле, [или] во внутренних органах». Однако Сентер замечает, ' \
              'что входящие в состав тела животных твёрдые вещества не образуют искру при трении, для этого ' \
              'потребовалась бы такая форма кварца, как кремень. По данным работы Erlich и Newman в 2009 году ' \
              'некоторые микроорганизмы могут выделять в результате своей жизнедеятельности кремний, ' \
              'однако вызванная во рту или горле динозавра искра привела бы к сильным ожогам дыхательных путей. ' \
              'Во внутренних органах к тому же отсутствует кислород, необходимый для поддержания пламени[1]. ' \
              'Isaacs в 2010 году, Batdorf и Porch в 2013 году и Lacy в 2013 году выдвинули предположение, что ' \
              'динозавры могли изрыгать отдельно две пары химических соединений, которые воспламенялись в результате ' \
              'контакта друг с другом (гипергольная смесь окислителя и горючего). В опровержение Филип Сентер ' \
              'замечает, что хотя известно много таких пар химических соединений, однако почти все они либо ' \
              'изобретены человеком, либо имеют слишком низкую температуру для живых существ. ' \
              'Только пероксид водорода как окислитель и аммиак как горючее могут подходить для живых существ. ' \
              'Но подходящие для пироксида водорода горючие вещества (керосин, пентаборан, или смеси, включающие ' \
              'гидразин и метанол) слишком ядовиты для живых существ. Подходящие для аммиака окислители ' \
              '(жидкий кислород и жидкий фтор) имеют температуру кипения в −183º C и −188º C соответственно, ' \
              'что неприемлемо для живых организмов. Дополнительно встаёт проблема, что газообразные формы ' \
              'гипергольных смесей окутают голову динозавра, в случае применения газообразного и жидкого компонента ' \
              'газообразный компонент при взаимодействии со струёй жидкого компонента достигнет животного, а ' \
              'применение только жидких компонентов для безопасности самого животного требует их соединения на ' \
              'достаточно большом расстоянии от динозавра[1].'
count = len(re.findall(r'\w+', text_string)) #удаляем знаки препинания
print(f'Количество слов в строке (исключая знаки препинания и регистр символов): {count}')

change_registr = text_string.lower()  # ровняем регистр слов для облегчения подсчета

count_word = {}
for word in change_registr.split():
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1
print(count_word)
# print(sorted(count_word.values(), reverse=True))
# print(sorted(count_word.items(), reverse=True))
# for word, count_word in count_word.items():
#   print(sorted(count_word, key=lambda x: x[1]))

sorted_tuple = sorted(count_word.items(), key=lambda x: x[1])
print(list(reversed(sorted_tuple)))
print("Десять самых встречаемых слов: ")
for i in list(reversed(sorted_tuple))[:10]:
    print([i])
