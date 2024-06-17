import time
from PIL import Image, ImageFilter
import concurrent.futures

img_names = [
    "photo-1516117172878-fd2c41f4a759.jpg",
    "photo-1532009324734-20a7a5813719.jpg",
    "photo-1524429656589-6633a470097c.jpg",
    "photo-1530224264768-7ff8c1789d79.jpg",
    "photo-1541698444083-023c97d3f4b6.jpg",
    "photo-1522364723953-452d3431c267.jpg",
    "photo-1516972810927-80185027ca84.jpg",
    "photo-1530122037265-a5f1f91d3b99.jpg",
    "photo-1516972810927-80185027ca84.jpg",
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_img(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(10))
    img.thumbnail(size)

    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed...")


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, img_names)

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1} seconds")
