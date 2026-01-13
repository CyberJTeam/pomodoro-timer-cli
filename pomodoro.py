import time
import os

def get_timer_settings():
    print("--- Pomodoro Timer ---")

    while True:
        try:
            work_mins = int(input("Mau belajar berapa lama (menit)? "))
            break_mins = int(input("Mau istirahat berapa lama (menit)? "))

            if work_mins > 0 and break_mins > 0:
                work_secs = work_mins * 60
                break_secs = break_mins * 60
                return work_secs, break_secs
            else:
                print("Masukinnya jangan dibawah 0 dong")
        except ValueError:
            print("Invalid")

def start_countdown(seconds, label):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"[{label}] {timer_display}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n--- {label} SELESAI! ---")

def main():
    work_secs, break_secs = get_timer_settings()
    pomodoro_count = 0
    try:
        while True:
            pomodoro_count += 1
            print(f"\n--- Pomodoro ke-{pomodoro_count} ---")
            start_countdown(work_secs, "BELAJAR")
            print("\a")

            start_countdown(break_secs, "ISTIRAHAT")
            print("\a")

            pilihan = input(f"\nSesi {pomodoro_count} selesai. Lanjut lagi? (y/n): ").lower()
            if pilihan != 'y':
                print(f"Hebat! Kamu sudah menyelesaikan {pomodoro_count} sesi belajar.")
                break
    except KeyboardInterrupt:
            print("\n\nPomodoro berhenti. Sampai Jumpa!")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()