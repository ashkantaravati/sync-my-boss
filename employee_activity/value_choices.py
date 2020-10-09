WORK_UPDATE_TYPES = (
    ("Work Started", "کار شروع شد"),
    ("Work Paused", "کار متوقف شد"),
    ("Work Stuck", "کار با مانع رو به رو شد"),
    ("Work Advanced", " کار در حال پیشروی است"),
    ("Work Succeeded", "کار با موفقیت پایان یافت"),
    ("Work Canceled", "کار لغو شد"),
    ("Work Failed", "کار با شکست مواجه شد"),
)

ATTENDANCE_ACTION_TYPES = (("Enter", "ورود"), ("Exit", "خروج"))


AVAILABILITY_STATUS_REASON_TYPES = (
    ("Available", "در دسترس"),
    ("In a Meeting", "در جلسه"),
    ("Focusing", "در حال تمرکز"),
    ("Busy", "مشغول"),
    ("On Hourly Leave", "در مرخصی ساعتی"),
    ("On Daily Leave", "در مرخصی روزانه"),
    ("Left Work", "سازمان را ترک کرده"),
    ("Away", "ترک میز"),
    ("Away for a meal", "ترک میز برای صرف وعده‌ی غذایی"),
)

DAYLONG_STATUS_TYPES = ["On Daily Leave"]
INDEFINITE_STATUS_TYPES = ["Available","Left Work"]

ACTIVITY_TYPES = (
    ("Sales", "فروش"),
    ("Marketing", "بازاریابی"),
    ("Project Management", "مدیریت پروژه"),
    ("Operations", "عملیات"),
    ("Human Resources", "امور منابع انسانی"),
    ("Support", "پشتیبانی"),
    ("Research and Development", "تحقیق و توسعه"),
    ("Learning and Development", "آموزش و توسعه"),
    ("Product Management", "مدیریت محصول"),
    ("Finance", "امور مالی"),
    ("Software Development", "توسعه‌ی نرم‌افزار"),
    ("Design", "طراحی"),
    ("Search Engine Optimization", "بهینه‌سازی موتور جستجو"),
    ("Contracts", "امور قراردادها"),
    ("General", "عمومی"),
)