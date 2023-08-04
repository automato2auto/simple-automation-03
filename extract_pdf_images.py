# استيراد للأدوات والمكاتب التي ستساعدنا
import fitz
from PIL import Image
import os 

# إنشاء مجلد الصور الناتجة في حال لم يكن موجود
if os.path.isdir('./img'):

    os.mkdir("./img")

# فتح ملف ال PDF
doc = fitz.open('مسار_الملف.pdf')

# القائمة يلي رح نحفظ فيها الصور المستخرجة
images_list = []

# استخراج  معلومات الصور من صفحات الملف وإضافتها لقائمة الصور
for page in doc:
    images_list.extend(page.get_images())

# في حال لم يكن هنالك صور يتم طباعة رسالة بذلك
if not images_list:
    print(f'{file_path} has no images')

# حفظ الصور إلى الجهاز في مجلد img
for i, img in enumerate(images_list, start=1):
    # استخراج بيانات الصورة من الملف
    base_image = doc.extract_image(img[0])
    image_name = str(i) + '.' + base_image['ext']
    # حفظ الصورة إلى الجهاز
    with open(f'./img/{image_name}', 'wb') as image_file:
        image_file.write(base_image['image'])
        image_file.close()
# <a href="https://www.freepik.com/icons/pic">Icon by Freepik</a>