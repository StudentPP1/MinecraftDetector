from ultralytics import YOLO
import pyautogui
import keyboard
import tkinter as tk

"""
For start detecting you have to press '+' on keyboard
For stop detecting you have to press '-' on keyboard
For exit program you have to press '0' on keyboard
"""

model = YOLO("best.pt")


def get_cords_nearest_player(path_img: str) -> list[int] or None:
    try:
        predict = model.predict(path_img, save=True)
        results = [[box.conf.item(), [round(i.item()) for i in box.xyxy[0]]] for box in predict[0].boxes]
        max_value = max([i[0] for i in results])

        for result in results:
            if result[0] == max_value:
                return result[1]
    except Exception as ex:
        print(ex)
        return None


def on_press():
    root = tk.Tk()
    root.wait_visibility(root)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-fullscreen", 1)
    root.wm_attributes("-transparentcolor", root['bg'])
    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
    canvas.pack()

    while True:
        if keyboard.is_pressed("-"):   # break while
            root.destroy()
            break

        pyautogui.screenshot("screenshot.png")
        cords = get_cords_nearest_player("screenshot.png")
        # get box coordinates in (top - x1, left - y1, bottom - x1, right - y1)    0    if cords:

        canvas.delete('all')
        print(cords)

        if cords:
            canvas.create_line(cords[0], cords[1], cords[2], cords[1], fill="red")
            canvas.create_line(cords[0], cords[3], cords[2], cords[3], fill="red")
            canvas.create_line(cords[0], cords[1], cords[0], cords[3], fill="red")
            canvas.create_line(cords[2], cords[3], cords[2], cords[1], fill="red")

            root.update()

        else:
            print("Deleting")
            canvas.delete('all')
            root.update()


def main():
    while True:
        if keyboard.is_pressed("="):
            on_press()
        elif keyboard.is_pressed("0"):
            break


if __name__ == "__main__":
    main()

