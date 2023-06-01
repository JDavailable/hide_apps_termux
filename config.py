DEBUG_IS = True # Если True будет отображаться лог выполнения
NOTIFICATION = True # Если True вы получите уведомление от termux-api о процессе выволнения кода
path_to_screen_folder =  '/sdcard/Pictures/Screenshots' # Путь к папке со скринами
path_to_tg_downloads = "/sdcard/Download/Telegram"  # указываем путь к папке, которую нужно удалить
path_to_screenrecords_folder = "/sdcard/Movies/" # звездочка ОБЯЗАТЕЛЬНА

launcher = "amirz.shade" # Другой лаунчер который установиться как дефолтный
true_launcher = "com.android.launcher3"
home_path = "HOME=/data/data/com.termux/files/home2" # Путь к фейковому home для термукс
true_termux_home = 'HOME=/data/data/com.termux/files/home' # Стандартый home *Измените если вы используете нестандартный home 

path_to_conf = "/data/data/com.termux/files/home/.zshrc"
path_to_termux_prop = "/data/data/com.termux/files/home/.termux/termux.properties"

str_for_termux_prop = "default-working-directory=/data/data/com.termux/files/home2"
default_str_for_termux_prop = "default-working-directory=/data/data/com.termux/files/home"

# Список арок которые нужно скрыть
app_list = (
    "com.exteragram.messenger",
    "com.kylecorry.trail_sense",
	"ua.privatbank.ap24",
	"ua.gov.diia.app",
	"io.github.huskydg.magisk",
	"com.looker.droidify", 
	"dev.ukanth.ufirewall.donate",
	"com.mixplorer",
	"com.foobnix.pro.pdf.reader",
	"com.github.libretube",
	"ru.fourpda.client",
	"com.foxdebug.acode",
	"com.nononsenseapps.feeder",
	"com.blacksquircle.ui",
	"org.cryptomator",
	"org.chromium.chrome",
	"us.spotco.fennec_dos",
	"io.github.deweyreed.clipboardcleaner",
	"org.nuntius35.wrongpinshutdown",
	"mstoic.apps.disablefingerprintunlocktemporarily",
	"com.smartpack.kernelmanager",
	"com.trianguloy.urlchecker",
	"com.fox2code.mmm",
	"com.drdisagree.iconify",
	"github.tornaco.android.thanos"
	)
# Такой же список, только для user 10(work profile) !!ПРЕДВАРИТЕЛЬНО ПРОВЕРЬТЕ СОВПАДАЕТ ЛИ USER ID!!
app_list_user10 = (

	)

# Список триггеров по которым делитаются скрины
# Прошивка или приложение для скриншотов должно прописывать имя приложения в названии 
del_screen_app_list = (
	'Telegram', 
	"Quickstep", 
	"Termux", 
	"Mull",
	"Feeder",
	"LMODroid",
	"exteraGram",
	)
