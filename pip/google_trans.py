from googletrans import Translator

tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz, src='uz', dest='ru')
# google o'zi aniqlaydi source tilni, ammo src ni qo'ysak ham bo'laveradi
print(tarjima.text)
