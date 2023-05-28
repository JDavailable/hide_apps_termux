DEBUG_IS = True # Если True будет отображаться лог выполнения

path_to_screen_folder =  '/sdcard/Pictures/Screenshots' # Путь к папке со скринами
path_to_tg_downloads = "/sdcard/Download/Telegram"  # указываем путь к папке, которую нужно удалить
path_to_screenrecords_folder = "/sdcard/Movies/" # звездочка ОБЯЗАТЕЛЬНА

launcher = "amirz.shade" # Другой лаунчер который установиться как дефолтный

home_path = "HOME=/data/data/com.termux/files/home2" # Путь к фейковому home для термукс
true_termux_home = 'HOME=/data/data/com.termux/files/home' # Стандартый home *Измените если вы используете нестандартный home 

path_to_conf = "/data/data/com.termux/files/home/.zshrc"
path_to_termux_prop = "/data/data/com.termux/files/home/.termux/termux.properties"

str_for_termux_prop = "default-working-directory = " + home_path
default_str_for_termux_prop = "default-working-directory = " + true_termux_home

# Список арок которые нужно скрыть
app_list = (
    "com.kylecorry.trail_sense",
	"ua.privatbank.ap24",
	"ua.gov.diia.app",
	"csmh.ifibbpb",
	"com.looker.droidify", 
	"dev.ukanth.ufirewall.donate",
	"us.spotco.fennec_dos",
	"com.mixplorer",
	"com.foobnix.pro.pdf.reader",
	"com.github.libretube",
	"ru.fourpda.client",
	"com.foxdebug.acode",
	"com.nononsenseapps.feeder",
	"com.blacksquircle.ui",
	"org.cryptomator",
	"org.chromium.chrome"
	)
# Такой же список, только для user 10(work profile) !!ПРЕДВАРИТЕЛЬНО ПРОВЕРЬТЕ СОВПАДАЕТ ЛИ USER ID!!
app_list_user10 = (
	"com.fsck.k9",
	"com.android.documentsui"
	)

# Список триггеров по которым делитаются скрины
# Прошивка или приложение для скриншотов должно прописывать имя приложения в названии 
del_screen_app_list = (
	'Telegram', 
	"Quickstep", 
	"Termux", 
	"Mull",
	"Feeder"
	)
