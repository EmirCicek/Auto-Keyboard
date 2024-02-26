import pyautogui
import time
import keyboard
import webbrowser


# Fonksiyonlar

def prompt_al(text,title="Otomatik Tıklayıcı"):
    return pyautogui.prompt(text, title)

def confirm_et(text,buttons,title="Otomatik Tıklayıcı"): # Buttonlar liste ile verilmeli ==> ['OK', 'Cancel']
    return pyautogui.confirm(text=text, title=title, buttons=buttons)

def tus_bas(tus):
    pyautogui.hotkey(tus)

def tus_basildi_mi(tus):
    return keyboard.is_pressed(tus)



# Main Code

def main():
    islem_tipi = confirm_et("İşlem Tipini Seçiniz",["Yazı Yazdır","Tuşa Bastır"])
    if islem_tipi == "Yazı Yazdır":
        metin = prompt_al("Metin Giriniz")
        saniye_araligi = float(prompt_al("Saniye Aralığı Giriniz"))
        islem_onayı = confirm_et("İşlem 10 Saniye Sonra Başlatılıyor. İşlem Sırasında İşlemi Sonlandırmak için Esc ve F9 tuşlarına aynanda basılı tutunuz. İşlemi onaylıyor musunuz?",["Evet","Hayır"])
        if islem_onayı == "Evet":
            time.sleep(10)
            while not tus_basildi_mi("esc+f9"):
                pyautogui.typewrite(metin)
                time.sleep(saniye_araligi)
    elif islem_tipi == "Tuşa Bastır":
        tus = prompt_al("Tus Giriniz")
        saniye_araligi = float(prompt_al("Saniye Aralığı Giriniz"))
        islem_onayı = confirm_et("İşlem 10 Saniye Sonra Başlatılıyor. İşlem Sırasında İşlemi Sonlandırmak için Esc ve F9 tuşlarına aynanda basılı tutunuz. İşlemi onaylıyor musunuz?",["Evet","Hayır"])
        if islem_onayı == "Evet":
            time.sleep(10)
            while not tus_basildi_mi("esc+f9"):
                tus_bas(tus)
                time.sleep(saniye_araligi)
    yonlendirme = confirm_et("İşlem Sona Erdi. \n github.com/emircicek \n https://t.me/emircicek25",["Github ve Telegram Sayfalarını Ziyaret Et","Programı Kapat"])

    if yonlendirme == "Github ve Telegram Sayfalarını Ziyaret Et":
        webbrowser.open_new_tab("https://github.com/emircicek")
        webbrowser.open_new_tab("https://t.me/emircicek25")


main()
